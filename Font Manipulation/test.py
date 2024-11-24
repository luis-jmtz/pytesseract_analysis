from PIL import Image

def italicize_text_in_image(input_image_path, output_image_path, top_left, bottom_right):
    """
    Italicize the text in an image by skewing the area of the image containing the text.

    :param input_image_path: Path to the input image.
    :param output_image_path: Path to save the output image.
    :param top_left: Tuple (x1, y1) representing the top-left corner of the text region.
    :param bottom_right: Tuple (x2, y2) representing the bottom-right corner of the text region.
    """
    # Open the image
    image = Image.open(input_image_path)

    # Calculate width and height from coordinates
    x1, y1 = top_left
    x2, y2 = bottom_right
    width = x2 - x1
    height = y2 - y1

    # Crop the text area
    text_area = image.crop((x1, y1, x2, y2))

    # Apply affine transformation to skew the text area
    skew_matrix = (1, -0.3, 0, 0, 1, 0)  # Skew matrix for italic effect
    italicized_text_area = text_area.transform(
        text_area.size, 
        Image.AFFINE, 
        skew_matrix, 
        resample=Image.BICUBIC
    )

    # Paste the transformed text area back onto the original image
    image.paste(italicized_text_area, (x1, y1))

    # Save the modified image
    image.save(output_image_path)

# Example usage
input_image_path = "Control_Image.png"  # Path to your input image
output_image_path = "output_image_with_italic_text.png"  # Path to save the output image
top_left = (192, 240)  # Top-left coordinates of the text region
bottom_right = (307, 261)  # Bottom-right coordinates of the text region

# Apply the transformation
italicize_text_in_image(input_image_path, output_image_path, top_left, bottom_right)
