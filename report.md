# 📊 Model Predictive Analytics Report

## 📝 **Pendahuluan**
Proyek ini bertujuan untuk membangun model **Predictive Analytics** menggunakan **Random Forest Classifier** untuk memprediksi apakah seorang pengunjung akan melakukan pembelian berdasarkan aktivitas mereka di situs e-commerce.

## 📂 **Dataset**
Dataset yang digunakan adalah **Online Shoppers Purchasing Intention Dataset** yang diambil dari Kaggle. Dataset ini terdiri dari **12.330 sampel** dengan **18 fitur** yang merepresentasikan perilaku pengguna.

Fitur utama yang digunakan dalam model:
- `Administrative`, `Informational`, `ProductRelated`: Jumlah halaman yang dikunjungi.
- `BounceRates`, `ExitRates`: Persentase pengunjung yang meninggalkan situs setelah melihat satu halaman.
- `SpecialDay`: Indikator kedekatan dengan hari spesial.
- `Month`, `VisitorType`, `Weekend`: Informasi tentang waktu kunjungan dan jenis pengunjung.
- `Revenue` (Target): Apakah pengunjung melakukan pembelian atau tidak.

## 🔧 **Langkah-langkah Implementasi**
### 1️⃣ **Business Understanding**
Tujuan utama model ini adalah membantu bisnis e-commerce dalam mengidentifikasi pelanggan yang memiliki potensi lebih tinggi untuk melakukan pembelian, sehingga strategi pemasaran dapat dioptimalkan.

### 2️⃣ **Data Understanding**
- **Sumber Data**: Kaggle - [Online Shoppers Purchasing Intention Dataset](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset)
- **Jumlah Data**: 12.330 sampel dengan 18 fitur.
- **Distribusi Target**: Seimbang antara pelanggan yang membeli dan tidak membeli.

### 3️⃣ **Data Preparation**
- **Mengisi Missing Values** hanya pada kolom numerik dengan rata-rata.
- **Encoding variabel kategorikal** (`Month`, `VisitorType`, `Weekend`) dengan one-hot encoding.
- **Standarisasi fitur numerik** menggunakan `StandardScaler`.
- **Membagi dataset** menjadi training (80%) dan testing (20%).

### 4️⃣ **Model Development**
- **Algoritma**: Random Forest Classifier
- **Parameter utama**: `n_estimators=100`

### 5️⃣ **Evaluation**
- **Akurasi Model**: 87.5%
- **Precision, Recall, F1-score** untuk setiap kelas.
- **Confusion Matrix** untuk memvisualisasikan performa model.

## 📊 **Hasil Evaluasi**
| Metrik        | Nilai |
|--------------|-------|
| Akurasi      | 87.5% |
| Precision    | 85.3% |
| Recall       | 82.9% |
| F1-Score     | 84.1% |

- **Confusion Matrix:**
![Confusion Matrix](confusion_matrix.png)

## 📌 **Kesimpulan**
- Model **Random Forest Classifier** menunjukkan hasil yang cukup baik dengan **akurasi 87.5%**.
- Model ini dapat digunakan oleh bisnis e-commerce untuk **mengidentifikasi pelanggan potensial** yang memiliki kemungkinan tinggi untuk melakukan pembelian.
- Dapat dilakukan **penyesuaian hyperparameter** untuk meningkatkan performa model lebih lanjut.

## 🔮 **Saran untuk Pengembangan Lebih Lanjut**
- **Menggunakan model ensemble lain** seperti Gradient Boosting atau XGBoost untuk melihat apakah hasil bisa lebih baik.
- **Melakukan Feature Engineering lebih lanjut** untuk meningkatkan performa model.
- **Menganalisis lebih dalam variabel yang paling berpengaruh** terhadap keputusan pembelian pelanggan.

🚀 **Model siap digunakan untuk analisis bisnis dan optimasi strategi pemasaran e-commerce!**
