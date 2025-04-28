import csv
import io
import random
import os # Import os module for path manipulation

# --- Data Generation Functions ---

def generate_genuine_reviews(count):
    """Generates varied genuine reviews (Label 0) with real examples."""
    reviews = []
    # --- MODIFIED & ADDED TEMPLATES (Increased Variety & Lowercase) ---
    templates = [
        # Original templates modified/kept/expanded & lowercased
        # --- ADDED: Short Genuine Review Templates (Lowercase) ---
        "b aja sih",
        "biasa aja",
        "lumayan",
        "okelah",
        "cukup",
        "mayan",
        "not bad",
        "oke",
        "sip",
        "standar",
        "cukup bagus",
        "lumayan bagus",
        "oke banget",
        "mantap",
        "keren",
        "bagus",
        "good",
        "nice",
        "bermanfaat",
        "membantu",
        "work",
        "berfungsi",
        "lancar",
        "stabil",
        "ringan",
        "cepat",
        "mudah",
        "simpel",
        "intuitif",
        "lengkap",
        "puas",
        "suka",
        "recommended",
        "top",
        "jelek",  # Short negative
        "buruk",  # Short negative
        "parah",  # Short negative
        "error",  # Short negative
        "lambat",  # Short negative
        "berat",  # Short negative
        "susah",  # Short negative
        "ribet",  # Short negative
        "kurang",  # Short negative
        "kecewa",  # Short negative
        "program ini {adjective} banget, {positive_aspect}",
        "sangat {verb} untuk {activity}",
        "fitur {feature} sangat {adjective}",
        "saya {emotion} dengan {negative_aspect}",
        "performa {performance_aspect} perlu {improvement_suggestion}",
        "{positive_exclamation}! {positive_comment}",
        "desain ui-nya {design_adjective}, {design_comment}",
        "setelah update terbaru ke versi {version_number}, {update_effect}",
        "cukup {neutral_adjective}, tapi {minor_issue}",
        "sangat direkomendasikan untuk {target_user}",
        "banyak {bug_type} setelah {event}",
        "tolong tambahkan fitur {requested_feature}, pasti berguna",
        "mudah digunakan, bahkan untuk {user_type}",
        "langganan premiumnya {price_opinion}, tapi {value_proposition}",
        "tidak {negative_experience} seperti {competing_app_type} lain",
        "{positive_statement} tentang {specific_function}",
        "agak {difficulty} di awal, tapi sekarang lancar jaya",
        "notifikasi {notification_issue}, tolong diperbaiki",
        "{general_positive_short}. recommended!",
        "{general_negative_short}. perlu banyak perbaikan",
        "berfungsi dengan baik di device {device_type} saya",
        "konsumsi baterai {battery_usage}, lumayan awet",
        "ukuran software ini {size_opinion}, tidak bikin memori penuh",
        "efek {effect_type} nya {effect_quality}, cocok buat konten",
        "membantu saya {achieved_goal} sehari-hari",
        "secara keseluruhan, {overall_positive_opinion}",
        "sayangnya, {specific_complaint}, jadi agak terganggu",
        "koneksi internet {connection_dependency} untuk fitur utama",
        "proses {process_type} berjalan {process_speed}",
        "customer supportnya {support_quality} via {support_channel}",
        "tutorial penggunaan awalnya {tutorial_quality}",
        "pilihan {option_type} cukup {option_variety}",
        "sering {positive_action} tanpa masalah sama sekali",
        "kadang {negative_action}, tapi jarang terjadi sih",
        "cocok banget untuk {specific_use_case}",
        "versi gratisnya {free_version_limitations}, tapi sudah cukup",
        "iklannya {ad_frequency} dan {ad_relevance}, tidak terlalu mengganggu",
        "update terakhir {update_frequency}, developernya aktif",
        "komunitas penggunanya di {community_platform} {community_activity}",
        "saya pakai di {location}, sinyal {signal_strength}, {app_performance_location}",
        "integrasi dengan {integrated_service} berjalan mulus",
        "keamanan datanya {security_opinion}, semoga aman",
        "apakah ada rencana untuk {future_feature}?",
        "setelah update {version_number}, malah muncul {bug_type}. tolong dong dev perbaiki segera",
        "pengalaman pakainya {design_adjective}, {design_comment}. mantap",
        "pengalaman pakainya {design_adjective}, {design_comment}. pusing",
        "buat {activity} jadi {difficulty}, payah banget aplikasi ini",
        "ini software {adjective} parah, {negative_aspect}. nyesel install!",
        "bisa dicoba buat {activity}, {positive_comment}",
        "kecewa berat! {negative_aspect} bikin {negative_experience}",
        "error {bug_type} terus menerus, padahal udah {event}",
        "awalnya {difficulty}, tapi setelah ikutin {tutorial_quality} tutorial jadi {adjective}",
        "kirain bakal {adjective}, ternyata {negative_aspect}. zonk!",
        "performanya {performance_aspect} {adjective} banget di {device_type}",
        "jelek , {general_negative_short}. {negative_aspect}",
        "bagus, {general_positive_short}. {positive_aspect}",
        "tolong {improvement_suggestion} untuk {performance_aspect}, ganggu banget soalnya",
        "fitur {feature} nya sih {adjective}, tapi sayang {negative_aspect}",
        "ui/ux nya {design_adjective} tapi sering {negative_action}",
        "sejak pakai ini, {achieved_goal}. {emotion}!",
        "bikin emosi jiwa! {negative_action} terus pas lagi butuh",
        "salut sama developernya, {update_frequency} update dan {support_quality} supportnya",
        "ini bukan {competing_app_type} biasa, ini lebih bagus {positive_aspect}",
        "walaupun {minor_issue}, secara umum program ini {adjective}", # mixed review
        "secara fungsi {adjective}, tapi {negative_aspect} perlu dibenahi", # mixed review
        "saya pakai untuk {specific_use_case}, dan hasilnya {adjective}", # use case specific
        "butuh waktu {learning_time} untuk terbiasa, tapi sekarang {positive_outcome}", # learning curve detail
        "terima kasih developer sudah {positive_developer_action}", # appreciation
        "versi {version_number} ini {update_effect}, jauh lebih baik dari sebelumnya", # positive update effect
        "versi {version_number} ini {update_effect}, tolong kembalikan seperti dulu", # negative update effect
        "saya harap {improvement_suggestion} bisa segera diimplementasikan", # hopeful suggestion
        "untuk {activity}, aplikasi ini {adjective}. tapi untuk {other_activity}, masih kurang", # contextual usefulness
        "nilai plusnya di {positive_aspect}, tapi minusnya di {negative_aspect}", # clear pros and cons
        "bintang {rating_number} dulu, kalau {condition_for_change} saya ubah", # conditional rating

        # --- ADDED: New Genuine Templates (Lowercase) ---
        "aplikasi ini {verb} banget buat {activity}, terutama fitur {feature}-nya",
        "sempet {emotion} karena {negative_aspect}, tapi setelah {event} jadi {adjective}",
        "buat {target_user} kayak saya, ini {adjective} dan {positive_aspect}",
        "ada {minor_issue} sih, tapi overall {overall_positive_opinion}",
        "kenapa ya fitur {feature} kok {negative_action}? padahal sebelumnya lancar",
        "request fitur {requested_feature} dong min, biar makin {adjective}",
        "di {device_type} saya {location}, performanya {performance_aspect} {adjective}",
        "setelah pakai beberapa minggu, kesimpulannya: {overall_positive_opinion}",
        "tutorial {tutorial_quality} sangat membantu, jadi cepat paham cara pakai {specific_function}",
        "harganya {price_opinion}, tapi sebanding lah sama {value_proposition}",
        "sering banget {positive_action}, bikin {achieved_goal} jadi lebih mudah",
        "tolong {improvement_suggestion} di bagian {negative_aspect}, biar lebih nyaman",
        "desainnya {design_adjective}, {design_comment}. saya suka!",
        "update {version_number} bikin {update_effect}, jadi {emotion}",
        "apakah {feature} ini memang {intended_behavior} atau bug ya?",
        "konsumsi baterai {battery_usage}, aman buat dipakai seharian",
        "ukuran {size_opinion} tidak masalah, yang penting {positive_aspect}",
        "efek {effect_type} nya {effect_quality}, bikin hasil {activity} jadi lebih pro",
        "koneksi {connection_dependency} jadi kendala kalau lagi di {location} dengan sinyal {signal_strength}",
        "proses {process_type} {process_speed}, nggak perlu nunggu lama",
        "cs via {support_channel} {support_quality}",
        "pilihan {option_type} {option_variety}, bisa disesuaikan selera",
        "cocok untuk {specific_use_case}, tapi mungkin kurang pas buat {other_activity}",
        "versi gratis {free_version_limitations}, tapi cukup buat kebutuhan dasar",
        "iklan {ad_frequency} dan {ad_relevance}, masih bisa ditolerir lah",
        "developernya {update_frequency} update, kelihatan kalau {positive_developer_action}",
        "komunitas di {community_platform} {community_activity}, banyak tips berguna",
        "integrasi {integrated_service} {adjective}, mempermudah workflow",
        "soal {security_opinion}, semoga developer terus menjaga kepercayaan pengguna",
        "kalau bisa, tambahin {future_feature} di update selanjutnya",
        "agak {difficulty} pas awal, tapi {learning_time} kemudian jadi {positive_outcome}",
        "saya kasih bintang {rating_number} karena {negative_aspect}, tapi kalau {condition_for_change} pasti naik",
        "ini {general_positive_short}, {positive_comment}",
        "ini {general_negative_short}, {negative_experience}",
        "fitur {feature} adalah {positive_statement}",
        "sayang sekali {specific_complaint}, padahal potensinya bagus",
        "notifikasi {notification_issue} bikin ketinggalan info penting",
        "buat {user_type}, aplikasi ini {adjective} karena {positive_aspect}",
        "performa {performance_aspect} di {device_type} saya {adjective}, padahal spek lumayan",
        "secara umum {overall_positive_opinion}, meski ada {minor_issue}",
        "saya {emotion} waktu tahu ada fitur {feature}, ini {positive_comment}",
        "tolong perbaiki {bug_type} yang muncul setelah {event}",
        "desain {design_adjective} tapi {negative_action}, perlu perbaikan ux",
        "langganan premium {price_opinion}? {value_proposition} jadi pertimbangan",
        "tidak {negative_experience}, malah {positive_aspect}",
        "butuh {learning_time} buat ngerti {specific_function}, tapi worth it",
        "terima kasih sudah {positive_developer_action}, kami sebagai pengguna merasa didengar",
        "versi {version_number} {update_effect}, semoga bug segera fix",
        "kalau {condition_for_change}, saya yakin ratingnya bisa bintang 5",
        "plus: {positive_aspect}. minus: {negative_aspect}",
        "untuk {activity} oke, tapi {other_activity} lebih baik pakai {competing_app_name}",
        "baterai {battery_usage}, ukuran {size_opinion}, performa {adjective}. mantap!",
        "efek {effect_type} {effect_quality}, tapi proses {process_type} agak {process_speed}",
        "cs {support_quality} lewat {support_channel}, tapi tutorial {tutorial_quality} kurang",
        "pilihan {option_type} {option_variety}, tapi sayang {free_version_limitations}",
        "iklan {ad_frequency} {ad_relevance}, update {update_frequency}. bagus!",
        "di {location} {signal_strength}, aplikasi {app_performance_location}",
        "integrasi {integrated_service} lancar, keamanan {security_opinion}",
        "semoga ada {future_feature} dan perbaikan {bug_type}",
        "awalnya {difficulty}, tapi setelah {learning_time} jadi {positive_outcome}. {emotion}!",
        "bintang {rating_number} karena {specific_complaint}. akan diubah jika {condition_for_change}",
        "program {adjective}, fitur {feature} {positive_aspect}",
        "sangat {verb} untuk {activity}, proses {process_type} {process_speed}",
        "saya {emotion} karena {negative_aspect}, padahal ekspektasi tinggi",
        "performa {performance_aspect} {adjective}, tapi {minor_issue}",
        "{positive_exclamation}! {positive_comment}, terutama {specific_function}",
        "desain {design_adjective} {design_comment}, tapi notifikasi {notification_issue}",
        "update {version_number} {update_effect}, tolong {improvement_suggestion}",
        "direkomendasikan untuk {target_user}, mudah dipakai oleh {user_type}",
        "banyak {bug_type} setelah {event}, bikin {negative_experience}",
        "tolong tambah {requested_feature}, akan sangat {verb}",
        "premium {price_opinion}, tapi {value_proposition} oke",
        "tidak {negative_experience}, malah {positive_action}",
        "{positive_statement} adalah {feature}",
        "agak {difficulty}, tapi tutorial {tutorial_quality} membantu",
        "{general_positive_short}, {overall_positive_opinion}",
        "{general_negative_short}, {specific_complaint}",
        "berfungsi baik di {device_type}, baterai {battery_usage}",
        "ukuran {size_opinion}, efek {effect_type} {effect_quality}",
        "membantu {achieved_goal}, tapi koneksi {connection_dependency}",
        "cs {support_quality} via {support_channel}, pilihan {option_type} {option_variety}",
        "sering {positive_action}, jarang {negative_action}",
        "cocok untuk {specific_use_case}, iklan {ad_frequency} {ad_relevance}",
        "update {update_frequency}, komunitas {community_platform} {community_activity}",
        "di {location} {signal_strength} {app_performance_location}, integrasi {integrated_service} mulus",
        "keamanan {security_opinion}, semoga ada {future_feature}",
        "setelah {learning_time} jadi {positive_outcome}, terima kasih {positive_developer_action}",
        "versi {version_number} {update_effect}, bintang {rating_number} jika {condition_for_change}",
        "plus: {positive_aspect}, minus: {negative_aspect}. untuk {activity} oke, {other_activity} kurang",
        "mantap {adjective}, fitur {feature} sangat {verb}",
        "kecewa {negative_aspect}, performa {performance_aspect} buruk",
        "ui {design_adjective}, tapi sering {negative_action}",
        "update {version_number} malah {update_effect} negatif",
        "rekomendasi buat {target_user}, tapi hati-hati {minor_issue}",
        "bug {bug_type} pas {event}, tolong {improvement_suggestion}",
        "gratis tapi {free_version_limitations}, premium {price_opinion}",
        "belajar {specific_function} butuh {learning_time}, tapi hasilnya {positive_outcome}",
        "developer {positive_developer_action}, update {update_frequency} bagus",
        "bintang {rating_number} karena {specific_complaint}, ubah kalau {condition_for_change}",
        "secara fungsi {adjective}, tapi {negative_aspect} mengganggu",
        "pakai di {device_type} {location}, {app_performance_location}",
        "proses {process_type} {process_speed}, tapi butuh {connection_dependency}",
        "cs {support_quality}, tutorial {tutorial_quality}, komunitas {community_activity}",
        "pilihan {option_type} {option_variety}, keamanan {security_opinion}",
        "semoga {future_feature} ada, integrasi {integrated_service} ditingkatkan",
    ]

    # --- Expanded Lists (More Variety, Real Examples, Lowercase) ---
    # (All keywords converted to lowercase)
    adjectives = ["membantu", "keren", "bagus", "stabil", "cepat", "ringan", "intuitif", "lengkap", "bermanfaat", "memuaskan", "buruk", "lambat", "berat", "membingungkan", "kurang", "mengecewakan", "responsif", "andal", "efisien", "powerful", "simpel", "fungsional", "inovatif", "user-friendly", "menyebalkan", "tidak berguna", "penuh bug", "boros", "luar biasa", "fantastis", "oke", "cukup baik", "payah", "parah", "mantap", "ngelag", "smooth", "gampang", "susah", "jelas", "membantu banget", "nggak jelas", "ampuh", "biasa aja", "istimewa", "solid", "mumpuni", "memadai", "kurang optimal", "tidak stabil", "kacau", "sempurna", "brilian", "ciamik", "top", "jempolan", "asyik", "menarik", "unik", "standar", "pas-pasan", "menyedihkan", "mengganggu", "ribet", "kompleks", "fleksibel", "powerful"]
    positive_aspects = ["banyak pilihan filter keren", "mudah dinavigasi antar menu", "tidak ada iklan sama sekali", "sering update fitur baru yang berguna", "cocok untuk pemula seperti saya", "hasilnya berkualitas hd", "hemat kuota internet", "bisa dipakai mode offline", "tampilannya bersih dan modern", "banyak template siap pakai", "komunitasnya aktif saling bantu", "cs responsif via email", "cs responsif via chat", "bisa ekspor ke format mp4", "bisa ekspor ke format jpg", "proses rendering cepat", "tidak bikin hp panas", "ukurannya kecil", "fitur ainya cerdas", "opsi kustomisasi lengkap", "sinkronisasi antar perangkat lancar", "auto save berfungsi baik", "banyak pilihan font", "ada fitur kolaborasi", "gratis tapi fitur lengkap", "tidak ada watermark", "dukungan pelanggan cepat", "tutorialnya jelas", "interface menarik", "bisa import banyak format"]
    verbs = ["membantu", "berguna", "cocok", "efektif", "penting", "memudahkan", "mempercepat", "menginspirasi", "menghibur", "menghemat", "meningkatkan", "menyelesaikan", "mengatasi", "membuat", "menjadi", "mendukung", "mengoptimalkan", "menyederhanakan", "mempercantik", "mengatur", "menganalisis", "memvisualisasikan", "mengkreasikan"]
    activities = ["mengelola keuangan pribadi", "belajar bahasa inggris", "belajar bahasa korea", "mengedit foto untuk instagram", "mengedit video untuk tiktok", "mencatat ide-ide kreatif", "berkomunikasi dengan tim kerja", "memantau kesehatan dan olahraga", "berbelanja online kebutuhan bulanan", "pesan ojek online", "pesan taksi online", "streaming film indonesia", "streaming film barat", "main game mobile legends", "main game pubg", "mengatur jadwal harian", "mengatur jadwal mingguan", "mencari informasi lowongan kerja", "membaca berita terkini", "desain grafis", "presentasi", "coding", "menulis", "membuat musik", "menerjemahkan dokumen", "scan dokumen penting", "mengatur resep masakan", "membuat cv", "bikin portofolio", "belajar coding", "menggambar digital", "membuat animasi pendek", "mengelola sosial media", "riset pasar", "analisis data penjualan"]
    features = ["pencarian global", "ekspor data ke format csv", "ekspor data ke format excel", "template desain profesional", "mode gelap otomatis", "fitur kolaborasi tim real-time", "analitik performa konten", "backup otomatis ke google drive", "backup otomatis ke icloud", "filter ar lucu", "scan qr code pembayaran", "scan qr code undangan", "integrasi cloud dropbox", "integrasi cloud onedrive", "widget di homescreen android", "widget di homescreen ios", "notifikasi custom per kontak", "notifikasi custom per grup", "voice command google assistant", "voice command siri", "offline mode untuk artikel", "offline mode untuk peta", "multi-akun sosial media", "stabilisasi video", "auto-save", "history revisi", "smart cropping", "ai image generator", "ai text summarizer", "fitur text-to-speech", "fitur speech-to-text", "equalizer audio", "object removal tool", "background removal", "animasi teks", "transisi video", "color grading", "masking", "keyframe animation", "speed ramping", "reverse video", "template intro/outro", "pustaka musik bebas royalti"]
    emotions = ["kecewa berat", "senang banget", "sangat puas", "frustasi karena error", "bingung cara pakainya", "terkesan dengan fiturnya", "marah karena data hilang", "sedih tidak bisa dibuka", "lega masalah teratasi", "sangat terbantu", "kagum dengan developernya", "emosi jiwa", "sumpah kesel", "happy banget", "terharu bisa begini", "agak jengkel", "cukup senang", "biasa saja sih", "gregetan", "takjub", "kesal", "bete", "semangat", "optimis", "pesimis", "was-was"]
    negative_aspects = ["sering force close di hp xiaomi", "boros kuota telkomsel", "boros baterai iphone", "interface yang rumit dipelajari", "iklan video yang mengganggu", "fitur penting jadi premium", "fitur penting jadi berbayar", "respon lambat saat diklik", "susah login pakai akun google", "data tiba-tiba hilang", "tidak kompatibel dengan android 14", "hasil editan jadi pecah", "hasil editan jadi blur", "banyak bug aneh setelah update", "loadingnya lama banget", "makan ram banyak", "ui/ux nya bikin bingung", "sering not responding", "update malah nambah bug", "privasi data kurang terjamin", "tidak ada fitur undo", "proses ekspor gagal terus", "sinkronisasi sering macet", "watermark mengganggu", "pilihan ekspor terbatas", "tidak ada dukungan format tertentu", "terlalu banyak notifikasi", "memaksa rating bintang 5", "customer service tidak responsif", "fitur ai sering salah", "template monoton"]
    performance_aspects = ["waktu loading awal", "proses rendering video", "responsivitas antar muka", "stabilitas", "kecepatan download file", "kecepatan upload file", "konsumsi ram", "konsumsi memori internal", "konsumsi baterai", "kecepatan startup", "kelancaran animasi", "akurasi fitur ai", "kecepatan ekspor", "kecepatan impor", "penggunaan cpu", "kelancaran scrolling", "transisi antar layar"]
    improvement_suggestions = ["dioptimalkan lagi untuk hp kentang", "bugnya segera diperbaiki", "performa ditingkatkan", "opsi ekspor ditambah", "ui disederhanakan", "ux disederhanakan", "tampilannya dipercantik lagi", "dibuat lebih stabil dong", "ditambah fitur sinkronisasi antar device", "kurangi iklannya pliss", "jangan maksa update terus", "tambah opsi bahasa daerah", "perjelas tutorialnya", "respons cs ditingkatkan", "harga premium diturunkan", "tambah template baru", "perbaiki fitur x", "buat versi lite", "tambah integrasi y", "berikan opsi nonaktifkan notifikasi z"]
    positive_exclamations = ["mantap jiwa", "keren", "akhirnya nemu yang pas", "suka pokoknya", "keren dah", "best", "recommended lah", "bagus banget", "perfecto!", "juara!", "edan!", "ajib!", "top!", "the best!", "gokil!", "luar biasa!", "wow!"]
    positive_comments = ["yang saya cari selama ini", "berguna untuk kerjaan", "berguna untuk kuliah", "tidak mengecewakan sama sekali", "mempermudah hidup saya banget", "wajib install", "bakal langganan terus nih", "sesuai ekspektasi saya", "melebihi ekspektasi malah", "solusi yang mantap", "membuat pekerjaan lebih efisien", "tidak ada duanya", "sangat membantu produktivitas", "aplikasi andalan saya", "nggak nyesel bayar premium", "sangat berguna untuk hobi", "membuat konten jadi mudah"]
    design_adjectives = ["minimalis elegan", "modern dan segar", "menarik perhatian", "agak kuno", "agak jadul", "terlalu ramai", "terlalu penuh", "elegan profesional", "bersih dan rapi", "profesional look", "kurang menarik visualnya", "terlalu simpel", "terlalu kosong", "intuitif", "membingungkan", "enak dilihat", "sakit mata lihatnya", "konsisten", "user-friendly", "cluttered", "dated", "responsif", "estetik", "fungsional", "kreatif", "standar", "biasa"]
    design_comments = ["enak dilihat mata", "mudah dipahami alurnya", "perlu penyegaran desain", "agak membosankan tampilannya", "navigasinya sangat intuitif", "membingungkan letak menunya", "user-friendly banget", "susah nyari tombolnya", "warnanya pas", "fontnya enak dibaca", "perlu perbaikan di bagian navigasi", "ikonnya jelas", "animasinya halus", "layoutnya terstruktur", "perlu dirombak total", "terlalu banyak tombol"]
    version_number = ["1.2.3", "5.0.1", "2024.1", "3.5", "6.10", "7.0", "2.2.1", "terbaru", "kemarin", "beta", "alpha", "10.5.2", "versi 2023", "build 101", "v.8.8", "patch terbaru"]
    update_effects = ["jadi lebih cepat dan ringan", "muncul bug baru di fitur edit", "tampilannya berubah total, perlu adaptasi", "fitur filter tidak berfungsi lagi", "jauh lebih stabil sekarang", "makin berat di hp saya", "fitur sinkronisasi yang ditunggu akhirnya ditambahkan", "masalah lama akhirnya teratasi", "nggak ada perubahan signifikan", "malah jadi error", "baterai jadi lebih awet", "baterai jadi lebih boros", "beberapa fitur hilang", "ui jadi lebih fresh", "performa meningkat drastis", "ada fitur baru yang keren", "bug lama belum diperbaiki", "malah downgrade rasanya"]
    neutral_adjectives = ["lumayan lah", "oke aja", "standar sih", "biasa aja", "cukup memadai", "bolehlah dicoba", "ya gitu deh", "so-so", "tidak buruk", "cukup fungsional", "rata-rata", "cukup", "mayann"]
    minor_issues = ["iklannya kadang muncul tiba-tiba", "perlu koneksi internet indihome yang stabil", "beberapa fitur keren harus premium", "agak berat dibuka di samsung a series lama", "notifikasi whatsapp kadang telat masuk", "font teksnya kurang jelas terbaca", "loading gambar agak lama", "loading video agak lama", "ada typo dikit di menu", "tombol x nya kekecilan", "animasi kadang patah-patah", "perlu login ulang sesekali", "tema gelap kurang konsisten", "kadang suka force close", "ekspor kadang gagal", "sedikit lag pas scrolling", "perlu restart biar lancar lagi"]
    target_users = ["pekerja kantoran di jakarta", "mahasiswa ui", "mahasiswa ugm", "konten kreator tiktok", "konten kreator youtube", "ibu rumah tangga modern", "gamer kasual", "gamer pro", "pelajar sma", "pelajar smp", "freelancer desainer grafis", "freelancer penulis", "fotografer profesional", "musisi indie", "penulis blog", "penulis novel", "pedagang online di shopee", "pedagang online di tokopedia", "siapapun yang butuh edit cepat", "orang gaptek", "manajer proyek", "analis data", "guru", "dosen", "ukm", "startup", "fotografer pemula", "videografer", "editor lepas", "social media manager"]
    bug_types = ["bug tampilan di layar poni", "error saat menyimpan ke galeri", "force close tiba-tiba saat edit", "masalah login via facebook", "fitur filter tidak berfungsi", "typo di teks bahasa indonesia", "suara video hilang saat ekspor", "gambar thumbnail tidak muncul", "crash pas buka", "tombol nggak bisa diklik", "layar jadi hitam", "data corrupt", "bug sinkronisasi", "error kalkulasi", "masalah kompatibilitas", "bug undo/redo", "error impor file", "masalah rendering", "fitur x tidak jalan", "aplikasi freeze"]
    events = ["install ulang", "update os ke android 14", "update os ke ios 17", "membersihkan cache dan data", "restart hp samsung saya", "restart hp iphone saya", "ganti device ke baru", "login ulang akun", "update terakhir", "pertama kali install", "setelah menambahkan banyak data", "saat koneksi internet lambat", "pas buka file besar", "saat rendering video panjang", "setelah update aplikasi", "ketika multitasking"]
    requested_features = ["mode offline untuk semua fitur", "integrasi google calendar", "integrasi google tasks", "ekspor ke format pdf", "ekspor ke format docx", "widget homescreen yang interaktif", "tema kustom warna-warni", "dukungan bahasa sunda", "dukungan bahasa jawa", "fitur backup lokal ke sd card", "opsi font lebih banyak dan unik", "kontrol privasi data yang lebih detail", "fitur ai", "template lebih banyak lagi", "dukungan stylus pen", "versi web/desktop", "fitur kolaborasi yang lebih baik", "dukungan format heic", "fitur green screen", "auto caption bahasa indonesia", "integrasi cloud lain", "opsi aspect ratio lebih banyak", "fitur stabilisasi yang lebih canggih"]
    user_types = ["orang awam teknologi", "lansia gaptek", "anak-anak sd", "pemula baru coba", "profesional di bidangnya", "expert it", "emak-emak", "bapak-bapak", "generasi z", "milenial", "orang tua", "pelajar", "mahasiswa", "pekerja", "freelancer"]
    price_opinions = ["agak mahal untuk kantong mahasiswa", "harganya terjangkau banget", "sangat sepadan dengan fiturnya", "untungnya ada versi gratis", "terlalu mahal untuk fitur segitu", "ada opsi langganan tahunan lebih murah", "worth it lah harganya", "kemahalan sih menurutku", "harga bersaing dengan kompetitor", "gratis tapi banyak iklan", "harganya oke", "cukup pricey", "murah meriah", "sesuai budget"]
    value_propositions = ["fiturnya sangat lengkap dan powerful", "sangat membantu pekerjaan saya", "tidak ada alternatif gratis yang sebagus ini", "hemat waktu dan tenaga saya", "investasi yang bagus untuk produktivitas", "berguna banget buat sehari-hari", "sesuai dengan harganya", "memberikan nilai lebih", "solusi all-in-one", "kualitasnya premium", "hasilnya profesional", "mempermudah proses kreatif"]
    negative_experiences = ["lemot parah bikin emosi", "penuh iklan pop-up mengganggu", "susah dipakai, tidak user-friendly", "khawatir data pribadi tidak aman", "menipu, fitur tidak sesuai deskripsi", "tidak sebagus review di play store", "tidak sebagus review di app store", "bikin hp nge-hang", "buang-buang waktu installnya", "kehilangan data penting", "dipaksa upgrade ke premium", "hasilnya jelek", "prosesnya ribet", "bikin pusing kepala", "ngabisin kuota"]
    competing_app_type = ["editor foto", "editor video", "chatting", "platform e-commerce", "game moba", "ojek online", "software sejenis", "aplikasi produktivitas", "layanan streaming", "platform belajar online", "aplikasi catatan", "aplikasi desain", "aplikasi musik", "aplikasi berita"]
    competing_app_name = ["picsart", "snapseed", "whatsapp", "telegram", "shopee", "tokopedia", "mobile legends", "arena of valor", "gojek", "grab", "capcut", "vn editor", "canva", "instagram", "tiktok", "yang lain", "microsoft office", "google workspace", "netflix", "spotify", "coursera", "notion", "inshot", "lightroom", "premiere rush", "google keep", "figma", "adobe express"]
    positive_statements = ["poin plus utama program ini adalah", "hal yang saya suka dari software ini", "saya sangat mengapresiasi fitur ini", "yang bikin beda dari yang lain itu", "salut banget sama fitur ini", "fitur andalannya adalah", "nilai jual utamanya menurut saya", "kelebihannya ada di", "yang menonjol itu", "fitur favorit saya adalah"]
    specific_functions = ["fitur scan ktp yang akurat", "fitur scan npwp yang akurat", "konversi mata uang real-time saat belanja", "pengingat jadwal minum obat", "pemutar musik background saat buka app lain", "equalizer audio bawaan", "stabilisasi video anti goyang", "filter kecantikan ala korea", "template presentasi bisnis modern", "auto-caption", "voice changer", "object removal", "integrasi kalender", "fitur mind map", "analisis data otomatis", "fitur kolase foto", "pembuat slideshow", "efek green screen", "penghapus background", "fitur text-on-video"]
    difficulties = ["agak ribet pengaturannya", "bingung letak menunya", "sulit dipelajari fiturnya", "kurang intuitif alurnya", "perlu waktu adaptasi beberapa hari", "susah banget dipakainya", "gak ngerti sama sekali", "kurva belajarnya agak curam", "butuh tutorial tambahan", "membingungkan bagi pemula", "perlu eksperimen dulu", "tidak user-friendly"]
    notification_issues = ["sering telat masuk notifnya", "tidak muncul sama sekali notifikasinya", "terlalu banyak notif promosi", "notifikasi tidak relevan isinya", "sulit dimatikan notifikasi tertentu", "ganggu banget notifnya", "suara notifikasi tidak bisa diganti", "notif numpuk", "notif hilang sendiri", "setting notif reset terus"]
    general_positive_shorts = ["bagus pol", "ok banget", "mantap surantap", "sip markosip", "berguna sekali", "top markotop", "jos gandos", "keren abis", "mantul tenan", "suka!", "mantap!", "oke!", "ggwp", "mantap 👍", "bagus ✨", "keren 🔥", "luar biasa", "ajib", "ciamik", "puas"]
    general_negative_shorts = ["jelek banget", "error mulu", "lambat kayak keong", "payah", "kurang memuaskan", "ampas lah", "parah kacau", "nyesel install", "burik", "sampah", "hadeh", "jelek 👎", "error 😠", "lambat 🐌", "payah 🤦", "zonk", "parah", "kecewa", "buruk"]
    device_types = ["hp kentang ram 2gb", "xiaomi redmi note 10", "samsung galaxy s23 ultra", "iphone 11 jadul", "iphone 15 pro max terbaru", "oppo reno 8", "vivo v25", "realme c55", "tablet samsung tab s8", "ipad air 5", "laptop asus rog", "pc rakitan", "macbook pro m1", "google pixel 7", "low-end device", "mid-range phone", "flagship phone", "infinix note 30", "poco f5", "ipad mini 6", "laptop windows", "chromebook"]
    battery_usages = ["cukup irit baterai", "agak boros baterai kalau dipakai lama", "sangat menguras baterai hp", "konsumsi baterai normal saja", "lebih hemat baterai setelah update kemarin", "bikin batre cepet abis", "tidak terlalu berdampak pada baterai", "boros banget", "lumayan hemat", "standar lah"]
    size_opinions = ["ukurannya kecil", "ukurannya ringan", "ukuran standar zaman sekarang", "cukup besar ukurannya", "cukup berat ukurannya", "makan memori", "ukurannya wajar untuk fitur sebanyak ini", "gede banget filenya", "perlu storage lega", "ringan banget", "agak gede sih", "wajar"]
    effect_types = ["transisi video cinematic", "filter foto aesthetic", "animasi ui yang halus", "efek suara lucu", "efek suara keren", "stiker ar interaktif", "green screen", "slow motion", "efek glitch", "efek vintage", "color grading preset", "efek blur", "efek kartun", "animasi teks", "efek partikel", "overlay"]
    effect_qualities = ["efeknya halus dan profesional", "pilihan efeknya beragam dan unik", "kualitas efeknya standar saja", "terlihat kaku", "terlihat patah-patah", "efeknya terlihat murahan", "efeknya terlihat pasaran", "kualitasnya setara software pro", "mudah diaplikasikan", "butuh penyesuaian manual", "keren banget", "biasa aja", "kurang bagus", "mantap hasilnya"]
    achieved_goals = ["jadi lebih produktif kerja dari rumah", "menghemat waktu perjalanan ke kantor", "belajar hal baru tentang investasi saham", "tetap terorganisir jadwal meetingnya", "mendapatkan hiburan di waktu luang", "menyelesaikan tugas desain grafis", "meningkatkan skill editing video saya", "pekerjaan jadi cepat selesai", "bikin konten jadi gampang", "mengelola tugas tim lebih efektif", "memantau progres proyek lebih mudah", "membuat presentasi menarik", "menghasilkan karya yang bagus", "belajar skill baru"]
    overall_positive_opinion = ["software yang solid dan stabil", "ux nya seru", "secara keseluruhan sangat memuaskan", "hampir sempurna, tinggal poles dikit", "tidak ada keluhan berarti sejauh ini", "the best pokoknya", "sangat direkomendasikan", "pilihan yang tepat", "aplikasi yang bagus", "layak dicoba", "cukup impresif"]
    specific_complaint = ["fitur ekspor video masih sering error", "harga langganan premium naik lagi", "tidak ada dukungan untuk tablet huawei saya", "proses verifikasi akun lama sekali", "sinkronisasi antar hp android dan iphone bermasalah", "iklan terlalu banyak", "sering minta rating", "customer service susah dihubungi", "fitur x tidak berfungsi di device y", "tidak ada opsi backup lokal", "watermark tidak bisa dihilangkan (gratis)", "pilihan musik terbatas", "tidak support format file z", "sering crash saat menyimpan"]
    connection_dependency = ["harus selalu online pakai kuota", "harus selalu online pakai wifi", "bisa dipakai offline untuk fitur dasar", "butuh koneksi kencang untuk streaming", "butuh koneksi kencang untuk upload", "lemot kalau koneksi jelek", "fitur offline terbatas", "bisa offline sepenuhnya", "hybrid", "butuh koneksi stabil"]
    process_type = ["proses login", "proses autentikasi", "proses upload file besar", "proses rendering video 4k", "proses pembayaran via gopay", "proses pembayaran via ovo", "proses sinkronisasi data antar perangkat", "proses saving", "proses loading", "proses verifikasi email", "proses ekspor data", "proses impor template", "proses analisis", "proses kompresi"]
    process_speed = ["cepat sekali prosesnya", "agak lambat, perlu sabar", "sangat lama, bisa ditinggal ngopi", "tergantung kecepatan internet saya", "cepet banget", "lama banget buset", "instan", "butuh beberapa menit", "lumayan cepat", "standar", "terlalu lama"]
    support_quality = ["responsif dan sangat membantu solusinya", "lambat balasnya, nunggu berhari-hari", "jawabannya template bot, tidak membantu", "tidak menyelesaikan masalah saya", "adminnya ramah dan sabar", "dicuekin doang", "fast respon mantap", "solutif", "kurang informatif", "membantu tapi lama", "tidak ada support sama sekali", "sangat profesional"]
    support_channel = ["email", "live chat", "dm instagram", "dm twitter", "grup telegram komunitas", "form kontak di web", "telepon call center", "forum bantuan", "whatsapp", "facebook messenger", "komentar play store/app store"]
    tutorial_quality = ["tutorialnya jelas dan mudah diikuti pemula", "tutorialnya kurang lengkap untuk fitur advance", "tidak ada tutorial sama sekali", "videonya membingungkan dan terlalu cepat", "banyak tutorial di youtube", "gampang dipelajari tanpa tutorial", "dokumentasi lengkap", "faq sangat membantu", "tutorial interaktif", "contoh penggunaannya bagus", "kurang detail", "bahasanya teknis banget"]
    option_type = ["pilihan tema terang", "pilihan tema gelap", "pilihan bahasa indonesia", "pilihan bahasa inggris", "pilihan kualitas ekspor sd", "pilihan kualitas ekspor hd", "pilihan kualitas ekspor 4k", "pilihan metode pembayaran transfer bank", "pilihan metode pembayaran e-wallet", "layout", "font", "format tanggal", "satuan ukuran", "aspect ratio", "format output", "watermark style", "template kategori"]
    option_variety = ["opsinya banyak dan beragam", "pilihannya sedikit sekali", "cukup banyak variasinya", "kurang variatif, itu-itu saja", "lengkap banget pilihannya", "opsi kustomisasi terbatas", "sangat fleksibel", "cukup standar", "bisa lebih banyak lagi"]
    positive_action = ["menyimpan otomatis pekerjaan saya", "mengingatkan jadwal penting", "memberi rekomendasi konten yang relevan", "memperbaiki typo otomatis", "bekerja di background", "mengoptimalkan kualitas gambar otomatis", "memberikan saran cerdas", "membackup data secara rutin", "mempermudah navigasi", "memberikan shortcut berguna"]
    negative_action = ["crash tiba-tiba pas lagi asyik pakai", "logout sendiri dari akun", "menampilkan iklan judi online", "nge-freeze layarnya", "nutup sendiri", "restart paksa", "menghapus data tanpa konfirmasi", "mengubah pengaturan tanpa izin", "meminta izin aneh", "mengirim notifikasi spam", "membuat shortcut tanpa izin"]
    specific_use_case = ["edit video cinematic untuk prewedding", "membuat catatan rapat mingguan", "belajar kosakata bahasa jepang jlpt n5", "desain grafis cepat untuk postingan sosmed", "monitoring pengeluaran bulanan otomatis", "mencatat resep masakan", "bikin presentasi dadakan", "ngedit tugas sekolah", "membuat laporan keuangan", "mengelola inventaris toko online", "merencanakan perjalanan liburan", "bikin video tutorial", "membuat portofolio desain", "mengedit vlog harian", "membuat undangan digital"]
    free_version_limitations = ["ada watermark di hasil ekspor", "fitur dasar saja yang bisa dipakai", "dibatasi jumlah proyek", "dibatasi jumlah file", "iklan cukup banyak dan mengganggu", "tidak bisa akses template premium", "kualitas ekspor dibatasi ke sd", "tidak ada backup cloud", "harus online terus", "fitur kerennya bayar semua", "tidak ada support prioritas", "uji coba fitur terbatas waktu", "durasi video dibatasi", "tidak bisa pakai font custom", "pilihan efek terbatas"]
    ad_frequency = ["jarang banget muncul", "kadang-kadang saja muncul", "cukup sering muncul iklan video", "setiap beberapa klik muncul iklan banner", "hampir tidak ada iklan", "iklannya non-intrusif", "iklan muncul saat buka", "iklan muncul saat simpan hasil", "banyak banget iklannya", "iklan muncul di tengah penggunaan", "terlalu sering", "wajar untuk gratisan", "tidak ada iklan"]
    ad_relevance = ["iklannya relevan dengan minat saya", "iklan tidak relevan sama sekali", "iklan judi online", "iklan game online terus", "kadang relevan kadang tidak", "iklannya sopan dan bisa di-skip", "iklan produk shopee", "iklan produk lazada", "iklan aplikasi lain", "iklan pinjol mulu", "iklan yang menyesatkan", "iklan sesuai konteks", "iklan random"]
    update_frequency = ["sering dapat update tiap minggu", "sering dapat update tiap bulan", "jarang sekali update", "sudah lama tidak ada update sama sekali", "rutin update tiap bulan dengan fitur baru", "update terakhir memperbaiki banyak bug penting", "update cuma ganti versi, fitur sama aja", "developer rajin update", "update minor berkala", "update mayor setahun sekali", "terlalu sering update", "jarang banget", "update sesuai jadwal"]
    community_platform = ["facebook group", "forum kaskus", "grup telegram", "server discord", "subreddit", "forum developer", "komunitas di dalam aplikasi", "grup whatsapp", "forum online lain"]
    community_activity = ["aktif dan saling membantu antar anggota", "sepi banget, jarang ada postingan", "banyak diskusi menarik", "ada forum resminya tapi kurang aktif", "rame isinya master semua", "developer sering berinteraksi", "banyak tutorial dari anggota", "cukup aktif", "kurang responsif", "penuh spam"]
    location = ["depok", "jakarta selatan", "bandung", "surabaya", "medan", "bali", "yogyakarta", "semarang", "bogor", "bekasi", "tangerang", "malang", "makassar", "palembang", "jawa tengah", "jawa timur", "sumatera utara", "sulawesi selatan", "kalimantan timur"]
    signal_strength = ["sinyal telkomsel kuat", "sinyal xl kadang hilang", "pakai wifi indihome lancar", "sinyal indosat bagus", "koneksi stabil", "sinyal tri naik turun", "koneksi 5g ngebut", "sinyal jelek", "wifi lemot", "koneksi 4g lancar"]
    app_performance_location = ["tetap lancar", "agak lag kalau sinyal jelek", "loadingnya jadi lama", "nggak ngaruh ke performa", "fitur online tidak berfungsi", "berjalan normal", "sedikit terpengaruh", "sangat tergantung sinyal"]
    integrated_service = ["google drive", "dropbox", "slack", "kalender google", "spotify", "instagram api", "google photos", "microsoft onedrive", "zoom", "notion", "trello", "zapier", "google sheets", "google docs", "github", "figma", "adobe creative cloud"]
    security_opinion = ["terlihat cukup aman", "agak ragu soal privasi data", "semoga sudah terenkripsi", "perlu ditingkatkan keamanannya", "yakin aman sih", "was-was juga datanya", "ada autentikasi dua faktor", "kebijakan privasi jelas", "cukup meyakinkan", "perlu audit keamanan", "transparan soal data"]
    future_feature = ["integrasi ai untuk edit otomatis", "versi web", "versi desktop", "dukungan apple watch", "dukungan wear os", "fitur kolaborasi audio", "dukungan plugin eksternal", "api publik", "fitur analitik lebih dalam", "dukungan multi-bahasa lebih banyak", "template 3d", "fitur ar yang lebih canggih", "dukungan format video baru", "mode presentasi", "integrasi ai generatif"]
    comparison_point = ["lebih unggul dalam hal {positive_aspect}", "kalah dalam hal {negative_aspect}", "lebih mudah digunakan", "fiturnya lebih lengkap", "harganya lebih murah", "desainnya lebih menarik", "lebih stabil", "lebih ringan", "lebih intuitif", "kurang powerful", "lebih boros baterai"]
    learning_time = ["beberapa menit", "setengah jam", "beberapa jam", "satu hari", "beberapa hari", "seminggu", "sebentar", "cukup lama", "agak lama"]
    positive_outcome = ["jadi lebih efisien", "pekerjaan lebih cepat selesai", "hasilnya memuaskan", "bisa menguasai semua fiturnya", "sangat membantu", "jadi jago edit", "bisa bikin konten keren", "produktifitas meningkat"]
    positive_developer_action = ["mendengarkan masukan pengguna", "memperbaiki bug dengan cepat", "terus menambahkan fitur baru", "memberikan support yang baik", "membuat tutorial yang jelas", "aktif di komunitas", "transparan soal update", "responsif terhadap feedback"]
    intended_behavior = ["dihilangkan", "diubah fungsinya", "menjadi fitur premium", "membutuhkan izin tambahan", "bekerja seperti ini", "memang begitu cara kerjanya", "bukan bug"]
    other_activity = ["mengedit video kompleks", "mengelola proyek besar", "analisis data rumit", "membuat desain 3d", "animasi profesional", "coding aplikasi berat", "simulasi ilmiah", "produksi musik profesional"]
    rating_number = ["1", "2", "3", "4"]
    # --- Updated condition_for_change list (no inner placeholders, lowercase) ---
    condition_for_change = [
        "bug tampilan diperbaiki",
        "bug force close saat edit diperbaiki",
        "bug login facebook diperbaiki",
        "bug suara hilang saat ekspor diperbaiki",
        "bug crash pas buka diatasi",
        "fitur mode offline ditambahkan",
        "fitur ekspor ke pdf ditambahkan",
        "fitur tema kustom ditambahkan",
        "fitur backup lokal ditambahkan",
        "fitur kolaborasi yang lebih baik ditambahkan",
        "performa loading awal ditingkatkan",
        "performa rendering video ditingkatkan",
        "stabilitas aplikasi ditingkatkan",
        "konsumsi baterai dioptimalkan",
        "responsivitas antar muka ditingkatkan",
        "iklan dikurangi secara signifikan",
        "iklan video yang mengganggu dihilangkan",
        "harga premium diturunkan",
        "harga langganan lebih terjangkau",
        "masalah sering force close diatasi",
        "masalah boros kuota diatasi",
        "masalah interface yang rumit diperbaiki",
        "masalah data hilang diperbaiki",
        "masalah hasil editan pecah diatasi",
        "customer service lebih responsif",
        "cs bisa dihubungi lebih mudah",
        "update berikutnya lebih stabil",
        "update tidak menambah bug baru",
        "fitur filter berfungsi lagi",
        "fitur sinkronisasi antar perangkat berfungsi normal",
        "fitur penting tidak lagi premium",
        "watermark di versi gratis dihilangkan",
        "opsi ekspor lebih banyak",
        "kompatibilitas dengan android terbaru diperbaiki",
        "kompatibilitas dengan ios terbaru diperbaiki",
    ]

    generated_count = 0
    existing_reviews = set()
    while generated_count < count:
        template = random.choice(templates)
        try:
            replacements = {
                'adjective': random.choice(adjectives),
                'positive_aspect': random.choice(positive_aspects),
                'verb': random.choice(verbs),
                'activity': random.choice(activities),
                'feature': random.choice(features),
                'emotion': random.choice(emotions),
                'negative_aspect': random.choice(negative_aspects),
                'performance_aspect': random.choice(performance_aspects),
                'improvement_suggestion': random.choice(improvement_suggestions),
                'positive_exclamation': random.choice(positive_exclamations),
                'positive_comment': random.choice(positive_comments),
                'design_adjective': random.choice(design_adjectives),
                'design_comment': random.choice(design_comments),
                'version_number': random.choice(version_number),
                'update_effect': random.choice(update_effects),
                'neutral_adjective': random.choice(neutral_adjectives),
                'minor_issue': random.choice(minor_issues),
                'target_user': random.choice(target_users),
                'bug_type': random.choice(bug_types),
                'event': random.choice(events),
                'requested_feature': random.choice(requested_features),
                'user_type': random.choice(user_types),
                'price_opinion': random.choice(price_opinions),
                'value_proposition': random.choice(value_propositions),
                'negative_experience': random.choice(negative_experiences),
                'competing_app_type': random.choice(competing_app_type),
                'competing_app_name': random.choice(competing_app_name),
                'positive_statement': random.choice(positive_statements),
                'specific_function': random.choice(specific_functions),
                'difficulty': random.choice(difficulties),
                'notification_issue': random.choice(notification_issues),
                'general_positive_short': random.choice(general_positive_shorts),
                'general_negative_short': random.choice(general_negative_shorts),
                'device_type': random.choice(device_types),
                'battery_usage': random.choice(battery_usages),
                'size_opinion': random.choice(size_opinions),
                'effect_type': random.choice(effect_types),
                'effect_quality': random.choice(effect_qualities),
                'achieved_goal': random.choice(achieved_goals),
                'overall_positive_opinion': random.choice(overall_positive_opinion),
                'specific_complaint': random.choice(specific_complaint),
                'connection_dependency': random.choice(connection_dependency),
                'process_type': random.choice(process_type),
                'process_speed': random.choice(process_speed),
                'support_quality': random.choice(support_quality),
                'support_channel': random.choice(support_channel),
                'tutorial_quality': random.choice(tutorial_quality),
                'option_type': random.choice(option_type),
                'option_variety': random.choice(option_variety),
                'positive_action': random.choice(positive_action),
                'negative_action': random.choice(negative_action),
                'specific_use_case': random.choice(specific_use_case),
                'free_version_limitations': random.choice(free_version_limitations),
                'ad_frequency': random.choice(ad_frequency),
                'ad_relevance': random.choice(ad_relevance),
                'update_frequency': random.choice(update_frequency),
                'community_platform': random.choice(community_platform),
                'community_activity': random.choice(community_activity),
                'location': random.choice(location),
                'signal_strength': random.choice(signal_strength),
                'app_performance_location': random.choice(app_performance_location),
                'integrated_service': random.choice(integrated_service),
                'security_opinion': random.choice(security_opinion),
                'future_feature': random.choice(future_feature),
                'comparison_point': random.choice(comparison_point), # Added
                'learning_time': random.choice(learning_time),       # Added
                'positive_outcome': random.choice(positive_outcome),   # Added
                'positive_developer_action': random.choice(positive_developer_action), # Added
                'intended_behavior': random.choice(intended_behavior), # Added
                'other_activity': random.choice(other_activity),     # Added
                'rating_number': random.choice(rating_number),       # Added
                'condition_for_change': random.choice(condition_for_change), # Added
            }
            # Filter replacements needed for the current template
            valid_replacements = {k: v for k, v in replacements.items() if f"{{{k}}}" in template}
            review = template
            processed_keys = set() # Keep track of keys processed to handle multiple occurrences
            for k, v in valid_replacements.items():
                 if k not in processed_keys:
                     # Replace all occurrences of the placeholder for this key
                     review = review.replace(f"{{{k}}}", v)
                     processed_keys.add(k)

            review = review.strip()

            # Add punctuation if missing
            if review and not review.endswith(('.', '!', '?')):
                 # Add question mark for question templates, otherwise period
                 if any(q_word in template for q_word in ["apakah ada rencana", "apakah {feature} ini", "kenapa ya fitur", "apakah {feature} ini memang"]):
                     review += '?'
                 # else:
                 #    review += '.' # Removed adding period automatically to allow more natural endings

            # Ensure review is meaningful and not already generated
            if review and len(review) > 5 and review not in existing_reviews: # Adjusted min length slightly
                reviews.append((review, 0)) # Label 0 for genuine
                existing_reviews.add(review)
                generated_count += 1
        except KeyError as e:
            # print(f"Warning: KeyError {e} in template: '{template}' with replacements {valid_replacements}")
            pass
        except Exception as e:
            # print(f"Error generating genuine review with template '{template}': {e}")
            pass

    return reviews


