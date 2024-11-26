from Slant_image import TextSlanter

# Define input and output image paths
input_image_path = "Control_Image.png"
output_image_path_positive = "positive_slant.png"

# Create an instance of TextItalicizer
italicizer = TextSlanter(input_image_path, output_image_path_positive)

# Apply a positive slant
italicizer.italicize_text(slant_factor=20)

# For a negative slant
italicizer.output_image_path = "negative_slant.png"
italicizer.italicize_text(slant_factor=-20)