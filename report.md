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
1. **Data Preprocessing**
   - Mengisi **missing values** pada kolom numerik dengan rata-rata.
   - One-hot encoding untuk variabel kategorikal seperti `Month`, `VisitorType`, dan `Weekend`.
   - Standarisasi fitur numerik agar skala data seragam.

2. **Splitting Dataset**
   - Dataset dibagi menjadi **80% training** dan **20% testing**.

3. **Pelatihan Model**
   - Menggunakan **Random Forest Classifier** dengan `n_estimators=100`.

4. **Evaluasi Model**
   - Metrik yang digunakan:
     - **Akurasi**: Menunjukkan sejauh mana model dapat mengklasifikasikan data dengan benar.
     - **Precision, Recall, dan F1-score**: Memberikan insight terkait prediksi kelas positif dan negatif.
     - **Confusion Matrix**: Memvisualisasikan performa model dalam mengklasifikasikan data.

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