def generate_irrelevant_content(count):
    """Generates varied irrelevant content (Label 1) with real examples."""
    contents = []
    # --- MODIFIED & ADDED TEMPLATES (Increased Variety & Lowercase) ---
    templates = [
        # Original templates modified/kept/expanded & lowercased
        "ada yang tahu cara {action} di {unrelated_app_name}?",
        "kenapa {feature} di {related_app_name} tidak {expected_behavior} ya? beda sama {competitor_app_name}",
        "dibanding {competitor_app_name}, software ini {comparison_opinion}",
        "saya pakai {related_app_name} dari developer {developer_name}, {opinion_on_related_app}",
        "developer {developer_name} {developer_origin} memang {developer_reputation}",
        "balasan untuk @{username}: {response_to_user}. coba cek di {relevant_setting_location}",
        "gimana cara {task} ya? mohon bantuannya suhu",
        "apakah pinjol {specific_pinjol_app} ini aman dan terdaftar ojk?",
        "lebih suka pakai {alternative_app_name} karena {reason}",
        "ada rekomendasi lain untuk {purpose} selain ini?",
        "kok {issue} ya setelah update {operating_system} di hp {device_brand} saya?",
        "semoga {wish_or_hope}. aamiin",
        "setuju banget sama review @{other_username} tentang {topic}",
        "ini developernya yang bikin game {famous_app} itu bukan sih?",
        "customer servicenya {contact_experience}, ada nomor whatsapp resmi ga?",
        "hp saya {phone_spec}, kira-kira kuat ga ya buat main {specific_game} setting rata kanan?",
        "dulu pernah pakai {old_app_version}, {past_experience}. sekarang udah beda jauh",
        "kenapa harus bayar untuk {action_requiring_payment} sih? mending pakai {free_alternative} aja",
        "bagaimana cara mengganti {setting} di hp {device_brand}?",
        "saya fans berat {brand_name}, tapi program ini {app_specific_criticism}",
        "ulasan saya tentang {other_topic} di google maps kok hilang ya?",
        "ada yang punya tips & trik buat {unrelated_activity} di {place_or_platform}?",
        "ini tampilannya mirip banget sama {similar_app_name}",
        "tolong dong, {request_to_developer_general} di update berikutnya. penting nih!", # can be relevant but often used irrelevantly
        "lagi cari info tentang {news_topic} yang lagi viral",
        "ada yang jual {item_for_sale} daerah {location}?",
        "kode referral {service_name} saya: {referral_code}. lumayan dapet bonus cashback", # borderline spam/irrelevant
        "kode referral {service_name} saya: {referral_code}. lumayan dapet bonus poin", # borderline spam/irrelevant
        "baru nonton film {movie_title} di bioskop {cinema_name}, unik ceritanya",
        "ada lowongan kerja di bidang {job_field} di daerah {location}?",
        "selamat {greeting} semuanya!",
        "besok {event_happening} di {event_location}",
        "lagi dengerin lagu {song_title} - {artist_name} di spotify",
        "lagi dengerin lagu {song_title} - {artist_name} di joox",
        "ada yang tahu tempat {place_recommendation_request} yang enak dan murah di {location}?",
        "saya pengguna baru, salam kenal semua",
        "pertamax gan!",
        "izin share info ya admin, {shared_info}",
        "komen biar rame aja",
        "nyimak dulu",
        "info loker dong",
        "apa sih maksudnya?",
        "apalah",
        "hmm",
        "hoam",
        "malas",
        "hahahahahahahahaha",
        "wkwkwkwkwkwk"
        "hhhhhhh",
        "hhh",
        "wkwk",
        "xixixi",
        "xixi",
        "iyakah"
        "masa sih"
        "gatau ah males pengen jajan",
        "ada yang dari {community_or_group}?",
        "resep {food_name} dong",
        "harga {item_name} berapaan ya sekarang?",
        "jalanan {street_name} macet parah!",
        "ini ulasan ke-{review_number}", # meta comment about reviewing
        "ini gimana sih makenya?", # testing comment function
        "kok sepi ya?", # observation about comment section
        "ada yang online jam segini?", # checking for active users
        "saya kasih bintang {rating_number} biar developernya {developer_motivation}", # comment about rating motivation (often irrelevant)
        "ini software buatan {developer_origin} ya?", # question about origin
        "kenapa namanya {app_name_question}?", # question about app name
        "lagi butuh {unrelated_need}.", # personal need statement
        "curhat dikit ya, {personal_story}", # sharing personal story
        "ada yang ngalamin {shared_experience} juga?", # seeking shared experience (often unrelated)
        "menurut {person_opinion}, {statement_about_topic}", # quoting someone else
        "kalau di {other_platform}, fiturnya {feature_comparison}", # comparison with another platform
        "saya lebih suka {preference} daripada {alternative_preference}", # general preference statement
        "mending {suggestion} aja daripada {alternative_suggestion}", # unrelated suggestion
        "ini {misinformation_claim}", # spreading misinformation (can be irrelevant)
        "politik sekarang {political_comment}", # political comment
        "tim bola favorit saya {sports_team} {sports_result}", # sports comment
        "lagi nonton {tv_show} di {tv_channel}", # tv show comment
        "pesan saya untuk developer: {message_to_developer}", # general message, often irrelevant to specific features/bugs
        "hanya ingin mengucapkan {short_greeting}", # simple greeting
        "apakah ini {app_category} terbaik?", # general question, often rhetorical/irrelevant
        "ada yang tahu cara {action} di aplikasi lain?",  # repositioned from question section
        "baru nonton film {movie_title} di bioskop, seru juga",
        "ada rekomendasi tempat makan enak di {location}?",
        "ada yang punya tips & trik buat {unrelated_activity}?",
        "ini fungsinya buat apa?",

        # --- ADDED: More Irrelevant Templates (Lowercase) ---
        "tes komen doang",
        "halo {location}!",
        "ada yang pakai hp {device_brand} juga?",
        "lagi promo apa nih?",
        "iklan terus isinya", # complaint about ads, but not specific to the app's function
        "sundul gan",
        "jejak digital",
        "nunggu review dari suhu {username}",
        "ini aplikasi mirip {similar_app_name} ya?",
        "kok ratingnya bisa tinggi?", # questioning rating, not reviewing
        "ada grup wa/tele nya ga?",
        "developer {developer_name} emang {developer_reputation}",
        "lagi belajar {unrelated_skill}, ada rekomendasi?",
        "cuaca {weather_comment}, enaknya {personal_activity}",
        "info dong, {random_question}?",
        "saya dari {community_or_group}, ada yang sama?",
        "harga {item_name} lagi naik ya?",
        "{news_topic} lagi rame dibahas",
        "kalau mau {task} pakai apa ya bagusnya?",
        "balesan buat {other_username}: {response_to_user}",
        "pinjol {specific_pinjol_app} itu gimana sih?",
        "lebih enak {alternative_app_name} sih menurutku",
        "buat {purpose}, ada saran lain?",
        "hp {device_brand} saya {issue} nih",
        "semoga {wish_or_hope}",
        "cs nya {contact_experience}",
        "hp {phone_spec} kuat main {specific_game}?",
        "dulu {old_app_version} {past_experience}",
        "bayar buat {action_requiring_payment}? mending {free_alternative}",
        "ganti {setting} di {device_brand} gimana?",
        "fans {brand_name} tapi app ini {app_specific_criticism}",
        "review google maps saya soal {other_topic} hilang",
        "tips {unrelated_activity} di {place_or_platform}?",
        "mirip {similar_app_name}",
        "request {request_to_developer_general}",
        "jual {item_for_sale} di {location}",
        "kode referral {service_name}: {referral_code}",
        "nonton {movie_title} di {cinema_name}",
        "loker {job_field} di {location}?",
        "selamat {greeting}",
        "besok ada {event_happening} di {event_location}",
        "dengerin {song_title} - {artist_name}",
        "rekomendasi {place_recommendation_request} di {location}?",
        "salam kenal",
        "share info: {shared_info}",
        "resep {food_name}?",
        "jalan {street_name} macet",
        "ulasan ke-{review_number}",
        "gimana makenya?",
        "sepi amat",
        "ada yg online?",
        "bintang {rating_number} biar {developer_motivation}",
        "buatan {developer_origin}?",
        "kenapa namanya {app_name_question}?",
        "butuh {unrelated_need}",
        "curhat: {personal_story}",
        "ada yg ngalamin {shared_experience}?",
        "kata {person_opinion}, {statement_about_topic}",
        "di {other_platform} fiturnya {feature_comparison}",
        "lebih suka {preference} daripada {alternative_preference}",
        "mending {suggestion} daripada {alternative_suggestion}",
        "ini {misinformation_claim}",
        "politik {political_comment}",
        "{sports_team} {sports_result}",
        "nonton {tv_show} di {tv_channel}",
        "pesan buat dev: {message_to_developer}",
        "ucapin {short_greeting}",
        "ini {app_category} terbaik?",
        "ada yang bisa bantu {task}?",
        "lagi cari {item_for_sale}",
        "kode {service_name} {referral_code}",
        "film {movie_title} bagus ga?",
        "lowongan {job_field} dong",
        "tempat {place_recommendation_request} dimana ya?",
        "info {shared_info} dong",
        "harga {item_name} berapa?",
        "jalan {street_name} arah mana?",
        "ada dari {community_or_group}?",
        "resep {food_name} yang gampang?",
        "butuh {unrelated_need} nih",
        "curhat dong: {personal_story}",
        "siapa yg ngalamin {shared_experience}?",
        "kalau {person_opinion} bilang {statement_about_topic}",
        "di {other_platform} bisa {feature_comparison}",
        "mending {suggestion} atau {alternative_suggestion}?",
        "jangan percaya {misinformation_claim}",
        "bola semalam {sports_team} {sports_result}",
        "acara {tv_show} di {tv_channel} seru",
        "buat developer: {message_to_developer}",
        "sekedar {short_greeting}",
        "ini masuk kategori {app_category} apa?",
    ]

    # --- Expanded Lists (More Variety, Real Examples, Lowercase) ---
    # (All keywords converted to lowercase)
    rating_number = ["1", "2", "3", "4"] # Keep as is, used in genuine too
    actions = ["mengaktifkan mode gelap", "menghapus akun permanen", "mengubah bahasa ke inggris", "backup chat whatsapp ke google drive", "menambahkan teman via nomor hp", "scan qr code pedulilindungi", "bayar tagihan listrik pln", "cek saldo e-money mandiri", "cek saldo e-money bca", "nonaktifkan notifikasi game mobile legends", "ganti foto profil instagram", "unfollow akun", "posting story", "cek resi jne", "cek resi j&t", "mengganti nada dering", "menghubungkan ke printer wifi", "transfer pulsa", "beli token listrik", "cek kuota internet", "update status facebook", "kirim dm twitter", "upload video youtube", "join grup telegram"]
    unrelated_app_names = ["tiktok", "instagram", "whatsapp", "mobile legends", "genshin impact", "shopee", "gojek", "mypertamina", "pedulilindungi", "zoom", "spotify", "netflix", "traveloka", "dana", "ovo", "google maps", "facebook", "twitter", "x", "capcut", "telegram", "pinterest", "linkedin", "discord", "steam", "garena free fire", "youtube", "gmail", "google chrome", "microsoft word", "excel", "photoshop"]
    features = ["notifikasi chat", "fitur story", "fitur reels", "tombol 'like'", "tombol 'suka'", "login via akun google", "login via akun facebook", "filter 'doggy' di ig", "pembayaran pakai qris", "top-up saldo gopay", "top-up saldo ovo", "fitur dark mode", "upload foto", "upload video", "fitur live streaming", "centang biru", "algoritma fyp", "keranjang kuning tiktok", "shopeepaylater", "gopaylater", "fitur explore instagram", "trending topic twitter", "google discover feed"]
    related_app_names = ["gopartner", "clash royale", "instagram lite", "whatsapp business", "capcut pro", "spotify premium", "versi beta ini", "youtube music", "facebook lite", "twitter blue", "aplikasi ini versi lama", "aplikasi ini versi pro", "gbwhatsapp", "youtube vanced", "aplikasi sejenis lainnya"]
    expected_behaviors = ["muncul tepat waktu", "berfungsi normal", "bisa diklik", "bisa ditap", "tersimpan otomatis di galeri", "bisa di-scan pakai kamera", "terhubung ke server dengan lancar", "tidak force close", "loading cepat", "tidak lemot", "akurat", "bisa dibuka", "tidak error", "sesuai petunjuk", "muncul di notifikasi"]
    competitor_app_names = ["gopay", "ovo", "dana", "shopeepay", "linkaja", "capcut", "vn editor", "inshot", "picsart", "snapseed", "tokopedia", "lazada", "blibli", "grab", "maxim", "indodax", "bibit", "ajaib", "flip", "dana", "jenius", "notion", "evernote", "asana", "trello", "zoom", "google meet", "canva", "figma", "lightroom", "premiere rush", "final cut pro", "google keep", "microsoft onenote"]
    comparison_opinions = ["kalah jauh fiturnya", "lebih simpel ui-nya", "agak ribet pakainya", "fiturnya mirip tapi yang ini gratis", "lebih mahal langganannya", "lebih stabil jarang nge-bug", "lebih ringan di hp saya", "lebih banyak iklannya", "lebih intuitif navigasinya", "kurang lengkap opsinya", "sama aja bohong", "mendingan yang ono", "lebih powerful", "kurang user-friendly"]
    developer_names = ["gojek indonesia", "sea group", "meta", "google llc", "bytedance", "supercell", "moonton", "mihoyo", "hoyoverse", "telkom indonesia", "bank mandiri", "bca", "kominfo", "microsoft", "apple", "netflix inc.", "pt kereta api indonesia", "pln", "kemenkes", "tencent", "adobe"]
    developer_origins = ["indonesia", "singapura", "amerika serikat", "china", "finlandia", "korea selatan", "jepang", "swedia", "kanada", "eropa", "asia", "lokal", "luar negeri"]
    opinions_on_related_app = ["jauh lebih bagus", "sering error juga sama aja", "lebih stabil yang itu", "fiturnya beda jauh ternyata", "sama aja sih intinya", "kurang lebih mirip fungsinya", "yang itu lebih sering update", "lebih ringan", "lebih lengkap", "lebih mahal"]
    developer_reputations = ["terkenal inovatif", "responnya cepat kalau ada bug", "jarang update", "sering bikin software bagus", "sering bikin game bagus", "peduli feedback pengguna", "agak lambat perbaikannya kalau ada masalah", "sering akuisisi startup", "kontroversial", "dikenal handal", "developernya baik", "kurang responsif", "sering bikin aplikasi aneh"]
    usernames = ["penggunasetia123", "dewicantik_88", "budisantoso_real", "gamerproindo", "admintokoabc", "randomuser777", "pecintakucingdepok", "anakui_hits", "rinasusanti", "ahmad_maulana", "userxyz", "anonim007", "masterreviewer", "akusiapa", "orangbiasa", "tukangreview", "pembelajar", "netizen62"]
    response_to_user = ["coba cek di pengaturan notifikasi hp-nya", "saya juga ngalamin itu di hp samsung saya", "itu bug kayaknya, laporin aja ke developernya via email", "coba restart hp atau clear cache dulu", "mungkin servernya lagi down", "mungkin servernya lagi maintenance", "pastikan udah versi terbaru di play store", "pastikan udah versi terbaru di app store", "bisa jadi masalah jaringan internet kamu", "coba tanya di grup komunitasnya", "sama bro/sis", "googling aja coba", "cek youtube tutorialnya", "bukan urusan saya hehe"]
    relevant_setting_location = ["pengaturan sistem", "setting notifikasi sistem", "menu profil", "bagian bantuan", "bagian faq", "forum pengguna", "website resmi developer", "pengaturan aplikasi", "pusat bantuan", "komunitas facebook", "grup telegram"]
    tasks = ["export chat ke pdf", "import kontak dari file vcf", "share lokasi real-time ke whatsapp", "atur pengingat minum obat harian", "scan barcode produk di indomaret", "cek ongkir jne ke bandung", "cek ongkir j&t ke bandung", "cari resep rendang padang asli", "mencari lirik lagu", "konversi video ke mp3", "membuat playlist spotify", "belajar main gitar", "download film", "streaming bola", "cari kerjaan", "edit foto jadi anime"]
    specific_pinjol_app = ["adakami", "kredivo", "akulaku", "easycash", "julo", "kredit pintar", "pinjol ilegal yang sering sms itu", "spinjam", "findaya", "rupiah cepat", "indodana", "pinjol a", "pinjol b", "yang nawarin di wa itu"]
    alternative_app_name = ["software open source seperti krita", "software open source seperti gimp", "libreoffice", "canva", "telegram", "signal", "program sebelah", "bawaan hp", "google keep", "microsoft onenote", "aplikasi x", "aplikasi y", "yang gratisan aja"]
    reasons = ["lebih ringan di hp kentang saya", "gratis tanpa iklan sama sekali", "tampilannya lebih modern dan enak dilihat", "lebih lengkap fiturnya untuk edit video tiktok", "lebih aman privasi datanya katanya", "komunitas penggunanya lebih aktif dan membantu", "sudah terbiasa pakai itu", "lebih simpel dan to the point", "lebih murah", "lebih stabil", "nggak ribet"]
    purposes = ["edit video cepat untuk reels", "edit video cepat untuk shorts", "belajar investasi saham pemula", "cari resep masakan sunda", "atur jadwal tim proyek pakai trello", "atur jadwal tim proyek pakai asana", "monitoring harga bitcoin", "monitoring harga ethereum", "pesan tiket kereta api kai access", "cari teman mabar valorant", "mencari rekomendasi film", "belajar bahasa pemrograman python", "bikin cv online", "desain poster", "catatan kuliah", "ngatur keuangan"]
    issues = ["nggak bisa dibuka sama sekali", "force close terus", "lemot parah loadingnya lama banget", "minta update terus padahal udah terbaru", "keluar sendiri pas lagi asyik edit video", "nggak bisa login pakai akun google", "nggak bisa login pakai akun facebook", "kamera jadi error setelah install", "pembayaran gagal terus pakai qris", "notifikasi tidak muncul", "layar jadi putih/hitam", "baterai boros", "data hilang", "error koneksi", "tidak kompatibel"]
    operating_system = ["android 13", "android 14", "ios 16", "ios 17", "miui 14", "windows 11", "coloros 13", "one ui 6", "macos sonoma", "linux ubuntu", "harmonyos", "os terbaru", "os lama", "windows 10", "android 12"]
    device_brand = ["xiaomi", "samsung", "iphone", "oppo", "realme", "vivo", "infinix", "asus rog", "poco", "huawei", "google pixel", "motorola", "nokia", "sony xperia", "advan", "evercoss", "laptop asus", "laptop lenovo", "macbook"]
    weather_comments = ["panas banget", "hujan deras dari pagi", "mendung terus bikin mager", "cuacanya lagi cerah bagus", "gerah banget malam ini", "anginnya kenceng", "adem ayem", "dingin", "berawan", "biasa aja"]
    location = ["depok", "jakarta", "bekasi", "bogor", "tangerang", "bandung", "yogyakarta", "surabaya", "medan", "makassar", "bali", "semarang", "malang", "di kantor", "di rumah", "di kampus", "jawa barat", "jawa tengah", "jawa timur", "sumatera", "kalimantan", "sulawesi", "papua"]
    personal_activities = ["males ngapa-ngapain di rumah", "enak buat tidur siang", "bawaannya pengen ngemil seblak", "bawaannya pengen ngemil bakso", "lagi ngerjain tugas kuliah", "lagi ngerjain skripsi", "pengen liburan ke puncak", "pengen liburan ke anyer", "lagi wfh", "mau nonton bioskop xxi", "mau nonton bioskop cgv", "lagi main game", "lagi scroll tiktok", "pengen makan mie ayam", "mau jogging sore", "lagi kerja", "santai aja"]
    wishes_or_hopes = ["besok libur tanggal merah", "harga bitcoin tembus 1 miliar", "dia cepet bales chat whatsapp", "pandemi covid benar-benar berakhir", "timnas indonesia juara piala asia", "dapet kerjaan baru yang gajinya umr depok", "semoga lancar presentasi besok", "mudah-mudahan jalan margonda nggak macet", "semoga developernya baca ini", "berharap fiturnya gratis", "semoga menang undian", "mudah-mudahan sehat selalu", "semoga sukses"]
    topics = ["iklan yang tiba-tiba muncul full screen", "bug force close pas mau simpan", "harga langganan premium yang mahal", "fitur baru yang aneh dan nggak berguna", "kebijakan privasi yang membingungkan", "perbandingan dengan kompetitor", "update terbaru bikin boros baterai", "layanan pelanggan yang susah dihubungi", "masalah login", "kualitas ekspor", "isu keamanan data", "fitur yang dihapus", "performa aplikasi"]
    famous_app = ["instagram", "tiktok", "whatsapp", "youtube", "facebook", "twitter", "spotify", "netflix", "snapchat", "telegram", "zoom", "google maps", "gmail", "gojek", "grab", "shopee", "tokopedia", "mobile legends", "free fire", "genshin impact"]
    contact_experience = ["email nggak dibales-bales udah seminggu", "telepon cs sibuk terus", "live chatnya dijawab bot template terus", "susah banget cari kontak developernya", "dm instagram cuma di-read doang", "dm twitter cuma di-read doang", "responnya cepat tapi nggak ngasih solusi", "tidak ada opsi kontak sama sekali", "ramah tapi lambat", "jutek banget cs nya", "sangat membantu", "tidak profesional"]
    phone_spec = ["ram 3gb", "rom 32gb", "chipset snapdragon 660", "memori internal hampir penuh", "layar retak seribu", "baterai udah bocor parah", "iphone xr 64gb", "samsung a52s 5g", "hp kentang", "spek dewa", "flagship killer", "ram 4gb", "mediatek helio g85", "hp jadul", "baru beli kemarin"]
    specific_game = ["genshin impact", "pubg mobile", "call of duty mobile", "honkai star rail", "efootball 2024", "game aaa di pc", "cyberpunk 2077", "game berat lainnya", "game online kompetitif", "mobile legends", "free fire", "valorant", "dota 2", "stumble guys"]
    old_app_version = ["versi 2.0 dulu", "sebelum update besar kemarin", "pas awal rilis tahun 2020", "versi tahun lalu", "versi lama sebelum ui berubah", "versi beta", "versi alpha", "sebelum ganti nama", "pas masih gratis"]
    past_experiences = ["dulu bagus banget, sekarang banyak iklan", "lebih ringan dan simpel ui-nya dulu", "fiturnya lebih lengkap dulu, sekarang malah dikurangi", "fiturnya lebih lengkap dulu, sekarang malah dihilangkan", "dulu gratis semua fitur, sekarang banyak yang bayar", "dulu lebih stabil", "nggak banyak berubah", "makin bagus sekarang"]
    action_requiring_payment = ["download hasil edit tanpa watermark", "hapus watermark video", "pakai filter premium", "pakai efek premium", "akses semua template desain", "simpan lebih dari 3 proyek", "fitur kolaborasi tim", "unlock semua level game", "menyimpan dalam kualitas tinggi", "menggunakan fitur ai canggih", "backup cloud", "ekspor format tertentu", "menghilangkan iklan"]
    free_alternative = ["capcut", "vn video editor", "gimp", "canva versi gratis", "google docs", "google sheets", "google slides", "galeri bawaan hp", "editor foto bawaan hp", "aplikasi open source", "versi gratisnya", "aplikasi x gratis", "cari yg crack aja"]
    settings = ["profil whatsapp", "notifikasi instagram", "tema keyboard gboard", "tema keyboard swiftkey", "akun google yang tertaut di hp", "bahasa sistem hp", "pengaturan privasi lokasi", "izin kamera", "izin mikrofon", "pengaturan apn internet", "mode pesawat", "wallpaper hp", "nada dering telepon", "akun email"]
    brand_name = ["google", "meta", "facebook", "apple", "samsung", "microsoft", "netflix", "disney+", "xiaomi", "sony", "nintendo", "adobe", "amazon", "gojek", "tokopedia", "unilever", "indofood"]
    app_specific_criticism = ["kurang polish dibanding produk google lainnya", "terasa ketinggalan zaman ui-nya", "terasa ketinggalan zaman ux-nya", "tidak sesuai ekspektasi saya sebagai fans apple", "banyak bloatware bawaan hp samsung", "servernya sering down", "servernya sering maintenance", "kurang inovatif fiturnya", "tidak seintuitif produk adobe lain", "terlalu banyak fitur nggak penting", "monopoli pasar", "harganya kemahalan"]
    other_topic = ["resep nasi goreng viral", "review film horor siksa kubur", "tips hemat kuota telkomsel", "berita bola liga inggris", "jadwal konser coldplay jakarta", "harga tiket konser ed sheeran", "isu politik terbaru", "gosip artis kpop", "harga sembako", "promo supermarket", "liburan murah", "cara investasi"]
    unrelated_activity = ["main gitar kunci dasar", "masak rendang pakai bumbu instan", "trading saham bbca", "trading saham bbri", "belajar bahasa jepang otodidak", "benerin motor vario di bengkel", "nonton anime one piece terbaru", "cari kosan murah di depok", "streaming bola", "ikut webinar online", "olahraga pagi", "membersihkan rumah", "belajar makeup", "menjahit"]
    place_or_platform = ["youtube", "tiktok", "instagram", "di rumah", "di kampus", "di kantor", "facebook", "twitter", "linkedin", "kaskus", "reddit", "quora", "brainly", "di grup wa", "di forum online"]
    similar_app_name = ["edit video capcut", "edit video vn", "desain online canva", "sosial media instagram", "sosial media tiktok", "game moba arena of valor", "game moba lol wild rift", "notion", "evernote", "whatsapp", "telegram", "aplikasi x", "aplikasi y", "yang itu tuh"]
    request_to_developer_general = ["perbaiki bug login google", "tambah fitur dark mode universal", "optimalkan performa di hp ram kecil", "tolong respon keluhan pengguna di play store", "jangan kebanyakan iklan!", "turunin harga premiumnya dong", "adain promo dong", "semangat terus developernya!", "tolong perbaiki bug x", "tambah fitur y", "buat lebih ringan"]
    news_topic = ["harga bbm pertamina naik", "hasil pemilu 2024", "kasus korupsi terbaru", "perang rusia-ukraina terkini", "isu resesi global", "kebijakan pemerintah tentang tapera", "gempa bumi terkini", "update kasus viral", "berita artis cerai", "olimpiade paris", "harga emas hari ini"]
    item_for_sale = ["akun mobile legends mythic murah", "voucher game google play diskon", "hp second iphone 11", "jasa joki tugas kuliah", "laptop bekas lenovo thinkpad", "baju preloved murah", "baju thrift murah", "pulsa transfer", "token listrik murah", "makanan ringan", "aksesoris hp", "buku bekas"]
    service_name = ["gojek", "shopee", "tokopedia", "dana", "ovo", "grab", "netflix", "spotify", "bibit", "ajaib", "bca mobile", "brimo", "mandiri livin'", "facebook", "instagram", "google", "apple id", "akulaku", "kredivo", "mytelkomsel", "myxl", "pln mobile", "kai access"]
    referral_code = ["gojekhemat", "shopeeuntung", "tokopediaku", "danabonus50", "ajaktemanovo", "grabdiskonbaru", "bibitinvestasi", "ajaibku", "pakedana", "diskongrab", "referral123", "bonusku", "kodeku123", "pakereferralsaya"]
    movie_title = ["pengabdi setan 2", "avatar: the way of water", "spider-man: no way home", "drama korea queen of tears", "kkn desa penari", "miracle in cell no. 7", "agak laen", "film marvel terbaru", "film dc terbaru", "inside out 2", "film horor indonesia", "film action hollywood"]
    cinema_name = ["xxi margo city", "cgv depok mall", "cinepolis pejaten village", "xxi plaza senayan", "cgv grand indonesia", "bioskop terdekat", "platform streaming netflix", "platform streaming disney+", "vidio", "wetv", "bioskop lokal"]
    job_field = ["digital marketing", "admin online shop", "content writer freelance", "programmer remote python", "programmer remote javascript", "desainer grafis ui", "desainer grafis ux", "customer service wfh", "data entry", "penerjemah", "guru les", "editor video", "social media specialist"]
    greeting = ["pagi", "siang", "sore", "malam", "weekend", "selamat idul fitri", "selamat natal", "selamat tahun baru", "halo", "hai", "assalamualaikum", "selamat pagi/siang/sore/malam"]
    event_happening = ["konser coldplay", "libur panjang lebaran", "piala dunia", "pertandingan persija vs persib", "konser blackpink", "event jejepangan comifuro", "event jejepangan ennichisai", "ulang tahun saya", "acara kantor", "libur sekolah", "pemilu", "konser taylor swift"]
    event_location = ["gbk senayan", "ice bsd", "ancol", "monas", "trans studio bandung", "jiexpo kemayoran", "rumah", "kantor", "kampus", "bali", "yogyakarta", "stadion", "taman kota"]
    song_title = ["lagu tulus - hati-hati di jalan", "bohemian rhapsody - queen", "lagu bts - dynamite", "lagu taylor swift - anti-hero", "lagu soegi bornean - asmalibrasi", "lagu new jeans - hype boy", "lagu favorit saya", "playlist galau", "lagu dangdut koplo", "lagu pop indonesia terbaru", "lagu barat hits"]
    artist_name = ["tulus", "queen", "bts", "taylor swift", "soegi bornean", "new jeans", "dewa 19", "sheila on 7", "penyanyi favorit saya", "band indie lokal", "mahalini", "rizky febian", "judika"]
    place_recommendation_request = ["tempat makan ramen enak", "wisata alam curug", "bengkel motor honda resmi", "cafe buat nugas yang ada wifi", "toko buku gramedia", "tempat nongkrong asik", "service laptop terpercaya", "pantai bagus", "gunung buat hiking pemula", "toko oleh-oleh murah"]
    shared_info = ["promo diskon shopee 12.12", "link berita kompas", "link berita detik", "video kucing lucu", "lowongan kerja di linkedin", "meme receh dari twitter", "artikel tips & trik bermanfaat", "link youtube tutorial", "kode voucher diskon", "info gempa", "jadwal kereta", "link streaming ilegal"]
    community_or_group = ["komunitas fotografi depok", "grup mancing mania", "alumni sma negeri 1 depok", "fans klub jkt48", "grup wa rt", "grup facebook hobi", "komunitas sepeda", "grup pecinta anime", "forum developer indonesia", "grup ibu-ibu arisan"]
    food_name = ["seblak", "nasi goreng", "sate ayam", "bakso", "rendang", "mie ayam", "gado-gado", "martabak", "pizza", "ayam geprek", "kopi susu", "boba"]
    item_name = ["harga iphone 15", "harga emas antam", "harga tiket pesawat ke bali", "harga motor nmax", "harga laptop macbook air", "harga saham bbca", "harga bitcoin hari ini", "harga beras", "harga minyak goreng", "harga tiket kereta", "harga bensin pertamax"]
    street_name = ["jalan margonda raya", "jalan juanda depok", "tol jagorawi", "jalan sudirman jakarta", "jalan thamrin jakarta", "jalan depan rumah", "jalan tol cipularang", "jalan daan mogot", "jalan gatot subroto", "gang kecil dekat rumah"]
    # --- Added for new templates ---
    review_number = ["1", "2", "5", "10", "pertama", "terakhir", "kesekian", "ke-100", "ke-1000"]
    developer_motivation = ["senang", "semangat update", "memperbaiki bug", "menurunkan harga", "menambah fitur gratis", "biar dibaca", "supaya diperhatikan", "agar viral", "biar rating naik"]
    app_name_question = ["begini", "unik ini", "agak aneh", "susah disebut", "kok namanya ini", "artinya apa", "filosofinya apa"]
    unrelated_need = ["teman curhat", "pekerjaan baru", "pinjaman uang cepat", "motivasi hidup", "solusi masalah pribadi", "jodoh", "liburan", "makanan enak", "pulsa gratis"]
    personal_story = ["saya lagi sedih banget hari ini", "kemarin saya baru putus cinta", "skripsi saya nggak kelar-kelar", "lagi pusing mikirin cicilan", "saya baru aja dapat kabar baik", "lagi galau", "butuh semangat", "hidup ini berat", "alhamdulillah sehat"]
    shared_experience = ["hpnya jadi lemot setelah update os", "susah cari kerja sekarang", "harga-harga pada naik", "kena tipu online shop", "akun sosmed dihack", "paket internet mahal", "listrik sering mati", "banjir di daerah saya", "macet parah tiap hari"]
    person_opinion = ["kata ahli x", "menurut teman saya", "saya baca di artikel y", "influencer z bilang", "kata pak rt", "menurut dosen saya", "orang tua saya bilang", "ustadz a berkata"]
    statement_about_topic = ["ini bagus untuk kesehatan", "sebaiknya dihindari", "ini lagi tren sekarang", "teknologi ini akan mengubah dunia", "itu cuma hoax", "penting untuk masa depan", "tidak ada gunanya", "harus dicoba", "wajib tahu"]
    other_platform = ["twitter", "facebook", "forum kaskus", "reddit", "platform sebelah", "instagram", "tiktok", "linkedin", "youtube", "blog pribadi"]
    feature_comparison = ["lebih lengkap", "lebih mudah dipakai", "gratis", "lebih canggih", "kurang lebih sama", "lebih stabil", "lebih banyak bug", "lebih mahal", "lebih murah"]
    preference = ["teh", "kopi", "musik pop", "film horor", "warna biru", "liburan ke pantai", "android", "windows", "nasi padang", "bakso"]
    alternative_preference = ["kopi", "teh", "musik rock", "film komedi", "warna merah", "liburan ke gunung", "ios", "macos", "soto ayam", "mie ayam"]
    suggestion = ["belajar skill baru", "investasi leher ke atas", "olahraga teratur", "baca buku", "nabung", "cari kerja sampingan", "mulai bisnis kecil", "berhenti merokok", "makan sehat"]
    alternative_suggestion = ["main game terus", "rebahan aja", "boros", "nonton drakor seharian", "scroll sosmed tanpa henti", "jajan sembarangan", "begadang tiap malam", "malas-malasan"]
    misinformation_claim = ["bumi itu datar", "vaksin itu berbahaya", "minum air es bikin gemuk", "5g menyebarkan virus", "pesan berantai ini harus disebar", "obat x menyembuhkan segala penyakit", "investasi y pasti untung 1000%", "berita ini benar adanya"]
    political_comment = ["semakin panas", "tidak jelas arahnya", "perlu perubahan", "semoga amanah", "saya tidak peduli", "golput aja lah", "calon a bagus", "partai b korup", "debat capres kemarin seru"]
    sports_team = ["persija", "persib", "manchester united", "liverpool", "real madrid", "barcelona", "timnas indonesia", "arema", "persebaya", "juventus", "ac milan", "bayern munchen"]
    sports_result = ["menang telak", "kalah lagi", "mainnya seri", "juara!", "gagal lolos", "imbang", "kalah tipis", "menang dramatis", "masuk final"]
    tv_show = ["sinetron ikatan cinta", "masterchef indonesia", "acara berita malam", "kartun spongebob", "serial netflix terbaru", "indonesian idol", "liga dangdut", "mata najwa", "film di trans tv"]
    tv_channel = ["rcti", "sctv", "indosiar", "trans tv", "net tv", "hbo", "tv lokal", "mnc tv", "gtv", "tvone", "metro tv", "kompas tv"]
    message_to_developer = ["terus berkarya", "jangan menyerah", "semoga sukses selalu", "tolong dengarkan kami", "terima kasih atas kerja kerasnya", "semangat!", "jangan pelit fitur", "perbaiki bug nya dong", "kembangkan terus"]
    short_greeting = ["terima kasih", "maaf", "permisi", "selamat", "sampai jumpa", "halo", "hai", "ok", "sip", "mantap"]
    app_category = ["editor foto", "game", "media sosial", "e-commerce", "berita", "produktivitas", "musik", "video player", "utilitas", "keuangan", "transportasi", "edukasi"]
    unrelated_skill = ["bahasa inggris", "masak", "main musik", "coding", "desain", "public speaking", "menulis"]
    random_question = ["hari ini tanggal berapa", "besok libur ga", "ada promo makanan ga", "film bagus apa ya", "lagu baru apa yg enak"]

    generated_count = 0
    existing_contents = set()
    while generated_count < count:
        template = random.choice(templates)
        try:
            replacements = {
                'action': random.choice(actions),
                'unrelated_app_name': random.choice(unrelated_app_names),
                'feature': random.choice(features),
                'related_app_name': random.choice(related_app_names),
                'expected_behavior': random.choice(expected_behaviors),
                'competitor_app_name': random.choice(competitor_app_names),
                'comparison_opinion': random.choice(comparison_opinions),
                'developer_name': random.choice(developer_names),
                'developer_origin': random.choice(developer_origins),
                'opinion_on_related_app': random.choice(opinions_on_related_app),
                'developer_reputation': random.choice(developer_reputations),
                'username': random.choice(usernames),
                'response_to_user': random.choice(response_to_user),
                'relevant_setting_location': random.choice(relevant_setting_location),
                'task': random.choice(tasks),
                'specific_pinjol_app': random.choice(specific_pinjol_app),
                'alternative_app_name': random.choice(alternative_app_name),
                'reason': random.choice(reasons),
                'purpose': random.choice(purposes),
                'issue': random.choice(issues),
                'operating_system': random.choice(operating_system),
                'device_brand': random.choice(device_brand),
                'weather_comment': random.choice(weather_comments),
                'location': random.choice(location),
                'personal_activity': random.choice(personal_activities),
                'wish_or_hope': random.choice(wishes_or_hopes),
                'other_username': random.choice(usernames), # Use 'username' list
                'topic': random.choice(topics),
                'famous_app': random.choice(famous_app),
                'contact_experience': random.choice(contact_experience),
                'phone_spec': random.choice(phone_spec),
                'specific_game': random.choice(specific_game),
                'old_app_version': random.choice(old_app_version),
                'past_experience': random.choice(past_experiences),
                'action_requiring_payment': random.choice(action_requiring_payment),
                'free_alternative': random.choice(free_alternative),
                'setting': random.choice(settings),
                'brand_name': random.choice(brand_name),
                'app_specific_criticism': random.choice(app_specific_criticism),
                'other_topic': random.choice(other_topic),
                'unrelated_activity': random.choice(unrelated_activity),
                'place_or_platform': random.choice(place_or_platform),
                'similar_app_name': random.choice(similar_app_name),
                'request_to_developer_general': random.choice(request_to_developer_general),
                'news_topic': random.choice(news_topic),
                'item_for_sale': random.choice(item_for_sale),
                'service_name': random.choice(service_name),
                'referral_code': random.choice(referral_code),
                'movie_title': random.choice(movie_title),
                'cinema_name': random.choice(cinema_name),
                'job_field': random.choice(job_field),
                'greeting': random.choice(greeting),
                'event_happening': random.choice(event_happening),
                'event_location': random.choice(event_location),
                'song_title': random.choice(song_title),
                'artist_name': random.choice(artist_name),
                'place_recommendation_request': random.choice(place_recommendation_request),
                'shared_info': random.choice(shared_info),
                'community_or_group': random.choice(community_or_group),
                'food_name': random.choice(food_name),
                'item_name': random.choice(item_name),
                'street_name': random.choice(street_name),
                # --- Added for new templates ---
                'review_number': random.choice(review_number),
                'rating_number': random.choice(rating_number), # Use existing list
                'developer_motivation': random.choice(developer_motivation),
                'app_name_question': random.choice(app_name_question),
                'unrelated_need': random.choice(unrelated_need),
                'personal_story': random.choice(personal_story),
                'shared_experience': random.choice(shared_experience),
                'person_opinion': random.choice(person_opinion),
                'statement_about_topic': random.choice(statement_about_topic),
                'other_platform': random.choice(other_platform),
                'feature_comparison': random.choice(feature_comparison),
                'preference': random.choice(preference),
                'alternative_preference': random.choice(alternative_preference),
                'suggestion': random.choice(suggestion),
                'alternative_suggestion': random.choice(alternative_suggestion),
                'misinformation_claim': random.choice(misinformation_claim),
                'political_comment': random.choice(political_comment),
                'sports_team': random.choice(sports_team),
                'sports_result': random.choice(sports_result),
                'tv_show': random.choice(tv_show),
                'tv_channel': random.choice(tv_channel),
                'message_to_developer': random.choice(message_to_developer),
                'short_greeting': random.choice(short_greeting),
                'app_category': random.choice(app_category),
                'unrelated_skill': random.choice(unrelated_skill), # Added
                'random_question': random.choice(random_question), # Added
            }

            valid_replacements = {k: v for k, v in replacements.items() if f"{{{k}}}" in template}
            content = template
            processed_keys = set()
            for k, v in valid_replacements.items():
                 if k not in processed_keys:
                     content = content.replace(f"{{{k}}}", v)
                     processed_keys.add(k)

            content = content.strip()

            # Add punctuation if missing (more selective)
            if content and not content.endswith(('.', '!', '?')):
                 if any(q_word in template for q_word in ["ada yang tahu", "kenapa", "gimana cara", "apakah", "kok", "bagaimana", "ada rekomendasi", "ada yang punya", "ada yang jual", "ada yang online", "ini software buatan", "kenapa namanya", "ada yang ngalamin", "apakah ini", "kuat ga ya", "ada nomor whatsapp", "bukan sih", "gimana sih makenya", "kok ratingnya bisa tinggi", "ada grup wa/tele nya ga", "ada saran lain", "berapaan ya sekarang", "bagus ga", "dimana ya", "apa ya bagusnya", "gimana sih", "ada yg sama", "lagi naik ya", "ada yg online?", "buatan", "artinya apa?", "filosofinya apa?", "gimana?", "dong?", "apa ya?", "arah mana?"]):
                     content += '?'
                 elif content not in ["pertamax gan!", "nyimak dulu", "info loker dong", "komen biar rame aja", "apalah", "tes komen doang", "sundul gan", "jejak digital", "salam kenal", "ok", "sip", "mantap"]:
                     # Avoid adding period to very short or greeting-like phrases
                     if len(content.split()) > 2:
                         pass # Let it end without punctuation for more naturalness sometimes
                         # content += '.' # Optionally add period back if desired

            # Ensure content is meaningful and not already generated
            if content and len(content) > 5 and content not in existing_contents:
                contents.append((content, 1)) # Label 1 for irrelevant
                existing_contents.add(content)
                generated_count += 1
        except KeyError as e:
            # print(f"Warning: KeyError {e} in template: '{template}' with replacements {valid_replacements}")
            pass
        except Exception as e:
            # print(f"Error generating irrelevant content with template '{template}': {e}")
            pass

    return contents


