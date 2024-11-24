from PIL import Image
import numpy as np

# Input file path
image_path = "Control_Image.png"

# Load the image
image = Image.open(image_path)

# Convert the image to black and white (1-bit pixels, black and white)
bw_image = image.convert("1")

# Save the black and white image as a bitmap
bitmap_path = "Control_Image.bmp"
bw_image.save(bitmap_path, format="BMP")
print(f"Bitmap saved to {bitmap_path}")

# Convert the bitmap to a matrix
# 0 for black, 1 for white
matrix = np.array(bw_image, dtype=int)

# Save the matrix as a file
matrix_path = "Control_Image_Matrix.txt"
np.savetxt(matrix_path, matrix, fmt='%d')
print(f"Matrix saved to {matrix_path}")

# Debug print (optional)
print("Matrix preview:")
print(matrix)
