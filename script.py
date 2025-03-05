import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 📌 Download dataset from Kaggle
path = kagglehub.dataset_download("imakash3011/online-shoppers-purchasing-intention-dataset")
print("Path to dataset files:", path)

# 📌 Load Dataset
df = pd.read_csv(f"{path}/online_shoppers_intention.csv")
print("Jumlah data:", len(df))

# 📌 Data Preparation
# Mengisi missing values hanya untuk kolom numerik
df.fillna(df.select_dtypes(include=np.number).mean(), inplace=True)

# One-hot encoding untuk variabel kategorikal
categorical_features = ['Month', 'VisitorType', 'Weekend']
df = pd.get_dummies(df, columns=categorical_features, drop_first=True)

# Memisahkan fitur dan label
X = df.drop(columns=['Revenue'])
y = df['Revenue'].astype(int)

# Membagi dataset menjadi training set dan test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standarisasi fitur numerik
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 📌 Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 📌 Evaluasi Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"✅ Akurasi Model: {accuracy:.2%}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 📌 Confusion Matrix
plt.figure(figsize=(8,6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', xticklabels=['No Purchase', 'Purchase'], yticklabels=['No Purchase', 'Purchase'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