def generate_explicit_spam(count):
    """Generates varied explicit spam (Label 2) with real examples/patterns."""
    spams = []
    # --- MODIFIED & ADDED TEMPLATES (Increased Variety, Hyperbole, Lowercase) ---
    templates = [
        # Original templates modified/kept/expanded & lowercased
        "butuh {service}? hubungi {contact_info} sekarang! dijamin {guarantee} 100%!",
        "dapatkan {benefit} gratis! klik link di bio @{username_socmeds} atau {spam_url_short} sekarang!",
        "situs {topic} terbaik & terpercaya se-indonesia >> {url}. bonus {bonus_offer} menanti!",
        "kode promo: {promo_code} untuk diskon {discount}! khusus {time_limit}!",
        "{gibberish} {gibberish} {spam_call_to_action}",
        "{excessive_emojis} {spam_call_to_action} {excessive_emojis} jangan sampai kehabisan!",
        "{random_chars}...{random_chars}... kunjungi {url}!",
        "jual {item} murah ({item_condition}), wa {phone_number}. stok terbatas banget!",
        "join grup {group_topic} di {link_platform}: {group_link}. member aktif & info update!",
        "cuma tes komen. {random_phrase}",
        "mod {app_name} terbaru unlocked all features gratis download di {spam_url} no password!",
        "mod {app_name} terbaru unlocked vip gratis download di {spam_url} no password!",
        "investasi {investment_type} pasti profit! modal kecil untung besar! cek {url_invest} buktikan sendiri!",
        "pinjaman online {loan_type}, cair dalam 5 menit tanpa bi checking! {contact_or_link}",
        "pinjaman online {loan_type}, cair dalam 5 menit tanpa jaminan! {contact_or_link}",
        "{repetitive_text}, {repetitive_text}, {repetitive_text}!!!",
        "follow {account_type} kami: {account_name} untuk info {account_topic} terupdate!",
        "menang {prize} mudah di {website_name}! daftar gratis sekarang juga!",
        "tingkatkan {metric} anda dengan jasa kami di {contact_email}. harga promo khusus bulan ini!",
        "hanya bintang 5 {stars} yang membuktikan kualitasnya! yang kasih bintang 1 sirik!",
        "game {game_genre} penghasil saldo dana nyata: {game_link}. withdraw cepat & mudah!",
        "game {game_genre} penghasil saldo ovo nyata: {game_link}. withdraw cepat & mudah!",
        "mau {goal}? kunjungi {website_address}, solusi cepat dan terpercaya!",
        "zzzzzzzzzzzzzzzz {another_spam_phrase} zzzzzzzzzzzzzzzz kunjungi {url}",
        "peringatan keamanan: akun {service_name} anda bermasalah. segera verifikasi di {phishing_link} untuk menghindari pemblokiran.",
        "daftar {platform_name} sekarang dan dapatkan bonus {bonus_amount}! link: {registration_link}",
        "rahasia {skill} terbongkar! ebook gratis di {course_link}",
        "rahasia {skill} terbongkar! video tutorial gratis di {course_link}",
        "{single_word_spam}! {single_word_spam}! {single_word_spam}! klik {spam_url_short}!",
        "cek {product_category} terbaru diskon gila-gilaan di {ecommerce_link}",
        "nonton {movie_genre} gratis full hd sub indo tanpa iklan: {streaming_link}",
        "obat {health_product} herbal ampuh atasi {disease}. pesan via wa {whatsapp_number}",
        "lowongan kerja {job_title}, gaji {salary_range}. kirim cv ke {job_email} (no tipu!)",
        "selamat! nomor anda terpilih memenangkan {fake_prize}! klaim segera di {scam_link} (batas waktu 24 jam)",
        "tingkatkan {social_media_metric} anda! jasa {social_media_service} murah & permanen -> dm {contact_ig}",
        "butuh {financial_service} cepat tanpa ribet? kami solusinya! cek {website_finance}",
        "cek skor kredit anda gratis! {phishing_link}",
        "main {game_name} dapat {in_game_currency} gratis! klaim di {spam_url}",
        "pesan {transport_service} dapat diskon {discount}! pakai kode {promo_code}!",
        "ini adalah {hyperbole_noun} {app_category} {hyperbole_adj} yang pernah ada! {spam_call_to_action}",
        "dijamin {hyperbole_guarantee} kalau pakai ini! cek {url}!",
        "{hyperbole_adj} banget! {hyperbole_comment}. wajib coba {spam_url_short}",
        "solusi {hyperbole_noun} nomor #1 di dunia untuk {goal}! {contact_info}",
        "tidak ada yang bisa mengalahkan {app_name}! {hyperbole_adj} se-alam semesta! {excessive_emojis}",
        "pengalaman {hyperbole_adj} menanti anda! klik {spam_url} sekarang!",
        "ubah hidupmu jadi {hyperbole_adj} dengan {product_category} ini! info: {contact_email}",
        "semua orang bilang ini {hyperbole_adj}! buktikan di {website_name}!",
        "rating 1? pasti {negative_assumption}! ini jelas {hyperbole_adj}!",
        "dengan {service}, hasil {hyperbole_adj} dalam {short_time_promise}! {guarantee}!",
        "ini adalah {hyperbole_negative_adj} {app_category} yang pernah ada! jangan buang waktumu!",
        "{app_name} itu {hyperbole_negative_adj}, bikin nyesel download!",
        "sudah coba, rasanya {hyperbole_negative_adj} banget",
        "aplikasi ini benar-benar {hyperbole_negative_adj}, nggak sesuai harapan!",
        "{hyperbole_negative_adj} parah! mending cari alternatif lain dari {app_name}",
        "kalau kamu suka disiksa, silakan coba yang {hyperbole_negative_adj} ini!",
        "pengalaman paling {hyperbole_negative_adj} sepanjang hidup gue",
        "jangan sampai ketipu! ini aplikasi paling {hyperbole_negative_adj} di play store.",
        "{app_name} = {hyperbole_negative_adj}. gak recommended sama sekali!",
        "cuma buang-buang waktu dan kuota. {hyperbole_negative_adj} banget sumpah!",
        "virus terdeteksi di perangkat anda! klik {phishing_link} untuk membersihkan segera!", # scareware/phishing
        "pembaruan sistem penting diperlukan. klik {malware_link} untuk mengunduh.", # malware link
        "anda memenangkan undian {fake_lottery_name}! masukkan data bank di {phishing_link} untuk klaim.", # phishing
        "paket anda tertahan di bea cukai. bayar pajak di {scam_link} agar bisa dikirim.", # package scam
        "tonton video viral {viral_topic} eksklusif hanya di {spam_url}!", # clickbait
        "hasilkan uang dari rumah hanya dengan {simple_task}! daftar di {pyramid_scheme_link}", # pyramid scheme/mlm
        "obat kuat {health_product} bikin pasangan makin cinta! rahasia & aman. wa {whatsapp_number}", # adult content spam
        "sewa {illegal_item} murah dan aman. kontak {contact_info} (privasi terjamin).", # illegal service/item
        "mau tau siapa yang sering kepoin profil {social_media_platform} kamu? cek di {phishing_link}!", # profile checker scam
        "dapatkan {in_game_currency} {game_name} gratis dengan generator kami! {spam_url}", # game currency generator scam
        "beli {product_category} kw super mirip ori 99%! harga miring, kualitas bintang 5! cek ig {contact_ig}", # counterfeit goods
        "langganan {premium_service} murah via {payment_method_unofficial}. dm {username_socmeds}", # unofficial service sales
        "{repetitive_text} {url} {repetitive_text} {url}", # repetition with url
        "({random_chars}) {spam_call_to_action} ({random_chars}) -> {url}", # random chars framing cta
        "jual akun game {famous_game} murah, cek profil!",  # selling account (borderline spam)

        # --- ADDED: More Spam Variations (Lowercase) ---
        "aplikasi {app_name} ini {hyperbole_adj}! {spam_call_to_action}",
        "jangan download {app_name}, isinya {hyperbole_negative_adj} semua!",
        "mau {benefit}? gampang! klik {spam_url_short} aja!",
        "situs {topic} paling {hyperbole_adj}! bonus {bonus_offer} melimpah! {url}",
        "promo {discount} pakai kode {promo_code}! terbatas {time_limit}! {ecommerce_link}",
        "{excessive_emojis} {service} terbaik cuma di {contact_info}! {guarantee}! {excessive_emojis}",
        "download mod {app_name} {version_number} unlock all {spam_url}",
        "investasi {investment_type} di {url_invest}, {hyperbole_guarantee}!",
        "butuh {loan_type}? wa {phone_number} sekarang! proses {short_time_promise}!",
        "follow @{username_socmeds} buat info {account_topic} {hyperbole_adj}!",
        "menangkan {prize} di {website_name}! {spam_call_to_action}",
        "jasa {metric} {social_media_service} termurah -> {contact_ig}",
        "game {game_genre} ({game_link}) bisa hasilin {benefit}!",
        "raih {goal} dengan {hyperbole_noun} ini: {website_address}",
        "akun {service_name} anda dalam bahaya! klik {phishing_link}!",
        "daftar {platform_name} ({registration_link}) dapat {bonus_amount}!",
        "belajar {skill} instan! {course_link}",
        "{single_word_spam}! {single_word_spam}! {url}",
        "nonton {movie_genre} terbaru di {streaming_link}!",
        "obat {health_product} atasi {disease}, hubungi {whatsapp_number}",
        "loker {job_title} gaji {salary_range}, email {job_email}",
        "selamat! anda dapat {fake_prize}! klaim di {scam_link}",
        "{financial_service} tanpa ribet? {website_finance} solusinya!",
        "generator {in_game_currency} {game_name} work 100%! {spam_url}",
        "diskon {discount} {transport_service} pakai kode {promo_code}!",
        "aplikasi ini {hyperbole_negative_adj}! jangan install!",
        "peringatan! {malware_link} jangan diklik!",
        "undian {fake_lottery_name} tipu-tipu! jangan isi data di {phishing_link}",
        "paket dari luar negeri? hati-hati scam bea cukai {scam_link}",
        "video {viral_topic} full no sensor {spam_url}",
        "kerja {simple_task} dibayar dollar? {pyramid_scheme_link} (hati-hati mlm)",
        "obat {health_product} ilegal! jangan beli di {whatsapp_number}",
        "jual {illegal_item}? laporkan ke {contact_info} (ini contoh, jangan diikuti)",
        "cek profil {social_media_platform} stalker? {phishing_link} itu bohong!",
        "{product_category} kw murah? cek {contact_ig} (waspada barang palsu)",
        "langganan {premium_service} ilegal? {username_socmeds} (risiko akun dibanned)",
        "jual akun {famous_game} sultan? cek {account_name}",
        "butuh {service}? {contact_info} {guarantee}",
        "gratis {benefit}! klik {spam_url_short}",
        "situs {topic} {url} bonus {bonus_offer}",
        "kode {promo_code} diskon {discount} ({time_limit})",
        "{gibberish} {spam_call_to_action}",
        "{excessive_emojis} {spam_call_to_action}",
        "kunjungi {url} {random_chars}",
        "jual {item} ({item_condition}) wa {phone_number}",
        "grup {group_topic} {link_platform}: {group_link}",
        "mod {app_name} {spam_url}",
        "investasi {investment_type} {url_invest}",
        "pinjol {loan_type} {contact_or_link}",
        "{repetitive_text}!",
        "follow {account_type} {account_name} ({account_topic})",
        "menang {prize} di {website_name}",
        "tingkatkan {metric} -> {contact_email}",
        "game {game_genre} ({game_link}) hasilkan {benefit}",
        "mau {goal}? ke {website_address}",
        "verifikasi {service_name} di {phishing_link}",
        "daftar {platform_name} ({registration_link}) bonus {bonus_amount}",
        "ebook {skill} gratis {course_link}",
        "{single_word_spam}! {spam_url_short}",
        "diskon {product_category} di {ecommerce_link}",
        "nonton {movie_genre} gratis {streaming_link}",
        "obat {health_product} ({disease}) wa {whatsapp_number}",
        "loker {job_title} ({salary_range}) email {job_email}",
        "menang {fake_prize}? klaim {scam_link}",
        "jasa {social_media_metric} ({social_media_service}) dm {contact_ig}",
        "{financial_service}? cek {website_finance}",
        "cek kredit gratis {phishing_link}",
        "klaim {in_game_currency} {game_name} di {spam_url}",
        "diskon {transport_service} kode {promo_code}",
        "{hyperbole_adj}! {spam_call_to_action} {url}",
        "{hyperbole_negative_adj}! jangan download {app_name}",
        "virus! klik {phishing_link}",
        "update sistem {malware_link}",
        "menang undian {fake_lottery_name}? {phishing_link}",
        "paket tertahan {scam_link}",
        "video viral {viral_topic} {spam_url}",
        "kerja {simple_task} {pyramid_scheme_link}",
        "obat kuat {health_product} {whatsapp_number}",
        "sewa {illegal_item} {contact_info}",
        "cek stalker {social_media_platform} {phishing_link}",
        "generator {in_game_currency} {game_name} {spam_url}",
        "beli {product_category} kw {contact_ig}",
        "langganan {premium_service} murah {username_socmeds}",
        "jual akun {famous_game} {account_name}",
        "cuma {single_word_spam} {single_word_spam} {single_word_spam}",
        "{repetitive_text} {url} {repetitive_text}",
        "({random_chars}) {spam_call_to_action} {url}",

        # --- ADDED/MODIFIED: Templates with EXCESSIVE CAPS ---
        "BUTUH {service}?? HUBUNGI {contact_info} SEKARANG!! DIJAMIN {guarantee} 100% PASTI {hyperbole_adj}!!",
        "DAPATKAN {benefit} GRATIS!!! KLIK LINK DI BIO @{username_socmeds} ATAU {spam_url_short} SEKARANG JUGA!",
        "SITUS {topic} TERBAIK & TERPERCAYA SE-INDONESIA >> {url}. BONUS {bonus_offer} MENANTI ANDA!",
        "KODE PROMO: {promo_code} UNTUK DISKON {discount} GILA! KHUSUS {time_limit}!",
        "{gibberish} {gibberish} {spam_call_to_action_upper}", # Use new uppercase list
        "{excessive_emojis} {spam_call_to_action_upper} {excessive_emojis} JANGAN SAMPAI KEHABISAN!",
        "{random_chars}...{random_chars}... KUNJUNGI {url} SEKARANG!",
        "JUAL {item} MURAH ({item_condition}), WA {phone_number}. STOK TERBATAS BANGET!",
        "JOIN GRUP {group_topic} DI {link_platform}: {group_link}. MEMBER AKTIF & INFO UPDATE!",
        "MOD {app_name} TERBARU {version_number} UNLOCKED ALL FEATURES GRATIS DOWNLOAD DI {spam_url} NO PASSWORD!",
        "MOD {app_name} {version_number} UNLOCKED VIP GRATIS DOWNLOAD DI {spam_url} NO PASSWORD!",
        "INVESTASI {investment_type} PASTI PROFIT! MODAL KECIL UNTUNG BESAR! CEK {url_invest} BUKTIKAN SENDIRI!",
        "PINJAMAN ONLINE {loan_type}, CAIR DALAM 5 MENIT TANPA BI CHECKING! {contact_or_link}",
        "PINJAMAN ONLINE {loan_type}, CAIR DALAM 5 MENIT TANPA JAMINAN! {contact_or_link}",
        "{repetitive_text_upper}, {repetitive_text_upper}, {repetitive_text_upper}!!!", # Use new uppercase list
        "FOLLOW {account_type} KAMI: {account_name} UNTUK INFO {account_topic} TERUPDATE!",
        "MENANG {prize} MUDAH DI {website_name}! DAFTAR GRATIS SEKARANG JUGA!",
        "TINGKATKAN {metric} ANDA DENGAN JASA KAMI DI {contact_email}. HARGA PROMO KHUSUS BULAN INI!",
        "GAME {game_genre} PENGHASIL SALDO DANA NYATA: {game_link}. WITHDRAW CEPAT & MUDAH!",
        "GAME {game_genre} PENGHASIL SALDO OVO NYATA: {game_link}. WITHDRAW CEPAT & MUDAH!",
        "MAU {goal}? KUNJUNGI {website_address}, SOLUSI CEPAT DAN TERPERCAYA!",
        "PERINGATAN KEAMANAN: Akun {service_name} Anda Bermasalah. SEGERA VERIFIKASI di {phishing_link} Untuk Menghindari PEMBLOKIRAN.", # Mixed case warning
        "DAFTAR {platform_name} SEKARANG DAN DAPATKAN BONUS {bonus_amount}! LINK: {registration_link}",
        "RAHASIA {skill} TERBONGKAR! EBOOK GRATIS DI {course_link}",
        "RAHASIA {skill} TERBONGKAR! VIDEO TUTORIAL GRATIS DI {course_link}",
        "{single_word_spam_upper}! {single_word_spam_upper}! {single_word_spam_upper}! KLIK {spam_url_short}!", # Use new uppercase list
        "CEK {product_category} TERBARU DISKON GILA-GILAAN DI {ecommerce_link}",
        "NONTON {movie_genre} GRATIS FULL HD SUB INDO TANPA IKLAN: {streaming_link}",
        "OBAT {health_product} HERBAL AMPUH ATASI {disease}. PESAN VIA WA {whatsapp_number}",
        "LOWONGAN KERJA {job_title}, GAJI {salary_range}. KIRIM CV KE {job_email} (NO TIPU!)",
        "SELAMAT! NOMOR ANDA TERPILIH MEMENANGKAN {fake_prize}! KLAIM SEGERA DI {scam_link} (BATAS WAKTU 24 JAM)",
        "TINGKATKAN {social_media_metric} ANDA! JASA {social_media_service} MURAH & PERMANEN -> DM {contact_ig}",
        "BUTUH {financial_service} CEPAT TANPA RIBET? KAMI SOLUSINYA! CEK {website_finance}",
        "CEK SKOR KREDIT ANDA GRATIS! {phishing_link}",
        "MAIN {game_name} DAPAT {in_game_currency} GRATIS! KLAIM DI {spam_url}",
        "PESAN {transport_service} DAPAT DISKON {discount}! PAKAI KODE {promo_code}!",
        "INI ADALAH {hyperbole_noun} {app_category} {hyperbole_adj_upper} YANG PERNAH ADA! {spam_call_to_action_upper}", # Use new uppercase list
        "DIJAMIN {hyperbole_guarantee_upper} KALAU PAKAI INI! CEK {url}!", # Use new uppercase list
        "{hyperbole_adj_upper} BANGET! {hyperbole_comment}. WAJIB COBA {spam_url_short}", # Use new uppercase list
        "SOLUSI {hyperbole_noun} NOMOR #1 DI DUNIA UNTUK {goal}! {contact_info}",
        "TIDAK ADA YANG BISA MENGALAHKAN {app_name}! {hyperbole_adj_upper} SE-ALAM SEMESTA! {excessive_emojis}", # Use new uppercase list
        "PENGALAMAN {hyperbole_adj_upper} MENANTI ANDA! KLIK {spam_url} SEKARANG!", # Use new uppercase list
        "UBAH HIDUPMU JADI {hyperbole_adj_upper} DENGAN {product_category} INI! INFO: {contact_email}", # Use new uppercase list
        "SEMUA ORANG BILANG INI {hyperbole_adj_upper}! BUKTIKAN DI {website_name}!", # Use new uppercase list
        "DENGAN {service}, HASIL {hyperbole_adj_upper} DALAM {short_time_promise}! {guarantee_upper}!", # Use new uppercase list
        "INI ADALAH {hyperbole_negative_adj_upper} {app_category} YANG PERNAH ADA! JANGAN BUANG WAKTUMU!", # Use new uppercase list
        "{app_name} ITU {hyperbole_negative_adj_upper}, BIKIN NYESEL DOWNLOAD!", # Use new uppercase list
        "APLIKASI INI BENAR-BENAR {hyperbole_negative_adj_upper}, NGGAK SESUAI HARAPAN!", # Use new uppercase list
        "{hyperbole_negative_adj_upper} PARAH! MENDING CARI ALTERNATIF LAIN DARI {app_name}", # Use new uppercase list
        "JANGAN SAMPAI KETIPU! INI APLIKASI PALING {hyperbole_negative_adj_upper} DI PLAY STORE.", # Use new uppercase list
        "{app_name} = {hyperbole_negative_adj_upper}. GAK RECOMMENDED SAMA SEKALI!", # Use new uppercase list
        "CUMA BUANG-BUANG WAKTU DAN KUOTA. {hyperbole_negative_adj_upper} BANGET SUMPAH!", # Use new uppercase list
        "VIRUS TERDETEKSI DI PERANGKAT ANDA! KLIK {phishing_link} UNTUK MEMBERSIHKAN SEGERA!",
        "PEMBARUAN SISTEM PENTING DIPERLUKAN. KLIK {malware_link} UNTUK MENGUNDUH.",
        "ANDA MEMENANGKAN UNDIAN {fake_lottery_name}! MASUKKAN DATA BANK DI {phishing_link} UNTUK KLAIM.",
        "PAKET ANDA TERTAHAN DI BEA CUKAI. BAYAR PAJAK DI {scam_link} AGAR BISA DIKIRIM.",
        "TONTON VIDEO VIRAL {viral_topic} EKSKLUSIF HANYA DI {spam_url}!",
        "HASILKAN UANG DARI RUMAH HANYA DENGAN {simple_task}! DAFTAR DI {pyramid_scheme_link}",
        "OBAT KUAT {health_product} BIKIN PASANGAN MAKIN CINTA! RAHASIA & AMAN. WA {whatsapp_number}",
        "SEWA {illegal_item} MURAH DAN AMAN. KONTAK {contact_info} (PRIVASI TERJAMIN).",
        "MAU TAU SIAPA YANG SERING KEPOIN PROFIL {social_media_platform} KAMU? CEK DI {phishing_link}!",
        "DAPATKAN {in_game_currency} {game_name} GRATIS DENGAN GENERATOR KAMI! {spam_url}",
        "BELI {product_category} KW SUPER MIRIP ORI 99%! HARGA MIRING, KUALITAS BINTANG 5! CEK IG {contact_ig}",
        "LANGGANAN {premium_service} MURAH VIA {payment_method_unofficial}. DM {username_socmeds}",
        "{repetitive_text_upper} {url} {repetitive_text_upper} {url}", # Use new uppercase list
        "({random_chars}) {spam_call_to_action_upper} ({random_chars}) -> {url}", # Use new uppercase list
        "JUAL AKUN GAME {famous_game} MURAH, CEK PROFIL!",
        "{excessive_emojis} {single_word_spam_upper} {single_word_spam_upper} {single_word_spam_upper} {excessive_emojis}", # Use new uppercase list
        "WARNING! {service_name} bermasalah! VERIFIKASI SEKARANG: {phishing_link}", # Mixed case warning
        "KESEMPATAN EMAS! {benefit} GRATIS! {spam_call_to_action_upper} DI {spam_url_short}", # Use new uppercase list
        "SITUS {topic} NOMOR #1 >> {url}. {bonus_offer} TERBESAR!",
        "PROMO {promo_code} DISKON {discount}! BERAKHIR {time_limit}! JANGAN SAMPAI KELEWATAN!",
        "DOWNLOAD MOD {app_name} VERSI {version_number} FULL UNLOCKED DI {spam_url} SEKARANG!",
        "INVESTASI {investment_type} DIJAMIN {hyperbole_guarantee_upper}! CEK {url_invest}!", # Use new uppercase list
        "PINJOL {loan_type} CAIR {short_time_promise}! HUBUNGI {contact_or_link}!",
        "MAU {metric} NAIK DRASTIS? PAKAI JASA KAMI! {contact_email} HARGA SPESIAL!",
        "GAME {game_genre} PENGHASIL {benefit} TERBUKTI MEMBAYAR! {game_link}",
        "RAHASIA {goal} TERUNGKAP! KUNJUNGI {website_address} SEKARANG!",
        "JANGAN KLIK! {phishing_link} ADALAH PENIPUAN!", # Negative warning style
        "DAFTAR {platform_name} DAPAT {bonus_amount}! {registration_link} BURUAN!",
        "EBOOK {skill} GRATIS! DOWNLOAD DI {course_link} SEBELUM DIHAPUS!",
        "NONTON {movie_genre} FULL HD GRATIS! {streaming_link} NO IKLAN!",
        "OBAT {health_product} AMPUH! PESAN DI {whatsapp_number} SEKARANG!",
        "LOKER {job_title} GAJI {salary_range}! KIRIM CV KE {job_email} SEGERA!",
        "ANDA MENANG {fake_prize}! KLAIM DI {scam_link} SEBELUM {time_limit}!",
        "JASA {social_media_service} TERMURAH SE-IG! DM {contact_ig}!",
        "{financial_service} TANPA RIBET? {website_finance} SOLUSINYA!",
        "GENERATOR {in_game_currency} {game_name} 100% WORK! {spam_url}",
        "DISKON {discount} {transport_service} KODE {promo_code}! BURUAN PAKAI!",
        "APLIKASI {hyperbole_negative_adj_upper}! JANGAN INSTALL {app_name}!", # Use new uppercase list
        "PERHATIAN! VIRUS TERDETEKSI! BERSIHKAN DI {phishing_link}!",
        "UNDUH PEMBARUAN KEAMANAN PENTING: {malware_link}",
        "SELAMAT ANDA MENANG {fake_lottery_name}! MASUKKAN DATA DI {phishing_link}!",
        "PAKET TERTARAN DI BEA CUKAI! BAYAR DI {scam_link}!",
        "VIDEO {viral_topic} FULL? KLIK {spam_url}!",
        "KERJA {simple_task} DAPAT UANG? DAFTAR {pyramid_scheme_link}!",
        "JUAL {illegal_item} AMAN? HUB {contact_info}!",
        "CEK STALKER {social_media_platform}? {phishing_link}!",
        "GENERATOR {in_game_currency} {game_name}? {spam_url}!",
        "{product_category} KW SUPER? IG {contact_ig}!",
        "LANGGANAN {premium_service} MURAH? DM {username_socmeds}!",
    ]

    # --- Expanded Lists (More Variety, Real Examples, Hyperbole, Lowercase) ---
    # (All keywords converted to lowercase)
    # Modified list with uppercase calls to action
    spam_call_to_action_upper = ["KLIK SEKARANG!", "DAFTAR GRATIS!", "JANGAN SAMPAI KETINGGALAN!", "PESAN SEKARANG!",
                                 "DOWNLOAD SEKARANG!", "KUNJUNGI WEBSITE KAMI!", "HUBUNGI KAMI SEGERA!",
                                 "AMBIL BONUSMU!", "MAIN SEKARANG!", "BELI SEKARANG JUGA!", "CEK LINK DI BIO!",
                                 "SWIPE UP!", "KLIK DISINI!", "INFO LENGKAP KLIK!", "BURUAN KLIK!", "JANGAN RAGU!",
                                 "GABUNG SEKARANG!", "LIHAT SEKARANG!", "COBA SEKARANG!", "PESAN DISINI!"]

    # Modified list with uppercase guarantees
    guarantee_upper = ["AMANAH 100%", "TERPERCAYA NO #1", "PASTI PROFIT!", "GARANSI UANG KEMBALI!", "DIJAMIN PUAS!",
                       "100% WORK!", "ANTI RUNGKAD!", "PASTI CUAN!", "DIJAMIN BERHASIL!", "TERBUKTI MEMBAYAR!",
                       "PROSES KILAT!", "TANPA RIBET!", "PASTI MENANG!", "JACKPOT PASTI!", "PRIVASI AMAN 100%"]

    # Modified list with uppercase repetitive texts
    repetitive_text_upper = ["SPAM SPAM SPAM", "KLIK KLIK KLIK", "MURAH MURAH MURAH", "PROMO PROMO PROMO",
                             "GACOR GACOR GACOR", "WD WD WD", "AMAN AMAN AMAN", "TERPERCAYA TERPERCAYA",
                             "BONUS BONUS BONUS", "GRATIS GRATIS GRATIS", "CEPAT CEPAT CEPAT", "UNTUNG UNTUNG UNTUNG",
                             "MENANG MENANG MENANG", "JACKPOT JACKPOT JACKPOT", "VIRAL VIRAL VIRAL"]

    # Modified list with uppercase single word spam
    single_word_spam_upper = ["PROMO", "GRATIS", "DISKON", "KLIK", "DAFTAR", "MURAH", "CEPAT", "UNTUNG", "GACOR",
                              "BONUS", "JACKPOT", "MENANG", "TERBAIK", "VIRAL", "MANTAP", "OKE", "SPAM", "TES", "COBA",
                              "HOT", "NEW", "SALE", "URGENT", "PENTING", "SEGERA", "LIMITED", "WOW", "AMAZING", "BEST"]

    # Modified list with uppercase hyperbolic adjectives
    hyperbole_adj_upper = ["TERBAIK", "TERCANGGIH", "TERHEBAT", "PALING AMPUH", "NOMOR 1", "TAK TERTANDINGI",
                           "LUAR BIASA", "AJAIB", "REVOLUSIONER", "TERCEPAT", "TERMURAH", "PALING MENGUNTUNGKAN",
                           "SEMPURNA", "FANTASTIS", "ULTIMATE", "DEWA", "GILA", "MANTAP JIWA", "PALING GACOR",
                           "TERPERCAYA", "TERBUKTI"]

    # Modified list with uppercase negative hyperbolic adjectives
    hyperbole_negative_adj_upper = ["TERBURUK", "NGACO", "HANCUR BANGET", "SANGAT PARAH", "GAK MASUK AKAL",
                                    "GAK LAYAK PAKAI", "BIKIN TRAUMA", "LEBAY TAPI ZONK", "SAMPAH", "AMPAS", "PAYAH",
                                    "KACAU BALAU", "MENYESATKAN", "PENIPU", "BOHONG", "PALSU", "ABAL-ABAL",
                                    "JELEK BANGET"]

    # Modified list with uppercase guarantees
    hyperbole_guarantee_upper = ["PASTI BERHASIL", "DIJAMIN SUKSES 100%", "ANTI GAGAL", "HASIL INSTAN",
                                 "PROFIT RIBUAN PERSEN", "HIDUPMU BERUBAH DRASTIS", "PASTI KAYA", "DIJAMIN MANJUR",
                                 "LANGSUNG WORK", "AUTO SULTAN", "GARANSI 1000%", "TANPA RESIKO", "MODAL KEMBALI CEPAT"]

    famous_game = ['clash of clans', 'mobile legends', 'pubg mobile', 'free fire', 'genshin impact', 'roblox',
                   'stumble guys', 'valorant', 'dota 2', 'arena of valor', 'pokemon go', 'minecraft', 'among us',
                   'call of duty mobile', 'honkai star rail', 'efootball']
    app_category = ['editor foto', 'game', 'media sosial', 'e-commerce', 'berita', 'produktivitas', 'musik',
                    'video player', 'utilitas', 'keuangan', 'transportasi', 'edukasi', 'kesehatan', 'gaya hidup']
    services = ['dana cepat cair ilegal', 'jasa seo murah garansi halaman 1 google', 'followers instagram aktif',
                'followers tiktok aktif', 'like instagram aktif', 'like tiktok aktif',
                'pembuatan website toko online murah', 'backlink pbn berkualitas da tinggi',
                'backlink pbn berkualitas pa tinggi', 'joki game mobile legends sampai mythic',
                'joki game free fire sampai master', 'pulsa darurat telkomsel bunga rendah',
                'pulsa darurat xl bunga rendah', 'akun premium netflix lifetime murah',
                'akun premium spotify lifetime murah', 'akun premium canva lifetime murah', 'jasa hapus data pinjol',
                'pembuatan ktp palsu', 'pembuatan sim palsu', 'jasa peretas akun sosmed', 'jasa lacak lokasi nomor hp',
                'jasa teror online', 'jasa view youtube', 'jasa subscriber youtube', 'jasa komentar buzzer',
                'jasa gestun online', 'jasa pembuatan skripsi', 'jasa titip barang luar negeri', 'jasa ramal nasib']
    contact_infos = ['0812-3456-7890 (wa only fast respon)', 'admin@spamdomain.com', 'wa 0899-1111-2222',
                     'dm ig @spam_seller_indo', 'klik link di bio profil!', 'bit.ly/kontakspamnow',
                     't.me/spamservicecenter', 'line id: ribbo', 'kontak di website kami', 'wa.me/628xxxxxxxxxx',
                     'cek ig @rik_store_id', 'telegram: @rikadmin']
    guarantees = ['amanah no tipu-tipu', 'terpercaya sejak 2010', 'proses cepat 5 menit cair', 'pasti profit',
                  'pasti cuan', '100% work no hoax', 'garansi uang kembali jika gagal', 'pasti menang', 'pasti jackpot',
                  'dijamin puas', 'hasil permanen', 'privasi aman', 'pasti berhasil', 'dijamin ampuh',
                  'terbukti membayar', 'anti banned']
    benefits = ['saldo gopay 50rb', 'saldo ovo 100rb', 'saldo dana 50rb', 'pulsa gratis 100rb all operator',
                'voucher diskon shopee 50%', 'voucher diskon tokopedia 50%', 'akun premium canva pro sebulan',
                "ebook 'cara cepat kaya' gratis", 'konsultasi gratis masalah pinjol', 'iphone 15 gratis',
                'liburan ke bali gratis', 'mobil baru gratis', 'uang tunai 1 juta', 'emas antam 1 gram',
                'voucher makan gratis', 'produk gratis']
    username_socmeds = ['jualfollowers_indo1', 'promo_gila_official', 'gratisan_mantul_id', 'rajaspam_nusantara',
                        'infopinjol_cepatcair', 'slotgacor_maxwin_hariini', 'judionline_terpercaya_indo',
                        'bisnisonline_sukses', 'akunpremium_murahbanget', 'viralbanget_id', 'spamking_official',
                        'bonus_hunter77', 'admin_trusted_spam', 'ig_spam_murah']
    spam_url_short = ['https://bit.ly/bonusgratis123', 'https://s.id/promospamindo', 'https://tinyurl.com/klikuntung77',
                      'https://cutt.ly/spampromo', 'https://rebrand.ly/bonusspam', 'https://rb.gy/spamdewa',
                      'https://is.gd/linkspam', 'https://bit.do/yuhu', 'https://goo.gl/spamxyz',
                      'https://shorturl.at/spam1']
    topics = ['slot gacor anti rungkad pragmatic', 'slot gacor anti rungkad pgsoft', 'togel online hk terpercaya',
              'togel online sgp terpercaya', 'togel online sydney terpercaya', 'berita viral artis terbaru no sensor',
              'film gratis sub indo lk21', 'film gratis sub indo rebahin', 'prediksi bola jitu parlay malam ini',
              'cheat game mobile legends terbaru anti banned', 'cheat game pubg terbaru anti banned',
              'video viral terbaru', 'investasi bodong terbaru', 'lowongan kerja fiktif', 'obat kuat ilegal',
              'judi bola online', 'poker online uang asli', 'download lagu mp3 gratis', 'aplikasi mod terbaru',
              'bokep viral']
    urls = ['www.mainmenangterus.com', 'www.juditerpercaya123.net', 'www.klikdisinimenang.info',
            'www.nontonhematbanget.tv', 'https://rajajudi.online', 'https://slotmaxwin88.cc',
            'https://agenresmiterpercaya.com', 'https://linkalternatifresmi.net', 'https://promodahsyat.biz',
            'https://gratisanmantap.xyz', 'https://spamlink1.com', 'https://spamdomain2.net', 'https://klikspam3.org',
            'https://infospam4.biz']
    bonus_offers = ['bonus new member 100%', 'cashback mingguan 10%', 'free spin tanpa deposit',
                    'jackpot puluhan juta rupiah', 'rollingan slot 1%', 'bonus referral seumur hidup',
                    'hadiah langsung tanpa diundi', 'bonus deposit harian', 'bonus turnover', 'extra bonus',
                    'hadiah kejutan', 'poin reward']
    promo_codes = ['diskonhemat50k', 'untungterus77', 'cobaingratisnow', 'hematmax2025', 'spesialhariini1',
                   'klaimbonus77', 'newuser100', 'gajianhemat', 'flashsale123', 'cashbackgila', 'promo123', 'bonus777',
                   'gratisongkir', 'kodeunik']
    discounts = ['50%', '100rb', 'ongkir gratis se-indonesia', 'cashback 50rb poin', 'potongan harga spesial member',
                 'beli 1 gratis 1', 'diskon 90%', 'harga coret', '70%', 'rp 50.000', 'gratis ongkir', 'potongan 20%']
    time_limit = ['hari ini saja', '24 jam ke depan', 'akhir pekan ini', 'bulan ini', '100 pelanggan pertama',
                  'sebelum jam 12 malam', 'selama persediaan masih ada', 'terbatas!', 'segera!', 'minggu ini',
                  'khusus hari ini']
    gibberishes = ['asdf qwer zxcv', 'lorem ipsum dolor sit amet consectetur adipiscing elit', '12345 abcde 67890',
                   'poiuytrewq lkjhgfdsamnbvcxz', 'bla bla bla testing komen',
                   'spam kata kunci murah bagus cepat terpercaya', 'dfgdfgdfgdfgdfg', 'hjkhkjhkhkjh', '9876543210',
                   'random text generator', 'spam spam spam', 'tes tes tes', 'coba coba coba']
    excessive_emojis = ['🔥🔥🔥🔥🔥', '😂😂😂😂😂', '👍👍👍👍👍', '💰💰💰💰💰', '🎉🎉🎉🎉🎉', '💯💯💯💯💯', '👇👇👇👇👇', '➡️➡️➡️➡️➡️', '✅✅✅✅✅',
                        '💸💸💸💸💸', '🎁🎁🎁🎁🎁', '🚀🚀🚀🚀🚀', '✨✨✨✨✨', '🚨🚨🚨🚨🚨', '🤑🤑🤑🤑🤑', '😱😱😱😱😱', '💥💥💥💥💥']
    spam_call_to_action = ['klik sekarang!', 'daftar gratis!', 'jangan sampai ketinggalan!', 'pesan sekarang!',
                           'download sekarang!', 'kunjungi website kami!', 'hubungi kami segera!', 'ambil bonusmu!',
                           'main sekarang!', 'beli sekarang juga!', 'cek link di bio!', 'swipe up!', 'klik disini!',
                           'info lengkap klik!']
    random_chars = ["hjkl;'[]", '1qaz2wsx3edc', '.,mnbvcxz', ')(*&^%$#@!', '!@#$%^&*()_+', '-------+++++',
                    '>>>>>>>><<<<<<<<', '~~~~~~```', '||||||\\\\\\', '******', '======']
    items = ['akun mobile legends sultan murah full skin', 'pulsa transfer telkomsel murah', 'pulsa transfer xl murah',
             'script web phising bank', 'script web phising sosmed', 'database nomor wa aktif',
             'akun netflix premium sharing murah', 'akun netflix premium private murah', 'voucher google play diskon',
             'voucher steam diskon', 'followers tiktok permanen bergaransi', 'akun genshin impact hoki',
             'akun honkai star rail hoki', 'obat kuat ilegal', 'produk kw super', 'software bajakan',
             'akun game ff sultan', 'akun ig centang biru', 'ebook premium gratis', 'film bajakan terbaru']
    item_condition = ['mulus no minus', 'baru segel', 'bergaransi resmi', 'bergaransi toko', 'legit no tipu',
                      'akun pribadi aman', 'bekas tapi berkualitas', 'seperti baru', 'grade a++', 'murah meriah',
                      'dijamin ori', 'work 100%']
    phone_numbers = ['0855-1234-5678', '0877-9876-5432', '0888-1122-3344', '6281312345678', '+6289876543210',
                     '081234567890', '0821-xxxx-xxxx', '0838-yyyy-yyyy', '628xxxxxxxx', '08xx-xxxx-xxxx']
    group_topics = ['trader saham pemula', 'trader crypto pemula', 'pencari kerja online remote',
                    'reseller baju import', 'dropship baju import', 'komunitas gamer sultan top up murah',
                    'info promo marketplace', 'info diskon marketplace', 'grup arisan online amanah',
                    'prediksi togel jitu', 'info slot gacor', 'grup jual beli akun game', 'komunitas pinjol ilegal',
                    'grup bokep viral', 'grup cheat game', 'grup investasi bodong']
    link_platforms = ['whatsapp', 'telegram', 'discord', 'facebook group', 'line group', 'kaskus', 'website forum']
    group_links = ['https://chat.whatsapp.com/abcdefghijklmnopqrstu', 'https://t.me/joinchat/fghij456uvwspam',
                   'https://discord.gg/klmno789pqrspam', 'https://facebook.com/groups/taribari',
                   'https://line.me/ti/g/kelas5', 'https://bit.ly/grupwaspam', 'https://s.id/telegrspam']
    random_phrase = ['apa kabar?', 'semoga berhasil ya.', 'iseng aja komen.', 'testing 123.', 'numpang lewat.',
                     'mantap.', 'ok.', 'halo.', 'tes.', 'spam.']
    app_names = ['mobile legends bang bang', 'spotify premium', 'netflix', 'whatsapp', 'gbwhatsapp', 'higgs domino rp',
                 'higgs domino n', 'youtube', 'tiktok', 'free fire max', 'picsart', 'canva pro', 'game populer',
                 'aplikasi edit foto', 'aplikasi x', 'aplikasi y', 'game z']
    spam_urls = ['https://apkmody.io/some-mod', 'https://revdl.com/some-hack', 'https://getmodsapk.com/some-unlocked',
                 'https://mediafire.com/downloadspam123', 'https://apkpure.vip/gamecheat', 'https://happymod.com/reg',
                 'https://liteapks.com/moddedapp', 'https://an1.com/spam-download', 'https://rexdl.com/hacked-app',
                 'https://bit.ly/modapkspam', 'https://s.id/downloadmodgratis', 'https://mediafire.com/spamfile',
                 'https://zippyshare.com/spamlink']
    investment_types = ['saham gorengan ipo', 'crypto micin potensial x1000', 'robot trading forex anti loss',
                        'investasi emas bodong', 'arisan online pasti dapat', 'investasi bodong skema ponzi',
                        'nft abal-abal', 'investasi properti fiktif', 'trading binary option', 'investasi titip dana',
                        'saham receh']
    url_invests = ['www.pastikaya.com', 'www.modalbalikcepat.net', 'www.investasibodong.org', 'www.cryptogratis.info',
                   'www.bisnismudah.co', 'www.joinmembervip.com', 'www.cuaninstan.xyz', 'www.profitkonsisten.biz',
                   'www.spamcrypto.com', 'www.investasicepat.net', 'www.danakaget.org']
    loan_types = ['pinjol ilegal tanpa ktp', 'pinjol ilegal tanpa verifikasi', 'pinjol bunga rendah 0%',
                  'gadai bpkb online', 'gadai sertifikat rumah online', 'pinjol syariah abal-abal',
                  'dana talangan cepat cair', 'pinjaman tanpa bi checking', 'kredit tanpa agunan palsu',
                  'pinjaman cepat cair 24 jam', 'pinjol data busuk', 'pinjaman mahasiswa']
    contact_or_links = ['wa 0899-5555-6666', 'klik link di bio ig @pinjol_amanah_ilegal',
                        'https://bit.ly/pinjolkilatcairnow',
                        'isi form di website kami: https://pinjolresmiabalabal.com',
                        'https://t.me/pinjolcepatcairadmin', 'https://wa.me/628spamloan', 'https://s.id/pinjol',
                        'https://pinjolcepat.com']
    repetitive_texts = ['spam spam spam', 'klik disini sekarang juga', 'murah murah murah banget',
                        'promo terbatas hari ini', 'gacor gacor gacor maxwin', 'wd pasti cair bosku', 'aman aman aman',
                        'terpercaya terpercaya', 'bonus bonus bonus', 'gratis gratis gratis', 'cepat cepat cepat',
                        'untung untung untung']
    account_types = ['ig olshop fashion', 'tiktok affiliate skincare', 'fanspage fb jualan elektronik',
                     'channel youtube gaming giveaway', 'akun twitter buzzer politik', 'akun bot komentar',
                     'profil palsu', 'akun judi online', 'akun pinjol', 'akun spam']
    account_names = ['@jualakunmurahid', '@viralkantiktokandajasa', 'infopromodiskonterbaruid', '@gamersultanindoshop',
                     '@buzzerpolitikrp_real', 'adminslotgacor', 'cs_pinjolresmi', 'promoterbaik_id', '@spamaccount123',
                     '@sellerterpercaya', '@adminspam']
    account_topic = ['fashion kpop terbaru', 'tips fyp tiktok', 'diskon gila shopee', 'diskon gila lazada',
                     'giveaway iphone', 'giveaway saldo dana', 'berita politik terkini', 'info slot gacor hari ini',
                     'prediksi togel akurat', 'lowongan kerja palsu', 'judi online', 'pinjaman online', 'barang murah',
                     'konten viral']
    prizes = ['iphone 15 pro max', 'motor nmax baru', 'motor pcx baru', 'uang tunai 10 juta rupiah',
              'liburan gratis ke bali', 'liburan gratis ke eropa', 'saldo e-wallet 1 juta', 'mobil agya baru',
              'mobil brio baru', 'emas batangan antam', 'voucher belanja 5 juta', 'laptop gaming', 'ps5',
              'umroh gratis']
    website_names = ['www.undianberhadiahresmi.com', 'www.menangmudah.net', 'www.judionlinepastiwd.com',
                     'www.gebyarhadiah.co', 'www.rodakeberuntungan77.cc', 'www.pemenangresmiundian.com',
                     'www.klaimhadianow.xyz', 'www.bonuskejutan.info', 'www.spamwinner.com', 'www.hadiahgratis.net',
                     'www.judispam.org']
    metrics = ['traffic website', 'traffic blog', 'engagement sosmed', 'ranking google halaman 1', 'jumlah followers',
               'jumlah subscriber', 'penjualan online shop', 'jumlah download', 'skor seo', 'rating aplikasi',
               'views video', 'likes postingan', 'komentar postingan']
    contact_emails = ['marketing@seojitu.com', 'admin@naikinfollower.biz', 'order@jasabacklinkmurah.org',
                      'support@globalservice.net', 'cs@gamingwebsite.com', 'info@spampromo.com',
                      'partnership@scamcorp.org', 'spamcontact@mail.com', 'admin@spamweb.net']
    stars = ['⭐⭐⭐⭐⭐', '🌟🌟🌟🌟🌟', '💯💯💯💯💯', '👍👍👍👍👍', '✨✨✨✨✨', '💎💎💎💎💎', '🏆🏆🏆🏆🏆']
    game_genres = ['rpg idle auto battle', 'arcade klasik tetris', 'arcade klasik pacman', 'puzzle santai match-3',
                   'slot online gacor', 'tembak ikan joker', 'game kartu domino', 'game kartu poker',
                   'game penghasil uang', 'game viral', 'moba', 'fps', 'rpg', 'casual']
    game_links = ['https://play.google.com/store/apps/details?id=com.game.penghasil.uang',
                  'https://bit.ly/gameuangnyata123', 'https://gamepenghasilcuan.net',
                  'https://downloadapkcheatgame.com', 'https://maindapatduit.co', 'https://gamemoney.xyz',
                  'https://linkdownloadgamegratis.com', 'https://s.id/gamecuan', 'https://gamehoki.com']
    goals = ['kaya mendadak tanpa kerja', 'dapat jodoh bule cantik', 'dapat jodoh bule ganteng',
             'bebas finansial sebelum umur 30', 'punya rumah mewah di pondok indah', 'keliling dunia gratis',
             'menang lotre', 'menang togel', 'jadi sultan', 'viral di tiktok', 'terkenal', 'sukses instan',
             'dapat uang mudah', 'hidup mewah']
    website_addresses = ['www.caricepatusaha.com', 'http://jodohimpian.online', 'http://solusikeuanganajaib.net',
                         'http://rahasiacepatkaya.org', 'https://impianmudah.co', 'https://suksesinstan.com',
                         'http://pastiberhasil.xyz', 'https://klikmenang.biz', 'www.spamsukses.com',
                         'www.caragampang.net', 'www.websitetipu.org']
    another_spam_phrase = ['jangan ragu lagi bosku', 'terbukti membayar member', 'aman 100% terpercaya',
                           'rahasia sukses', 'dijamin berhasil', 'kesempatan emas', 'promo gila', 'cuan terus',
                           'wd lancar', 'join sekarang!']
    phishing_link = ['http://bit.ly/update_akun_anda_sekarang', 'http://secure-login-bca-klik.com',
                     'http://verifikasi-otp-penting-bri.net', 'http://facebook-security-check.com',
                     'http://google-account-recovery-help.org', 'http://shopee-klaim-voucher.info',
                     'http://klikbca-secure.xyz', 'http://login-instagram-help.com',
                     'http://appleid-verification-support.net', 'http://paypal-resolve-issue-now.com',
                     'http:///verifikasibank', 'http://bit.do/loginspam', 'http://account-update-required.com']
    platform_names = ['exchange kripto palsu', 'bonus hunter 77', 'platform trading abal abal',
                      'agen slot terpercaya palsu', 'komunitas arisan online bodong', 'website judi resmi palsu',
                      'marketplace tipu tipu', 'layanan cloud storage gratis', 'aplikasi investasi bodong',
                      'situs phising', 'web judi ilegal', 'platform mlm']
    bonus_amount = ['$50 usdt gratis', 'rp 100.000 saldo awal', '1 eth gratis', 'mobil tesla', 'bonus deposit 200%',
                    'iphone 15 gratis', 'saldo dana 1 juta', 'poin reward 10000', 'rp 500.000', '$100 bonus',
                    'hadiah langsung', 'cashback 100%']
    registration_link = ['http://bit.ly/daftarspamplatform', 'http://s.id/registernowspam',
                         'https://spamplatform.com/register-now', 'www.klikdisinidaftar.com',
                         'http://join-exclusive.xyz', 'http://getbonusfree.net', 'http://daftarspam.com',
                         'http://registerbonus.net']
    skills = ['trading forex pasti profit', 'trading crypto pasti profit', 'digital marketing affiliate komisi besar',
              'bahasa inggris cepat 1 minggu', 'membuat website tanpa coding', 'membuat program tanpa coding',
              'hipnotis jarak jauh', 'gendam jarak jauh', 'jualan online laris manis', 'menjadi kaya raya instan',
              'membaca pikiran orang', 'skill dewa', 'rahasia sukses', 'cara cepat pintar']
    course_link = ['https://kelastradingpalsu.com/promo-vip', 'http://masterdigitalabal.net/free-ebook-download',
                   'http://englishcepatbodong.org/daftar-gratis', 'https://belajarwebsiteinstan.com/join',
                   'http://rahasiasuksesonline.net', 'http://skilldewa.xyz', 'http://kursusinstan.biz',
                   'http://s.id/kelass', 'http://bit.ly/kursusbodong', 'http://belajarr.com']
    single_word_spams = ['promo', 'gratis', 'diskon', 'klik', 'daftar', 'murah', 'cepat', 'untung', 'gacor', 'bonus',
                         'jackpot', 'menang', 'terbaik', 'viral', 'mantap', 'oke', 'spam', 'tes', 'coba', 'hot', 'new',
                         'sale']
    product_category = ['gadget terbaru iphone', 'gadget terbaru samsung', 'fashion wanita import korea',
                        'skincare viral bpom palsu', 'peralatan rumah tangga unik china', 'obat kuat herbal',
                        'suplemen pelangsing', 'barang kw super', 'produk ilegal', 'makanan/minuman ajaib',
                        'elektronik murah', 'kosmetik abal-abal', 'aksesoris gaming', 'mainan anak']
    ecommerce_link = ['http://shopee.co.id/rikseller123', 'https://tokopedia.com/mema-official',
                      'http://lazada.co.id/kura-store', 'https://bukalapak.com/primaliga',
                      'https://blibli.com/diskonbajubaru', 'https://jdid.com/komputeristop',
                      'http://tiktok.shop/keripikkuning', 'http://s.id/shoelash', 'http://bit.ly/kulkul',
                      'http://spammart.com']
    movie_genre = ['film horor indonesia terbaru', 'action barat full movie', 'anime jepang sub indo',
                   'drama korea romantis populer', 'film india bollywood', 'film semi ilegal', 'film viral no sensor',
                   'box office terbaru', 'film bioskop gratis', 'download film hd', 'streaming anime',
                   'drakor sub indo']
    streaming_link = ['http://lk21.uno', 'http://rebahin.life', 'http://bioskopkeren.cyou', 'http://indoxxi.cam',
                      'http://dutafilm.buzz', 'http://terbit21.lol', 'http://nontonspamgratis.xyz',
                      'http://streamingviral.net', 'http://bit.ly/nontonspam', 'http://s.id/filmspam',
                      'http://bioskopspam.com']
    health_product = ['obat pelangsing herbal alami', 'obat kuat pria tahan lama', 'pemutih kulit ampuh permanen',
                      'peninggi badan cepat terbukti', 'obat diabetes mujarab', 'obat kolesterol mujarab',
                      'obat kanker ajaib', 'suplemen kecerdasan otak', 'obat jerawat ampuh', 'vitamin c dosis tinggi',
                      'obat herbal x']
    disease = ['segala macam penyakit', 'diabetes', 'kolesterol tinggi', 'jerawat parah', 'ejakulasi dini', 'kanker',
               'obesitas', 'kebotakan', 'penuaan dini', 'asam urat', 'stroke', 'jantung', 'covid-19']
    whatsapp_number = ['https://wa.me/6281234567890', '089876543210', '+6287711223344', '62855-2434-5677',
                       'https://wa.me/6282442343', '0843-4334-4343']
    job_title = ['admin online shop gaji tinggi', 'data entry remote kerja dari rumah', 'customer service wfh mudah',
                 'reseller tanpa modal untung besar', 'investor saham palsu', 'model',
                 'kerja ketik captcha dibayar dollar', 'lowongan cpns palsu', 'kerja online mudah',
                 'freelance gaji besar', 'lowongan kerja bodong']
    salary_range = ['5-10 juta per bulan', '100rb-500rb per hari', 'gaji umr jakarta', 'komisi besar puluhan juta',
                    'gaji dollar', 'gaji fantastis', 'penghasilan tak terbatas', 'di atas 10 juta', 'gaji nego',
                    'sesuai target']
    job_email = ['hrd@perusahaanpalsu-loker.com', 'lokerbodong@gmail.com', 'karir@spamcorp-global.net',
                 'rekrutmen@agenscam.com', 'jobvacancy.spam@outlook.com', 'spamjob@mail.com', 'lokerpalsu@spam.net']
    fake_prize = ['voucher belanja 1 juta', 'hp samsung s24 ultra', 'mobil agya baru', 'mobil brio baru',
                  'paket umroh gratis', 'uang tunai 50 juta', 'emas 100 gram', 'liburan ke eropa gratis', 'iphone 16',
                  'motor vario', 'rumah mewah', 'saldo dana 10 juta']
    scam_link = ['http://bit.ly/klaimhadiahspam123', 'http://hadiahkejutan-resmi.com',
                 'http://pemenang-undian-bankxyz.com', 'www.selamatandamenang.net', 'http://klikhadiah.info',
                 'http://undiansuper.xyz', 'https://giftforyou.biz', 'http://s.id/hadiahspam', 'http://klaimspam.com',
                 'http://pemenangspam.net']
    social_media_metric = ['followers ig', 'followers tiktok', 'views tiktok', 'views reels', 'views youtube',
                           'subscriber youtube', 'like facebook', 'comment facebook', 'share facebook',
                           'engagement rate', 'verified badge', 'followers twitter', 'likes tiktok', 'views story ig']
    social_media_service = ['tambah followers aktif', 'tambah followers pasif', 'jasa like buzzer',
                            'jasa comment buzzer', 'beli jam tayang youtube monetisasi', 'jasa centang biru ilegal',
                            'jasa unbanned akun', 'jasa hack akun', 'jasa view live ig', 'jasa auto like',
                            'jasa followers murah']
    contact_ig = ['@jasasosmedmurah_id', '@naikinfollowers_amanah', '@rajaviral_official_id', '@buzzer_service_pro',
                  '@spamsosmedking', '@verifiedmurah', '@igspamfollower', '@adminsosmedspam', '@jualfollowerspam']
    financial_service = ['pinjaman dana tunai cepat cair', 'kartu kredit tanpa survey', 'kartu kredit tanpa slip gaji',
                         'investasi aman profit tinggi', 'jasa gestun', 'jasa gesek tunai', 'jasa pencairan paylater',
                         'jasa pembuatan rekening palsu', 'dana hibah', 'modal usaha tanpa jaminan',
                         'kredit hp tanpa dp']
    website_finance = ['danacepat-ilegal.com', 'kartukreditinstan-scam.com', 'investasipastiprofit-tipu.net',
                       'solusikeuangan-bodong.org', 'pinjolmudah.xyz', 'creditcardmagic.biz', 'spamfinance.com',
                       'danaspam.net', 'pinjolspam.org']
    service_name = ['gojek', 'shopee', 'tokopedia', 'dana', 'ovo', 'grab', 'netflix', 'spotify', 'bibit', 'ajaib',
                    'bca mobile', 'brimo', "mandiri livin'", 'facebook', 'instagram', 'google', 'apple id', 'akulaku',
                    'kredivo', 'mytelkomsel', 'myxl', 'paypal', 'steam', 'microsoft account', 'bank x', 'e-wallet y']
    game_name = ['mobile legends', 'free fire', 'pubg mobile', 'higgs domino', 'roblox', 'genshin impact',
                 'clash of clans', 'pokemon go', 'valorant', 'steam wallet', 'call of duty', 'honkai star rail',
                 'game online x', 'game y']
    in_game_currency = ['diamond', 'uc', 'koin emas', 'robux', 'primogem', 'gems', 'pokecoin', 'vp',
                        'steam wallet code', 'chip domino', 'cash game', 'gold', 'point']
    transport_service = ['gojek', 'grab', 'maxim', 'bluebird', 'ojek online', 'taksi online', 'travel antar kota',
                         'sewa mobil', 'angkutan umum']
    hyperbole_negative_adj = ['terburuk', 'ngaco', 'hancur banget', 'sangat parah', 'gak masuk akal', 'gak layak pakai',
                              'bikin trauma', 'lebay tapi zonk', 'sampah', 'ampas', 'payah', 'kacau balau',
                              'menyesatkan']
    hyperbole_adj = ['terbaik', 'tercanggih', 'terhebat', 'paling ampuh', 'nomor 1', 'tak tertandingi', 'luar biasa',
                     'ajaib', 'revolusioner', 'tercepat', 'termurah', 'paling menguntungkan', 'sempurna', 'fantastis',
                     'ultimate', 'dewa', 'gila', 'mantap jiwa']
    hyperbole_noun = ['solusi', 'produk', 'layanan', 'metode', 'rahasia', 'cara', 'platform', 'alat', 'teknik',
                      'strategi', 'aplikasi', 'game', 'website', 'jasa']
    hyperbole_guarantee = ['pasti berhasil', 'dijamin sukses 100%', 'anti gagal', 'hasil instan',
                           'profit ribuan persen', 'hidupmu berubah drastis', 'pasti kaya', 'dijamin manjur',
                           'langsung work', 'auto sultan']
    hyperbole_comment = ['semua masalahmu hilang seketika', 'kamu akan jadi sultan', 'tidak akan pernah menyesal',
                         'ini yang kamu butuhkan', 'semua orang wajib punya', 'wajib coba sekarang',
                         'rugi kalau gak pakai', 'the best pokoknya', 'gak ada obat!']
    negative_assumption = ['iri', 'tidak paham teknologi', 'gaptek', 'belum coba aja', 'dibayar kompetitor',
                           'sirik tanda tak mampu', 'gak ngerti kualitas', 'haters', 'otak udang']
    short_time_promise = ['1 menit', '5 menit', '1 hari', 'sekejap mata', 'hitungan detik', 'langsung', 'instan',
                          'hari ini juga', 'sekarang juga', 'cepat kilat']
    malware_link = ['http://bit.ly/update_penting_os', 'http://s.id/download_security_patch',
                    'https://penting-system-update.com/file.exe', 'http://fix-device-error-now.net/patch.apk',
                    'http://download-virus-cleaner.com', 'www.security-update-android.apk', 'https://klikdisini.com']
    fake_lottery_name = ['undian nasional resmi', 'gebyar hadiah bank xyz', 'lotere internasional megamillions',
                         'program berhadiah shopee/tokopedia', 'undian berhadiah whatsapp', 'lotre facebook',
                         'google rewards']
    viral_topic = ['video skandal artis', 'rekaman cctv kejadian aneh', 'bocoran rahasia pemerintah',
                   'penampakan makhluk misterius', 'video lucu viral', 'berita hoax viral', 'kontroversi terbaru',
                   'gosip panas']
    simple_task = ['klik iklan', 'nonton video', 'isi survei', 'main game', 'undang teman', 'download aplikasi',
                   'baca artikel', 'share postingan', 'jawab kuis']
    pyramid_scheme_link = ['https://bisnisdarirumahmudah.com/join', 'https://passiveincome-real.net/register',
                           'https://jadikaya-cepat.org/member-area', 'https://mlmsukses.xyz', 'https://bisnisspam.com',
                           'https://gabungmlm.net', 'https://kayabareng.org']
    illegal_item = ['narkoba jenis baru', 'senjata api rakitan', 'dokumen palsu', 'data pribadi curian', 'akun curian',
                    'software bajakan', 'film ilegal', 'barang selundupan', 'hewan langka']
    social_media_platform = ['instagram', 'facebook', 'tiktok', 'twitter', 'whatsapp', 'youtube', 'telegram',
                             'linkedin']
    premium_service = ['netflix', 'spotify', 'youtube premium', 'canva pro', 'vpn premium', 'microsoft 365', 'disney+',
                       'hbo go', 'adobe creative cloud', 'zoom premium']
    payment_method_unofficial = ['pulsa', 'transfer bank pribadi', 'e-wallet non-resmi', 'saldo game', 'voucher game',
                                 'barter barang']
    version_number = ['1.2.3', '5.0.1', '2024.1', '3.5', '6.10', '7.0', '2.2.1', 'terbaru', 'kemarin', 'beta', 'alpha',
                      '10.5.2', 'versi 2023', 'build 101', 'v.8.8', 'patch terbaru', 'pro', 'vip', 'unlocked']

    generated_count = 0
    existing_spams = set()
    while generated_count < count:
        template = random.choice(templates)
        try:
            replacements = {
                'hyperbole_guarantee_upper': random.choice(hyperbole_guarantee_upper),
                'hyperbole_negative_adj_upper': random.choice(hyperbole_negative_adj_upper),
                'hyperbole_adj_upper': random.choice(hyperbole_adj_upper),
                'single_word_spam_upper': random.choice(single_word_spam_upper),
                'repetitive_text_upper': random.choice(repetitive_text_upper),
                'guarantee_upper': random.choice(guarantee_upper),
                'spam_call_to_action_upper': random.choice(spam_call_to_action_upper),
                'famous_game': random.choice(famous_game),
                'service': random.choice(services),
                'contact_info': random.choice(contact_infos),
                'guarantee': random.choice(guarantees),
                'benefit': random.choice(benefits),
                'username_socmeds': random.choice(username_socmeds),
                'spam_url_short': random.choice(spam_url_short),
                'topic': random.choice(topics),
                'url': random.choice(urls),
                'bonus_offer': random.choice(bonus_offers),
                'promo_code': random.choice(promo_codes),
                'discount': random.choice(discounts),
                'time_limit': random.choice(time_limit),
                'gibberish': random.choice(gibberishes),
                'excessive_emojis': random.choice(excessive_emojis),
                'spam_call_to_action': random.choice(spam_call_to_action),
                'random_chars': random.choice(random_chars),
                'item': random.choice(items),
                'item_condition': random.choice(item_condition),
                'phone_number': random.choice(phone_numbers),
                'group_topic': random.choice(group_topics),
                'link_platform': random.choice(link_platforms),
                'group_link': random.choice(group_links),
                'random_phrase': random.choice(random_phrase),
                'app_name': random.choice(app_names),
                'spam_url': random.choice(spam_urls),
                'investment_type': random.choice(investment_types),
                'url_invest': random.choice(url_invests),
                'loan_type': random.choice(loan_types),
                'contact_or_link': random.choice(contact_or_links),
                'repetitive_text': random.choice(repetitive_texts),
                'account_type': random.choice(account_types),
                'account_name': random.choice(account_names),
                'account_topic': random.choice(account_topic),
                'prize': random.choice(prizes),
                'website_name': random.choice(website_names),
                'metric': random.choice(metrics),
                'contact_email': random.choice(contact_emails),
                'stars': random.choice(stars),
                'game_genre': random.choice(game_genres),
                'game_link': random.choice(game_links),
                'goal': random.choice(goals),
                'website_address': random.choice(website_addresses),
                'another_spam_phrase': random.choice(another_spam_phrase),
                'phishing_link': random.choice(phishing_link),
                'platform_name': random.choice(platform_names),
                'bonus_amount': random.choice(bonus_amount),
                'registration_link': random.choice(registration_link),
                'skill': random.choice(skills),
                'course_link': random.choice(course_link),
                'single_word_spam': random.choice(single_word_spams),
                'product_category': random.choice(product_category),
                'ecommerce_link': random.choice(ecommerce_link),
                'movie_genre': random.choice(movie_genre),
                'streaming_link': random.choice(streaming_link),
                'health_product': random.choice(health_product),
                'disease': random.choice(disease),
                'whatsapp_number': random.choice(whatsapp_number),
                'job_title': random.choice(job_title),
                'salary_range': random.choice(salary_range),
                'job_email': random.choice(job_email),
                'fake_prize': random.choice(fake_prize),
                'scam_link': random.choice(scam_link),
                'social_media_metric': random.choice(social_media_metric),
                'social_media_service': random.choice(social_media_service),
                'contact_ig': random.choice(contact_ig),
                'financial_service': random.choice(financial_service),
                'website_finance': random.choice(website_finance),
                'service_name': random.choice(service_name),
                'game_name': random.choice(game_name),
                'in_game_currency': random.choice(in_game_currency),
                'transport_service': random.choice(transport_service),
                # --- Added for Hyperbole ---
                'hyperbole_adj': random.choice(hyperbole_adj),
                'hyperbole_negative_adj': random.choice(hyperbole_negative_adj),
                'hyperbole_noun': random.choice(hyperbole_noun),
                'app_category': random.choice(app_category), # Use existing list
                'hyperbole_guarantee': random.choice(hyperbole_guarantee),
                'hyperbole_comment': random.choice(hyperbole_comment),
                'negative_assumption': random.choice(negative_assumption),
                'short_time_promise': random.choice(short_time_promise),
                # --- Added for More Spam Variations ---
                'malware_link': random.choice(malware_link),
                'fake_lottery_name': random.choice(fake_lottery_name),
                'viral_topic': random.choice(viral_topic),
                'simple_task': random.choice(simple_task),
                'pyramid_scheme_link': random.choice(pyramid_scheme_link),
                'illegal_item': random.choice(illegal_item),
                'social_media_platform': random.choice(social_media_platform),
                'premium_service': random.choice(premium_service),
                'payment_method_unofficial': random.choice(payment_method_unofficial),
                'version_number': random.choice(version_number), # Added
            }

            valid_replacements = {k: v for k, v in replacements.items() if f"{{{k}}}" in template}
            spam = template
            processed_keys = set()
            for k, v in valid_replacements.items():
                 if k not in processed_keys:
                     spam = spam.replace(f"{{{k}}}", v)
                     processed_keys.add(k)

            spam = spam.strip()

            # Ensure spam is meaningful and not already generated
            # Increased minimum length slightly for spam to avoid overly short, less characteristic spam
            if spam and len(spam) > 10 and spam not in existing_spams: # Adjusted min length
                spams.append((spam, 2)) # Label 2 for explicit spam
                existing_spams.add(spam)
                generated_count += 1
        except KeyError as e:
            # print(f"Warning: KeyError {e} in template: '{template}' with replacements {valid_replacements}")
            pass
        except Exception as e:
            # print(f"Error generating spam with template '{template}': {e}")
            pass

    return spams

