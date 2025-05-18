import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Contoh dataset dummy (bisa diganti dengan data asli)
data = {
    'waktu': [8, 9, 17, 14, 18, 7, 12, 15, 19, 20],
    'hari': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu', 'Senin', 'Selasa', 'Rabu'],
    'cuaca': ['Cerah', 'Hujan', 'Cerah', 'Mendung', 'Hujan', 'Cerah', 'Cerah', 'Hujan', 'Mendung', 'Cerah'],
    'volume_kendaraan': [80, 95, 110, 70, 120, 60, 55, 90, 100, 75],
    'kemacetan': ['Ya', 'Ya', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Tidak']
}

df = pd.DataFrame(data)

# Encode data kategori
df_encoded = pd.get_dummies(df, columns=['hari', 'cuaca'])

# Pisahkan fitur dan target
X = df_encoded.drop('kemacetan', axis=1)
y = df['kemacetan']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model Decision Tree
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = model.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Visualisasi pohon keputusan
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=X.columns, class_names=['Tidak', 'Ya'], filled=True)
plt.title("Model Decision Tree untuk Prediksi Kemacetan")
plt.show()
