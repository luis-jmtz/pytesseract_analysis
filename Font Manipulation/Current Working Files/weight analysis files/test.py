import cv2
import numpy as np

# Load the image in grayscale
image_path = "Control_Image.png"  # Replace with your image file
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# Binarize the image (convert to black and white)
_, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Get the dimensions of the image
height, width = binary_image.shape

# Initialize variables for thickness calculation
total_thickness = 0
line_count = 0

# Iterate through each row (horizontal scan)
for row in range(height):
    line_started = False
    line_thickness = 0

    for col in range(width):
        # Check if the current pixel is part of a black line
        if binary_image[row, col] == 255:  # Black pixel
            if not line_started:
                line_started = True  # Start of a new line
                line_thickness = 1
            else:
                line_thickness += 1  # Increment the thickness for the current line
        else:
            if line_started:
                # End of a line, add thickness to total
                total_thickness += line_thickness
                line_count += 1
                line_started = False  # Reset for the next line

    # Handle a line that ends at the end of the row
    if line_started:
        total_thickness += line_thickness
        line_count += 1

# Calculate the average line thickness
if line_count > 0:
    average_thickness = total_thickness / line_count
else:
    average_thickness = 0  # No lines found

print(f"Average Line Thickness: {average_thickness}")









# import cv2
# import numpy as np

# # Load the image in grayscale
# image_path = 'Control_Image.png'  # Adjust this path to your image
# image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# # Ensure the image loads successfully
# if image is None:
#     raise FileNotFoundError(f"Image not found at {image_path}")

# # Convert to binary (black text on white background)
# _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)

# # Define a circular kernel for thickening
# kernel_size = 1 # Adjust the size for more or less thickening
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))

# # Apply dilation to thicken the lines
# thickened_image = cv2.dilate(binary_image, kernel, iterations=1)

# # Convert back to original color scheme (black letters on white background)
# thickened_image = cv2.bitwise_not(thickened_image)

# # Save the result
# output_path = 'kernel1.png'
# cv2.imwrite(output_path, thickened_image)

# output_path