# --- Main Execution ---

# Define filename
# Using the same filename as the previous correct version
# Make sure this path is correct relative to where you run the script
# Using '../data/main_dataset/' assumes the script is run from a directory
# one level below the 'data' directory (e.g., from a 'scripts' folder)
# Adjust if necessary.
# Updated filename to v4 to reflect new changes
csv_filename = "../data/main_dataset/dataset_spam_nlp_v5.csv"

# Get the directory where the script is located
# Handle case where __file__ might not be defined (e.g., interactive environment)
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()

# Construct the full path, ensuring the directory exists
csv_filepath = os.path.join(script_dir, csv_filename)
output_dir = os.path.dirname(csv_filepath)

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    print(f"Creating directory: {output_dir}")
    os.makedirs(output_dir)


# Define target counts per label (approximate)
target_total = 15000 # Increased target count further for more data
count_per_label = target_total // 3
# Adjust slightly to get closer to the target
count_genuine = count_per_label
count_irrelevant = count_per_label
count_spam = count_per_label + (target_total % 3) # Give spam the remainder

print(f"Generating review data (Target: ~{target_total} reviews)...")
print(f"- Genuine (Label 0): Target {count_genuine}")
print(f"- Irrelevant (Label 1): Target {count_irrelevant}")
print(f"- Spam (Label 2): Target {count_spam}")


