import os
from PIL import Image, ImageDraw, ImageFont

def create_char_images(font_path, output_dir, image_size=(128, 160), font_size=96):
    """
    Create images for each alphanumeric character (upper and lowercase) using the given font.
    
    :param font_path: Path to the .ttf font file
    :param output_dir: Directory where character images will be saved
    :param image_size: Size of the output images (width, height)
    :param font_size: Size of the font to render the characters
    """
    # Characters to generate (upper and lower case alphanumeric)
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    # Create the font object
    font = ImageFont.truetype(font_path, font_size)
    
    # Get the font ascent and descent (for vertical alignment adjustments)
    ascent, descent = font.getmetrics()
    
    # Loop through each character and create an image
    for char in characters:
        # Create a blank image with white background
        image = Image.new("RGB", image_size, "white")
        draw = ImageDraw.Draw(image)
        
        # Get text bounding box to calculate exact positioning
        bbox = draw.textbbox((0, 0), char, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Center the character horizontally, adjust vertically based on font metrics
        text_x = (image_size[0] - text_width) / 2
        text_y = (image_size[1] - text_height) / 2 - descent / 2
        
        # Draw the character on the image
        draw.text((text_x, text_y), char, font=font, fill="black")
        
        # Save the image in the output directory
        image_path = os.path.join(output_dir, f"{char}.png")
        image.save(image_path)

def generate_images_for_fonts(fonts_folder, output_base_folder):
    """
    Loop through each .ttf font in the given folder and generate images for upper and lowercase alphanumeric characters.
    
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
fonts_folder = r"Low Accuracy Fonts"  # Path to fonts folder
output_base_folder = r"low_acc_Font_Image_Folder"  # Path to save images

# Run the script
generate_images_for_fonts(fonts_folder, output_base_folder)
