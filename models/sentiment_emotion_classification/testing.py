import pickle
import numpy as np
import tensorflow as tf
import swifter
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import re, string, unicodedata
from langdetect import detect
from googletrans import Translator
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import chardet
import json
import argparse
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# --- Text Preprocessing Setup ---
# try:
#     translator = Translator()
#     factory = StemmerFactory()
#     stemmer = factory.create_stemmer()
# except Exception as e:
#     print(f"Error initializing preprocessing tools: {e}")
#     # Consider adding fallback mechanisms or exiting if these are critical

merged_slang_file = '../../data/slang/merged_slang_dict.json'
with open(merged_slang_file, 'r', encoding='utf-8') as f:
    slang_dict = json.load(f)

# Define stop words (consider loading from a file for larger lists)
stop_words = set(stopwords.words('indonesian'))

class IndoTextPreprocessor:
    def __init__(self):
        self.lowercase = True
        self.remove_non_ascii = True
        self.remove_punctuation = True
        self.remove_numbers = True
        self.remove_stopwords = True
        self.stemming = False
        self.remove_extra_spaces = True

    def normalize_slang(self, text):
        tokens = text.split()
        return ' '.join(slang_dict.get(word, word) for word in tokens)

    def clean_text(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return "" # Return empty string for non-strings or empty input
        # try:
        #     # Basic language check (optional, can be slow)
        #     # lang = detect(text)
        #     # if lang != "id":
        #     #     text = translator.translate(text, src=lang, dest="id").text
        #     pass # Skipping translation for now to avoid potential errors/rate limits
        # except Exception as e:
        #     # print(f"Language detection/translation error for text: '{text[:50]}...': {e}")
        #     pass # Continue processing even if translation fails

        if self.lowercase:
            text = text.lower()
        text = re.sub(r"http\S+|www\S+|https\S+", '', text) # Remove URLs
        text = re.sub(r'<.*?>', '', text) # Remove HTML tags
        if self.remove_non_ascii:
            text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        if self.remove_punctuation:
            # Keep spaces, remove punctuation
            text = text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
        if self.remove_numbers:
            text = re.sub(r'\d+', '', text) # Remove numbers

        text = self.normalize_slang(text) # Normalize slang

        tokens = text.split() # Tokenize by space

        if self.remove_stopwords:
            tokens = [word for word in tokens if word not in stop_words]

        # Join before stemming for Sastrawi
        text_to_stem = ' '.join(tokens)

        if self.stemming:
            try:
                text_to_stem = stemmer.stem(text_to_stem)
            except Exception as e:
                # print(f"Stemming error for text: '{text_to_stem[:50]}...': {e}")
                pass # Continue without stemming if error occurs
            tokens = text_to_stem.split() # Re-split after stemming

        cleaned_text = ' '.join(tokens)

        if self.remove_extra_spaces:
            cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

        # Handle cases where text becomes very short or repetitive after cleaning
        if len(cleaned_text) <= 3 or re.fullmatch(r'(.)\1{2,}', cleaned_text):
             return "kosong" # Return placeholder instead of empty

        return cleaned_text

    def transform(self, text_series):
        # Apply cleaning function to each element in the Pandas Series
        return text_series.swifter.apply(self.clean_text)

# --- Load NN Model and Components ---
try:
    print("Loading tokenizer...")
    tokenizer = pickle.load(open("../../models_dump/sentiment_emotion_classification_dump/tokenizer.pkl", "rb"))
    print("Loading label encoders...")
    le_emosi = pickle.load(open("../../models_dump/sentiment_emotion_classification_dump/le_emosi.pkl", "rb"))
    le_sentimen = pickle.load(open("../../models_dump/sentiment_emotion_classification_dump/le_sentimen.pkl", "rb"))
    print("Loading NN model...")
    nn_model = tf.keras.models.load_model("../../models_dump/sentiment_emotion_classification_dump/nn_multitask_model.h5")
    print("Components loaded successfully.")
except FileNotFoundError as e:
    raise RuntimeError(f"Model, tokenizer, or label encoder file missing: {e}")
except Exception as e:
    raise RuntimeError(f"Error loading components: {e}")

# --- Prediction Logic (NN Only) ---
def predict_nn_only(cleaned_texts_series):
    """
    Performs prediction using only the NN model.

    Args:
        cleaned_texts_series (pd.Series): A Pandas Series containing the
                                          preprocessed text data.

    Returns:
        tuple: A tuple containing two lists:
               - List of predicted emotion labels.
               - List of predicted sentiment labels.
    """
    if not isinstance(cleaned_texts_series, pd.Series):
         raise ValueError("Input must be a Pandas Series.")

    # Handle potential "kosong" placeholders if needed, or ensure tokenizer handles them
    # texts_to_process = cleaned_texts_series.replace("kosong", "").tolist() # Example handling
    texts_to_process = cleaned_texts_series.tolist()

    print("Tokenizing and padding sequences...")
    sequences = tokenizer.texts_to_sequences(texts_to_process)
    padded = pad_sequences(sequences, maxlen=120, padding='post', truncating='post')

    print("Predicting with NN model...")
    # Predict using the loaded NN model
    nn_pred_emosi_prob, nn_pred_sentimen_prob = nn_model.predict(padded, batch_size=64, verbose=0) # Use verbose=0 for less output

    # Get the class index with the highest probability
    nn_pred_emosi_indices = np.argmax(nn_pred_emosi_prob, axis=1)
    nn_pred_sentimen_indices = np.argmax(nn_pred_sentimen_prob, axis=1)

    print("Decoding predictions...")
    # Convert indices back to original labels
    predicted_emosi = le_emosi.inverse_transform(nn_pred_emosi_indices).tolist()
    predicted_sentimen = le_sentimen.inverse_transform(nn_pred_sentimen_indices).tolist()

    return predicted_emosi, predicted_sentimen


# --- Main Execution Logic ---
if __name__ == "__main__":
    # Setup argument parser to get input and output file paths
    input_file = 'data.csv'
    output_file = 'output.csv'

    print(f"Reading input CSV: {input_file}")
    try:
        # Read the CSV file specified by the command-line argument
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file}")
        exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        exit(1)

    # Check if 'ulasan' column exists in the loaded CSV
    if 'content' not in df.columns:
        print(f"Error: Input CSV '{input_file}' must contain a column named 'content'. Found columns: {df.columns.tolist()}")
        exit(1)

    print("Preprocessing 'content' column...")
    preprocessor = IndoTextPreprocessor()
    # Fill NaN values in the 'content' column with empty strings before processing
    df['ulasan_cleaned'] = preprocessor.transform(df['content'].fillna(''))

    print("Starting prediction process...")
    try:
        # Get predictions using only the NN model based on the cleaned 'ulasan' column
        predicted_emosi, predicted_sentimen = predict_nn_only(df['ulasan_cleaned'])

        # Add predictions as new columns to the DataFrame
        df['pred_emosi'] = predicted_emosi
        df['pred_sentimen'] = predicted_sentimen

        # Remove the intermediate cleaned column
        df = df.drop(columns=['ulasan_cleaned'])

        print(f"Saving results to: {output_file}")
        # Save the DataFrame (including original columns + new predictions)
        # to the CSV file specified by the command-line argument
        df.to_csv(output_file, index=False, encoding='utf-8') # Specify encoding for safety
        print("Processing complete.")
        print(f"File output disimpan sebagai: {output_file}")

    except Exception as e:
        print(f"An error occurred during prediction or saving: {e}")
        exit(1)