import pandas as pd
import csv

df = pd.read_csv("../data/main_dataset/dataset_spam_nlp_v5.csv")

mapping = {
    0: "genuine_review",
    1: "irrelevant_content",
    2: "explicit_spam"
}

df['kategori'] = df['kategori'].map(mapping)

# df = df.rename(columns={"Label": "kategori"})
# df = df.rename(columns={"ReviewText": "ulasan"})

df.to_csv(
    "dataset_spam_nlp.csv",
    index=False,
    quoting=csv.QUOTE_ALL,
    quotechar='"'
)