import cv2
import numpy as np

# Load the image in grayscale
image_path = 'Control_Image.png'  # Adjust this path to your image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Ensure the image loads successfully
if image is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# Convert to binary (black text on white background)
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)

# Define a circular kernel for thickening
kernel_size = 1 # Adjust the size for more or less thickening
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))

# Apply dilation to thicken the lines
thickened_image = cv2.dilate(binary_image, kernel, iterations=1)

# Convert back to original color scheme (black letters on white background)
thickened_image = cv2.bitwise_not(thickened_image)

# Save the result
output_path = 'kernel1.png'
cv2.imwrite(output_path, thickened_image)

output_path
