from Slant_image import TextSlanter


slant_value = -60
image_name = f"{slant_value}_Slant.png"

# Define input and output image paths
input_image_path = "Control_Image.png"

# Create an instance of TextItalicizer
slanter = TextSlanter(input_image_path, "temp")

# For a negative slant
slanter.output_image_path = image_name
slanter.italicize_text(slant_value)