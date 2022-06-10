# -*- coding: utf-8 -*-
"""citra original to segmentasi citra inversi rgb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kqiGpvZ3QeZtZMmYPak6Kip8ZxMzqM7D

C. Citra Original to citra inversi RGB

1. kita harus memanggil library python package yang di perlukan dengan cara    
mengimportkan library python package nya
"""

import numpy as np
import imageio
import matplotlib.pyplot as plt

"""2. masukkan kode untuk memasukkan citra original terlebih dahulu"""

citra_asli = imageio.imread("didi2.png")

plt.imshow(citra_asli)
plt.title("citra original")
plt.show()

"""3. selanjutnya masukkan kode segmentasi citra digital yang kita inginkan, di sini saya memakai segmentasi citra digital metode inversi grayscale dan inversi rgb"""

# membaca gambar

img = imageio.imread("didi2.png")

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

# membuat variabel versi dari gambar

img_inversi = np.zeros(img.shape, dtype=np.uint8)

#membuat fungsi untuk metode inversi rgb
 
def inversi_rgb(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red = nilai - red
            green = img[y][x][1]
            green = nilai - green
            blue = img[y][x][2]
            blue = nilai - blue
            img_inversi[y][x] = (red, green, blue)

# menampilkan hasil inversi RGB
inversi_rgb(255)
plt.imshow(img_inversi)
plt.title("inversi rgb")
plt.show()