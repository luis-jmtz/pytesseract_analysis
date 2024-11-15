from jpeg_to_png import toPNG

image_path = r"eng_AF_003.jpg"

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