from Slant_image import TextSlanter

slant_value = -65
input_image_path = "Control_Image.png"
slanter = TextSlanter(input_image_path, "temp")

image_name = fr"Slanted_Images\{slant_value}_Slant.png"
slanter.output_image_path = image_name
slanter.italicize_text(slant_value)


# while slant_value < 61:
#     image_name = fr"Slanted_Images\{slant_value}_Slant.png"
#     slanter.output_image_path = image_name
#     slanter.italicize_text(slant_value)
#     slant_value += 1