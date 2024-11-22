import cv2
import os

def apply_erosion(image_path, output_path="eroded_image.jpg", iterations=1):
    """
    Applies erosion to the input image and saves the result as a new image.

    :param image_path: Path to the input image.
    :param output_path: Path to save the eroded image.
    :param iterations: Number of iterations for the erosion. Fewer iterations mean less erosion.
    """
    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image. Please ensure it's a valid image file.")
        return

    # Create a 3x3 kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

    # Apply erosion with the specified number of iterations
    eroded_image = cv2.erode(image, kernel, iterations=iterations)

    # Save the resulting image
    cv2.imwrite(output_path, eroded_image)
    print(f"Eroded image saved at: {output_path}")


input_image_path = "Tesseract_Test_Image.png"
apply_erosion(input_image_path, "eroded_image7.png", iterations=7)