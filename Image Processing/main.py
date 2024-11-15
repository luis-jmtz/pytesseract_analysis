from jpeg_to_png import toPNG
from up_saturater import saturateColor

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
    
png_path = f"{base_name}.png"

try:
    saturator = saturateColor(png_path)
    # Increase saturation by the hard-coded factor (1.5)
    saturator.increase_saturation()
    print("Saturation increase successful")
except ValueError as e:
    print(f"Saturation adjustment failed: {e}")
