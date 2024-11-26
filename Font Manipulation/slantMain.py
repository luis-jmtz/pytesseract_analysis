from Slant_image import TextSlanter

slant_value = -60
#Slanted_Images\Control_Image.png
image_name = fr"Slanted_Images\{slant_value}_Slant.png"

# Define input and output image paths
input_image_path = "Control_Image.png"

slanter = TextSlanter(input_image_path, "temp")


slanter.output_image_path = image_name
slanter.italicize_text(slant_value)