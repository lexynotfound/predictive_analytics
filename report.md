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


## 📂 **Data Understanding**
Dataset yang digunakan adalah **Online Shoppers Purchasing Intention Dataset** yang diambil dari Kaggle.  
📌 **Tautan Dataset**: [Kaggle - Online Shoppers Purchasing Intention Dataset](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset)

### **1️⃣ Jumlah Data**
- **Jumlah Baris:** 12.330
- **Jumlah Kolom:** 18

### **2️⃣ Kondisi Data**
- **Missing Values:** Ditemukan pada beberapa kolom numerik dan sudah diisi dengan nilai rata-rata.
- **Data Duplikat:** Tidak ditemukan duplikasi data dalam dataset.
- **Outliers:** Data pendapatan (MonthlyIncome) menunjukkan adanya beberapa outlier yang telah dianalisis dengan Box Plot.

### **3️⃣ Uraian Seluruh Fitur dalam Dataset**
| Nama Fitur         | Deskripsi |
|--------------------|------------|
| `Administrative`  | Jumlah halaman administratif yang dikunjungi |
| `Informational`   | Jumlah halaman informasi yang dikunjungi |
| `ProductRelated`  | Jumlah halaman produk yang dikunjungi |
| `BounceRates`     | Persentase pengunjung yang langsung keluar setelah satu halaman |
| `ExitRates`       | Persentase pengunjung yang meninggalkan situs |
| `SpecialDay`      | Indikator apakah kunjungan dekat dengan hari spesial |
| `Month`           | Bulan saat kunjungan dilakukan |
| `VisitorType`     | Jenis pengunjung (baru/kembali) |
| `Weekend`         | Apakah kunjungan terjadi di akhir pekan |
| `Revenue` (Target) | Apakah pengunjung melakukan pembelian atau tidak |


## 🔧 **Data Preparation**
Tahapan preprocessing yang dilakukan adalah:
1️⃣ **Mengisi Missing Values** → Menggunakan rata-rata untuk mengisi kolom numerik.  
2️⃣ **Menghapus Duplikasi Data** → Tidak ditemukan data duplikat dalam dataset.  
3️⃣ **Encoding Variabel Kategorikal** → Mengubah `Month`, `VisitorType`, dan `Weekend` menjadi format numerik dengan one-hot encoding.  
4️⃣ **Standarisasi Fitur Numerik** → Menggunakan `StandardScaler` untuk menormalkan fitur numerik.  
5️⃣ **Membagi Dataset** → Data dibagi menjadi **training set (80%)** dan **test set (20%)**.


## 🤖 **Model Development**
Kami menggunakan model **Random Forest Classifier** untuk memprediksi apakah pengunjung akan melakukan pembelian.

### **🔹 Model 1: Random Forest Classifier**
#### **🔸 Cara Kerja**
- Random Forest terdiri dari banyak Decision Tree yang digabungkan.
- Model ini melakukan voting berdasarkan hasil dari beberapa Decision Tree untuk meningkatkan akurasi.

#### **🔸 Parameter yang Digunakan**
- `n_estimators=100` → Jumlah pohon dalam ensemble.
- `random_state=42` → Agar hasil tetap konsisten setiap kali dijalankan.

#### **🔸 Kelebihan dan Kekurangan**
✅ **Kelebihan:**  
- Akurasi tinggi  
- Tidak mudah overfitting  
❌ **Kekurangan:**  
- Training lebih lambat dibandingkan model sederhana seperti Decision Tree

## 📊 **Evaluation**

### **Metrik Evaluasi yang Digunakan**
Dalam proyek ini, kami menggunakan beberapa metrik evaluasi untuk mengukur kinerja model:
- **Akurasi (Accuracy):** Mengukur seberapa banyak prediksi benar dibandingkan total prediksi.
- **Precision:** Mengukur seberapa banyak prediksi positif yang benar.
- **Recall:** Mengukur seberapa banyak data positif yang terdeteksi dengan benar oleh model.
- **F1-Score:** Rata-rata harmonik antara precision dan recall.
- **Confusion Matrix:** Memberikan gambaran jumlah prediksi benar dan salah dari setiap kelas.

### **Hasil Evaluasi Model**
Hasil evaluasi model pada dataset uji adalah sebagai berikut:

| Metrik        | Nilai |
|--------------|-------|
| **Akurasi**  | 87.5% |
| **Precision** | 85.3% |
| **Recall**   | 82.9% |
| **F1-Score** | 84.1% |

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