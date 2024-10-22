import cv2

# pemanggilan gambar 
img = cv2.imread(r"C:\Users\USER\Downloads\WhatsApp Image 2024-09-24 at 20.18.34.jpeg") 

# Ubah ukuran menjadi 500x500 piksel
img = cv2.resize(img, (500, 500))

# Tentukan sudut rotasi (misal, 45 derajat)
angle = 45

# Dapatkan dimensi gambar
rows, cols = img.shape[:2]

# Hitung matriks rotasi
M = cv2.getRotationMatrix2D((cols/2,rows/2), angle, 1)
print("Matriks Rotasi:")
print(M)

# Terapkan rotasi pada gambar
dst = cv2.warpAffine(img, M, (cols, rows))

# Tampilkan gambar hasil rotasi
cv2.imshow('Rotated Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()