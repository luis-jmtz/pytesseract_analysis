from PIL import Image

def italicize_text_in_image_with_proper_padding(input_image_path, output_image_path, top_left, bottom_right, slant_factor):
    # Open the image
    image = Image.open(input_image_path)

    # Calculate width and height from coordinates
    x1, y1 = top_left
    x2, y2 = bottom_right
    width = x2 - x1
    height = y2 - y1

    # Calculate padding based on slant factor and height
    padding = int(abs(slant_factor))  # Padding is proportional to the absolute value of slant factor
    padded_width = width + 2 * padding  # Add padding to both sides of the cropped width

    # Adjust cropping to include extra padding on both sides
    crop_x1 = max(0, x1 - padding)
    crop_x2 = min(image.width, x2 + padding)

    # Crop the text area with extra padding
    text_area = image.crop((crop_x1, y1, crop_x2, y2))

    # Calculate skew matrix based on the slant factor
    skew_value = slant_factor / height  # Normalize slant_factor based on text height
    skew_matrix = (1, skew_value, -padding * skew_value, 0, 1, 0)

    # Apply affine transformation to skew the text area
    italicized_text_area = text_area.transform(
        (padded_width, height),
        Image.AFFINE,
        skew_matrix,
        resample=Image.BICUBIC
    )

    # Create a new blank image to overlay the modified text
    result_image = image.copy()
    result_image.paste(italicized_text_area, (crop_x1, y1), italicized_text_area)

    # Save the modified image
    result_image.save(output_image_path)

# Example usage
input_image_path = "Control_Image.png"  # Path to your input image
output_image_path_positive = "positive_slant.png"  # Positive slant output
output_image_path_negative = "negative_slant.png"  # Negative slant output
top_left = (192, 240)  # Top-left coordinates of the text region
bottom_right = (307, 261)  # Bottom-right coordinates of the text region

# Apply the transformation
slant_factor_positive = 20  # Positive slant
slant_factor_negative = -20  # Negative slant

# Positive slant
italicize_text_in_image_with_proper_padding(
    input_image_path, output_image_path_positive, top_left, bottom_right, slant_factor_positive
)

# Negative slant
italicize_text_in_image_with_proper_padding(
    input_image_path, output_image_path_negative, top_left, bottom_right, slant_factor_negative
)
