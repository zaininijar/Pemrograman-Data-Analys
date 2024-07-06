# Contoh Kasus: Prediksi Harga Rumah dengan Regresi Linear

## Deskripsi Kasus

Kamu ingin memprediksi harga rumah berdasarkan luas bangunan.

## Data

Kamu memiliki dataset yang berisi informasi tentang harga rumah dan luas bangunan. Data ini disajikan dalam bentuk tabel dengan dua kolom: `luas_bangunan` (dalam meter persegi) dan `harga_rumah` (dalam jutaan rupiah).

```markdown
| luas_bangunan (m²) | harga_rumah (juta) |
| ------------------ | ------------------ |
| 50                 | 300                |
| 60                 | 340                |
| 70                 | 380                |
| 80                 | 420                |
| 90                 | 460                |
| 100                | 500                |
```

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
```

### 4. Prediksi

Menggunakan model tersebut untuk memprediksi harga rumah berdasarkan luas bangunan yang diberikan.

### Output

- Slope (`b1`) akan memberikan kemiringan garis regresi.
- Intercept (`b0`) akan memberikan titik potong dengan sumbu Y.
- Prediksi harga rumah untuk luas bangunan 85 m².

Plot akan menampilkan data asli sebagai titik biru dan garis regresi sebagai garis merah.

## Kesimpulan

Dengan menggunakan regresi linear, kita dapat memprediksi harga rumah berdasarkan luas bangunan. Model yang dibuat menggunakan data sampel dapat digunakan untuk estimasi harga rumah baru dengan luas tertentu.