# Generate data for each label
genuine_reviews = generate_genuine_reviews(count_genuine)
irrelevant_content = generate_irrelevant_content(count_irrelevant)
explicit_spam = generate_explicit_spam(count_spam)

# Combine all data
all_data = genuine_reviews + irrelevant_content + explicit_spam
random.shuffle(all_data) # Shuffle the combined data

print(f"\nGenerated {len(genuine_reviews)} genuine reviews.")
print(f"Generated {len(irrelevant_content)} irrelevant content entries.")
print(f"Generated {len(explicit_spam)} explicit spam entries.")
print(f"Total generated entries: {len(all_data)}")


print(f"\nSaving data to {csv_filepath}...")

try:
    # Write data to CSV file
    # Use 'utf-8' encoding for broader character support
    # Use csv.QUOTE_NONNUMERIC to quote only fields that are not numbers (int, float)
    with open(csv_filepath, 'w', newline='', encoding='utf-8') as output_file:
        # Use doublequote=True (default) to handle quotes inside strings properly
        # Keep using QUOTE_NONNUMERIC as it correctly handles text vs numbers
        writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
        # Write header - Headers are strings, so they will be quoted by QUOTE_NONNUMERIC
        writer.writerow(['ulasan', 'kategori']) # Standard header
        # Write data rows (list of tuples)
        # Ensure labels are integers so QUOTE_NONNUMERIC works correctly
        writer.writerows(all_data)
    print(f"Successfully saved {len(all_data)} entries to {csv_filepath}")

except IOError as e:
    print(f"Error saving file: {e}")
except Exception as e:
    print(f"An unexpected error occurred during saving: {e}")
