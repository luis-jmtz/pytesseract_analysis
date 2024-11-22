import cv2
import numpy as np

def thicken_text(input_image_path, output_image_path, thickness):

    # Read the image in grayscale
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found at {input_image_path}")
    
    # Ensure the image has black text on a white background
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Use dilation to thicken the text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (thickness, thickness))
    thickened_image = cv2.dilate(binary_image, kernel, iterations=1)
    
    # Invert the image back to white background and black text
    thickened_image = cv2.bitwise_not(thickened_image)
    
    # Save the output image
    cv2.imwrite(output_image_path, thickened_image)
    print(f"Output image saved at {output_image_path}")

# Example usage:
# Provide the input image path, output image path, and the thickness in pixels
input_path = "Tesseract_Test_Image2.png"  # Replace with your image path
output_path = "output_image2.png"  # Replace with desired output path
thickness = 5  # Adjust the thickness as needed

thicken_text(input_path, output_path, thickness)
