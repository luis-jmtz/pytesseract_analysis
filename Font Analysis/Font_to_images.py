import os
from PIL import Image, ImageDraw, ImageFont

def create_char_images(font_path, output_dir, image_size=(64, 64), font_size=48):
    """
    Create images for each alphanumeric character using the given font.
    
    :param font_path: Path to the .ttf font file
    :param output_dir: Directory where character images will be saved
    :param image_size: Size of the output images (width, height)
    :param font_size: Size of the font to render the characters
    """
    # Characters to generate (alphanumeric)
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    # Create the font object
    font = ImageFont.truetype(font_path, font_size)
    
    # Loop through each character and create an image
    for char in characters:
        # Create a blank image with white background
        image = Image.new("RGB", image_size, "white")
        draw = ImageDraw.Draw(image)
        
        # Get text size to center it in the image
        text_width, text_height = draw.textsize(char, font=font)
        text_x = (image_size[0] - text_width) / 2
        text_y = (image_size[1] - text_height) / 2
        
        # Draw the character on the image
        draw.text((text_x, text_y), char, font=font, fill="black")
        
        # Save the image in the output directory
        image_path = os.path.join(output_dir, f"{char}.png")
        image.save(image_path)

def generate_images_for_fonts(fonts_folder, output_base_folder):
    """
    Loop through each .ttf font in the given folder and generate images for alphanumeric characters.
    
    :param fonts_folder: Directory containing .ttf font files
    :param output_base_folder: Base directory to save the generated images
    """
    # Loop through each file in the fonts folder
    for font_filename in os.listdir(fonts_folder):
        if font_filename.endswith(".ttf"):
            font_path = os.path.join(fonts_folder, font_filename)
            font_name = os.path.splitext(font_filename)[0]
            
            # Create an output directory for each font
            output_dir = os.path.join(output_base_folder, font_name)
            os.makedirs(output_dir, exist_ok=True)
            
            print(f"Generating images for font: {font_name}")
            create_char_images(font_path, output_dir)

# Specify the path to the folder containing .ttf fonts and the output directory
fonts_folder = "path/to/fonts_folder"  # replace with the path to your fonts folder
output_base_folder = "path/to/output_folder"  # replace with the path to save images

# Run the script
generate_images_for_fonts(fonts_folder, output_base_folder)
