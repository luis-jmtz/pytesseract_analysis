from PIL import Image, ImageChops, ImageDraw

def italicize_text_in_image_no_artifacts_fixed(input_image_path, output_image_path, top_left, bottom_right):
    """
    Italicize the text in an image by skewing the area of the image containing the text.
    Dynamically fills artifacts with the background color sampled from the surrounding area.

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

    # Add padding to the width to accommodate the skew
    padding = int(height * 0.3)  # Calculate padding based on skew factor (-0.3)
    padded_width = width + padding

    # Crop the text area with extra padding
    text_area = image.crop((x1, y1, x2 + padding, y2))

    # Dynamically sample the background color from the surrounding area of the text
    surrounding_area = image.crop((x1 - 5, y1 - 5, x2 + 5, y2 + 5))
    background_color = surrounding_area.getpixel((0, 0))  # Sample the top-left pixel of the surrounding area

    # Create a new background for the text area to avoid artifacts
    text_area_with_background = Image.new("RGB", (padded_width, height), background_color)
    text_area_with_background.paste(text_area, (0, 0))

    # Apply affine transformation to skew the text area
    skew_matrix = (1, -0.3, 0, 0, 1, 0)  # Skew matrix for italic effect
    italicized_text_area = text_area_with_background.transform(
        (padded_width, height),
        Image.AFFINE,
        skew_matrix,
        resample=Image.BICUBIC
    )

    # Blend the skewed text area back onto the original image
    final_text_area = Image.new("RGB", image.size, background_color)
    final_text_area.paste(italicized_text_area, (x1, y1))

    # Merge the transformed text area with the original image
    final_image = ImageChops.add(final_text_area, image)

    # Save the modified image
    final_image.save(output_image_path)

# Example usage
input_image_path = "Control_Image.png"  # Path to your input image
output_image_path = "output5.png"  # Path to save the output image
top_left = (192, 240)  # Top-left coordinates of the text region
bottom_right = (307, 261)  # Bottom-right coordinates of the text region

# Apply the transformation
italicize_text_in_image_no_artifacts_fixed(input_image_path, output_image_path, top_left, bottom_right)
