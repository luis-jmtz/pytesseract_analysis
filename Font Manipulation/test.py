from PIL import Image

def italicize_text_in_image_fixed(input_image_path, output_image_path, top_left, bottom_right):

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

    # Apply affine transformation to skew the text area
    skew_matrix = (1, -0.3, 0, 0, 1, 0)  # Skew matrix for italic effect
    italicized_text_area = text_area.transform(
        (padded_width, height), 
        Image.AFFINE, 
        skew_matrix, 
        resample=Image.BICUBIC
    )

    # Paste the transformed text area back onto the original image
    # Shift the paste position to align the top-left corner of the skewed text
    image.paste(italicized_text_area, (x1, y1))

    # Save the modified image
    image.save(output_image_path)

# Example usage
input_image_path = "Control_Image.png"  # Path to your input image
output_image_path = "output_image_with_italic_text_fixed2.png"  # Path to save the output image
top_left = (192, 240)  # Top-left coordinates of the text region
bottom_right = (307, 261)  # Bottom-right coordinates of the text region

# Apply the transformation
italicize_text_in_image_fixed(input_image_path, output_image_path, top_left, bottom_right)
