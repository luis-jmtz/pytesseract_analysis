from jpeg_to_png import toPNG
from up_saturater import saturateColor
from upscaler import upscaleImage
from to_BnW import imageBnW
from morph_images import morph_processor


image_path = r"color_note.jpeg"

#gets base name of file
base_name = image_path.split('.')[0]

print(base_name)

try:
    converter = toPNG(image_path)
    # Convert to PNG if it is a JPEG
    converter.convert_to_png()
    print("toPNG Successful")
    print(f"New Image: {base_name}.png")
except ValueError:
    print("toPNG Failure")
    
png_path = fr"PNG_images\{base_name}.png"

try:
    saturator = saturateColor(png_path)
    # Increase saturation by the hard-coded factor (1.5)
    saturator.increase_saturation()
    print("Saturation increase successful")
except ValueError as e:
    print(f"Saturation adjustment failed: {e}")

saturated_path = fr"Saturated_Images\{base_name}_saturated.png"

try:
    upscaler = upscaleImage(saturated_path, base_name)
    # Upscale the image by the hard-coded factor (1.5)
    upscaler.upscale_image()
    print("Image upscaling successful")
except ValueError as e:
    print(f"Image upscaling failed: {e}")
    

upscaled_path = fr"Upscaled_Images\{base_name}_upscaled.png"


try:
    bnw_converter = imageBnW(upscaled_path, base_name)
    # Convert to black and white using Otsu's binarization
    bnw_converter.convert_to_bnw()
    print("Black and white conversion successful")
except ValueError as e:
    print(f"Black and white conversion failed: {e}")
    

BnW_image_path = fr"BnW_Images\{base_name}_BnW.png"

try:
    morpher = morph_processor(BnW_image_path, base_name)
    # Apply morphological opening and closing
    morpher.apply_morphology()
    print("Morphological processing successful")
except ValueError as e:
    print(f"Morphological processing failed: {e}")
