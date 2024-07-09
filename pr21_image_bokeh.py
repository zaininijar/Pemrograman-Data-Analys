from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk membaca gambar menggunakan Pillow


def read_image_pillow(file_path):
    image = Image.open(file_path)
    return image


# Fungsi untuk menyimpan gambar menggunakan Pillow


def save_image_pillow(image, file_path):
    image.save(file_path)


# Fungsi untuk mengonversi gambar ke skala abu-abu menggunakan OpenCV

# image = read_image_pillow('images/image.png')


def convert_to_grayscale(image):
    image_array = np.array(image)
    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    return Image.fromarray(gray_image)


# new_image = convert_to_grayscale(image)
# save_image_pillow(new_image, 'images/results/grayscale.png')

# Fungsi untuk menerapkan filter Gaussian menggunakan OpenCV

# image = read_image_pillow('images/image.png')


def apply_gaussian_blur(image, kernel_size=(15, 15)):
    image_array = np.array(image)
    blurred_image = cv2.GaussianBlur(image_array, kernel_size, 0)
    return Image.fromarray(blurred_image)


# new_image = apply_gaussian_blur(image)
# save_image_pillow(new_image, 'images/results/gaussionblur.png')

# Fungsi untuk membuat mask untuk objek utama

image = cv2.imread('images/image.png')


def create_mask(image, rect):
    mask = np.zeros(image.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    cv2.grabCut(image, mask, rect, bgdModel,
                fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)
    image = image * mask2[:, :, np.newaxis]

    return image, mask2


image_mask, new_mask = create_mask(image, rect=(0, 0, 0, 0))
new_image = image_mask * new_mask
save_image_pillow(new_image, 'images/results/mask.png')

# Fungsi untuk menggabungkan objek utama dengan latar belakang blur


def apply_bokeh_effect(image, mask, blurred_bg):
    mask = np.stack([mask] * 3, axis=-1)  # Convert to 3-channel mask
    return np.where(mask == 0, blurred_bg, image)

# Fungi untuk menampilkan gambar-gambar menggunakan matplotlib


def display_images(original, gray, bokeh):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0]. imshow(original)
    axes[0]. set_title('Original Image')
    axes[0].axis('off')
