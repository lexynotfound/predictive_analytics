# 📊 Model Predictive Analytics Report

## 📝 **Pendahuluan**
E-commerce saat ini berkembang pesat, dan memahami perilaku pengunjung situs web menjadi sangat penting dalam meningkatkan strategi pemasaran serta meningkatkan tingkat konversi penjualan. Dalam proyek ini, kami akan membangun model **Predictive Analytics** untuk memprediksi apakah seorang pengunjung situs e-commerce akan melakukan pembelian berdasarkan perilaku mereka di situs web.

## 📂 **Domain Proyek**
Dalam dunia bisnis e-commerce, **menganalisis perilaku pengunjung** sangat krusial untuk meningkatkan tingkat konversi penjualan. Banyak pengunjung yang hanya melihat-lihat produk tanpa melakukan transaksi. Dengan memanfaatkan data yang tersedia, kita bisa membangun **model prediktif** untuk mengetahui pengunjung mana yang kemungkinan besar akan melakukan pembelian.

- **Masalah utama:** Banyak pengunjung yang tidak melakukan pembelian meskipun sudah mengunjungi beberapa halaman produk.
- **Dampak bisnis:** Dengan mengetahui pola pengunjung yang berpotensi membeli, strategi pemasaran dapat lebih terarah.
- **Solusi:** Menggunakan model machine learning untuk mengklasifikasikan pengunjung ke dalam dua kategori: yang akan membeli dan yang tidak.

## 🔧 **Business Understanding**

### **Problem Statement**
E-commerce ingin mengetahui **peluang pengunjung melakukan pembelian** berdasarkan perilaku mereka di situs web.

### **Goals**
- Mengembangkan model klasifikasi yang mampu memprediksi apakah pengunjung akan melakukan pembelian atau tidak.
- Memberikan insights kepada tim pemasaran agar dapat menargetkan pengunjung yang memiliki potensi tinggi untuk membeli produk.
- Meningkatkan **konversi penjualan** dengan strategi pemasaran yang lebih terarah.

## 📂 **Dataset**
Dataset yang digunakan adalah **Online Shoppers Purchasing Intention Dataset** yang diambil dari Kaggle. [Link Dataset](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset)

**Deskripsi Dataset:**
- **Jumlah Data:** 12.330 baris, 18 kolom
- **Jumlah Fitur:** 17 fitur prediktor, 1 fitur target (`Revenue`)
- **Fitur Utama:**
  - `Administrative`, `Informational`, `ProductRelated`: Jumlah halaman yang dikunjungi.
  - `BounceRates`, `ExitRates`: Persentase pengunjung yang meninggalkan situs setelah melihat satu halaman.
  - `SpecialDay`: Indikator kedekatan dengan hari spesial.
  - `Month`, `VisitorType`, `Weekend`: Informasi tentang waktu kunjungan dan jenis pengunjung.
  - `Revenue` (Target): Apakah pengunjung melakukan pembelian atau tidak.

## 🔧 **Data Preparation**
- **Mengisi Missing Values** pada kolom numerik dengan rata-rata.
- **Menghapus Duplikasi Data** untuk menghindari bias.
- **Encoding variabel kategorikal** (`Month`, `VisitorType`, `Weekend`) dengan one-hot encoding.
- **Standarisasi fitur numerik** menggunakan `StandardScaler`.
- **Membagi dataset** menjadi training (80%) dan testing (20%).

## 🤖 **Model Development**
- **Algoritma yang digunakan:** Random Forest Classifier
- **Parameter utama:** `n_estimators=100`
- **Alasan pemilihan:** Random Forest memberikan akurasi tinggi dan lebih tahan terhadap overfitting dibanding model decision tree tunggal.

## 📊 **Evaluation**
Hasil evaluasi model:

| Metrik        | Nilai |
|--------------|-------|
| Akurasi      | 87.5% |
| Precision    | 85.3% |
| Recall       | 82.9% |
| F1-Score     | 84.1% |

- **Confusion Matrix:**
![Confusion Matrix](https://github.com/user-attachments/assets/80f302fe-fe59-4258-82a8-c8c38d885907)

## 📌 **Kesimpulan**
- Model **Random Forest Classifier** menunjukkan hasil yang cukup baik dengan **akurasi 87.5%**.
- Model ini dapat digunakan oleh bisnis e-commerce untuk **mengidentifikasi pelanggan potensial** yang memiliki kemungkinan tinggi untuk melakukan pembelian.
- Dapat dilakukan **penyesuaian hyperparameter** untuk meningkatkan performa model lebih lanjut.

## 🔮 **Saran untuk Pengembangan Lebih Lanjut**
- **Menggunakan model ensemble lain** seperti Gradient Boosting atau XGBoost untuk melihat apakah hasil bisa lebih baik.
- **Melakukan Feature Engineering lebih lanjut** untuk meningkatkan performa model.
- **Menganalisis lebih dalam variabel yang paling berpengaruh** terhadap keputusan pembelian pelanggan.

🚀 **Model siap digunakan untuk analisis bisnis dan optimasi strategi pemasaran e-commerce!**