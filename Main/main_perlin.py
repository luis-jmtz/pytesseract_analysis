from perlin_generator import perlinNoiser

# Initialize and process the image
processor = perlinNoiser(
    input_image_path="Control_Image.png",
    intensity=0.5,
    output_image_path="output.png"
)
processor.process_image()