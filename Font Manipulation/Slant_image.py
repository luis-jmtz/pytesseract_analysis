from PIL import Image

class TextSlanter:
    def __init__(self, input_image_path, output_image_path):
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path

        # Hard-coded coordinates for the text region
        self.top_left = (0, 240)  # Top-left coordinates of the text region
        self.bottom_right = (500, 261)  # Bottom-right coordinates of the text region

    def italicize_text(self, slant_factor):
        # Open the image
        image = Image.open(self.input_image_path)

        # Extract coordinates and dimensions
        x1, y1 = self.top_left
        x2, y2 = self.bottom_right
        width = x2 - x1
        height = y2 - y1

        # Calculate padding based on slant factor
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

        # Calculate offset to re-center the text
        offset = int((padding * skew_value) / 2)
        if slant_factor > 0:
            paste_x1 = crop_x1 - offset  # Shift left for positive slant
        else:
            paste_x1 = crop_x1 + offset  # Shift right for negative slant

        # Paste the transformed text area back onto the original image
        image.paste(italicized_text_area, (paste_x1, y1))

        # Save the modified image
        image.save(self.output_image_path)
        print(f"Saved slanted image with slant factor {slant_factor} to {self.output_image_path}")
