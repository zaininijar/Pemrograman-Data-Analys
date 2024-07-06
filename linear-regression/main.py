import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
luas_bangunan = np.array([50, 60, 70, 80, 90, 100]).reshape((-1, 1))
harga_rumah = np.array([300, 340, 380, 420, 460, 500])

# Membuat model regresi linear
model = LinearRegression()
model.fit(luas_bangunan, harga_rumah)

# Menghitung parameter
b1 = model.coef_[0]
b0 = model.intercept_

print(f"Slope (b1): {b1}")
print(f"Intercept (b0): {b0}")

# Prediksi harga rumah untuk luas bangunan tertentu
luas_bangunan_baru = np.array([85]).reshape((-1, 1))
prediksi_harga = model.predict(luas_bangunan_baru)
print(f"Prediksi harga rumah untuk luas bangunan 85 m²: {prediksi_harga[0]} juta")

# Plot data dan garis regresi
plt.scatter(luas_bangunan, harga_rumah, color='blue')
plt.plot(luas_bangunan, model.predict(luas_bangunan), color='red')
plt.xlabel('Luas Bangunan (m²)')
plt.ylabel('Harga Rumah (juta)')
plt.title('Regresi Linear: Prediksi Harga Rumah')
plt.show()
