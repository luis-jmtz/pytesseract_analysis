import cv2
import numpy as np

def thicken_text_preserving_space(input_image_path, output_image_path, thickness):
    """
    Thickens the characters in a black-text-on-white-background image
    while preserving the relative white space between the characters.
    
    Args:
        input_image_path (str): The file path to the input image.
        output_image_path (str): The file path to save the output image.
        thickness (int): The number of pixels to thicken the edges of the characters.
    """
    # Read the image in grayscale
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found at {input_image_path}")
    
    # Ensure the image has black text on a white background
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    # Perform dilation to thicken the text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (thickness, thickness))
    thickened_image = cv2.dilate(binary_image, kernel, iterations=1)

    # Combine the thickened image with the original to preserve white space
    combined_image = cv2.bitwise_and(thickened_image, binary_image)
    
    # Invert back to white background with black text
    result_image = cv2.bitwise_not(combined_image)

    # Save the output image
    cv2.imwrite(output_image_path, result_image)
    print(f"Output image saved at {output_image_path}")

# Example usage:
# Provide the input image path, output image path, and the thickness in pixels
input_path = "Tesseract_Test_Image2.png"  # Replace with your image path
output_path = "output_imagev2-1.png"  # Replace with desired output path
thickness = 5  # Adjust the thickness as needed

thicken_text_preserving_space(input_path, output_path, thickness)
