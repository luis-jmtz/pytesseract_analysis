from Slant_image import TextSlanter


slant_value = -60
image_name = f"{slant_value}.png"

# Define input and output image paths
input_image_path = "Control_Image.png"

# Create an instance of TextItalicizer
italicizer = TextSlanter(input_image_path, image_name)

# Apply a positive slant
italicizer.italicize_text(slant_factor=slant_value)

# For a negative slant
italicizer.output_image_path = "negative_slant.png"
italicizer.italicize_text(slant_factor=-20)