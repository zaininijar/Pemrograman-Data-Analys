```markdown
# Contoh Kasus: Prediksi Harga Rumah dengan Regresi Linear

## Deskripsi Kasus

Kamu ingin memprediksi harga rumah berdasarkan luas bangunan.

## Data

Kamu memiliki dataset yang berisi informasi tentang harga rumah dan luas bangunan. Data ini disajikan dalam bentuk tabel dengan dua kolom: `luas_bangunan` (dalam meter persegi) dan `harga_rumah` (dalam jutaan rupiah).

| luas_bangunan (m²) | harga_rumah (juta) |
| ------------------ | ------------------ |
| 50                 | 300                |
| 60                 | 340                |
| 70                 | 380                |
| 80                 | 420                |
| 90                 | 460                |
| 100                | 500                |

## Langkah-langkah

### 1. Mempersiapkan Data

Kita akan memisahkan data menjadi dua variabel: `X` untuk luas bangunan dan `Y` untuk harga rumah.

### 2. Menghitung Parameter Regresi

Kita akan menghitung nilai slope (`b1`) dan intercept (`b0`) menggunakan rumus regresi linear:
```

b1 = (n(ΣXY) - (ΣX)(ΣY)) / (n(ΣX^2) - (ΣX)^2)
b0 = (ΣY - b1(ΣX)) / n

```

### 3. Membuat Model
Menggunakan parameter yang telah dihitung untuk membuat model regresi linear:
```

Ŷ = b0 + b1 \* X

````

### 4. Prediksi
Menggunakan model tersebut untuk memprediksi harga rumah berdasarkan luas bangunan yang diberikan.

## Implementasi dengan Python
Mari kita implementasikan contoh ini dengan Python untuk menghitung parameter regresi dan membuat prediksi.

```python
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
````

### Output

- Slope (`b1`) akan memberikan kemiringan garis regresi.
- Intercept (`b0`) akan memberikan titik potong dengan sumbu Y.
- Prediksi harga rumah untuk luas bangunan 85 m².

Plot akan menampilkan data asli sebagai titik biru dan garis regresi sebagai garis merah.

## Kesimpulan

Dengan menggunakan regresi linear, kita dapat memprediksi harga rumah berdasarkan luas bangunan. Model yang dibuat menggunakan data sampel dapat digunakan untuk estimasi harga rumah baru dengan luas tertentu.

```

Dokumentasi di atas menjelaskan langkah-langkah untuk memprediksi harga rumah menggunakan regresi linear beserta contoh implementasinya dengan Python.
```
