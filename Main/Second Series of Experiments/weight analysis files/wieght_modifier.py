import cv2
import os

# Fixed variables
image_path = r"font_50_control.png"
output_folder = "weight_test_images_v3"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the image in grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# Convert the image to black and white using Otsu's binarization
_, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# First loop: Dilation
for kernel_size in range(1, 9):  
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    dilated_image = cv2.dilate(binary_image, kernel, iterations=1)
    
    # Save the dilated image
    output_path = os.path.join(output_folder, f"weight_-{kernel_size}_50.png")
    cv2.imwrite(output_path, dilated_image)

# Second loop: Erosion
for kernel_size in range(1, 41):  # Kernel sizes from 1 to 7
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    eroded_image = cv2.erode(binary_image, kernel, iterations=1)
    
    # Save the eroded image
    output_path = os.path.join(output_folder, f"weight_{kernel_size}_50.png")
    cv2.imwrite(output_path, eroded_image)

print(f"Processing complete. Images are saved in the '{output_folder}' folder.")
