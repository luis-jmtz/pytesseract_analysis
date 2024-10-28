from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import os

# Define file paths
input_file_path = r"data_set_builder\input.txt"  # Path to the input text file
fonts_folder_path = r"data_set_builder\Google_Handwritten_Fonts"  # Path to the folder containing font files
output_image_folder = r"data_set_builder\Handwritten Font Images"  # Folder to save the output images

# Create the output directory if it doesn't exist
os.makedirs(output_image_folder, exist_ok=True)

# Load text from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Create a new image for each font
width, height = 800, 600  # Adjust dimensions as needed
line_height = 20  # Adjust line height

# Loop through all font files in the specified folder
for font_file in os.listdir(fonts_folder_path):
    if font_file.lower().endswith(('.ttf', '.otf')):  # Check for font file types
        font_path = os.path.join(fonts_folder_path, font_file)
        
        # Create a new image
        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)
        
        # Load the font
        try:
            font = ImageFont.truetype(font_path, 16)  # You can change the font size here
        except IOError:
            print(f"Could not load font: {font_file}")
            continue  # Skip to the next font if there's an error

        # Set the starting position for the text
        x, y = 10, 10

        # Wrap text and draw it onto the image
        for line in text.split('\n'):
            words = line.split()
            current_line = ""

            for word in words:
                test_line = current_line + word + ' '
                width_test = draw.textbbox((0, 0), test_line, font=font)[2]  # Get the width of the text

                if width_test <= (width - 20):  # Subtract some padding
                    current_line = test_line  # Add the word to the current line
                else:
                    # Draw the current line and reset it
                    draw.text((x, y), current_line, fill='black', font=font)
                    y += line_height  # Move down for the next line
                    current_line = word + ' '  # Start a new line with the current word

            # Draw any remaining text
            if current_line:
                draw.text((x, y), current_line, fill='black', font=font)
                y += line_height  # Move down for the next line

        # Save the image with the same name as the font (without extension)
        output_image_path = os.path.join(output_image_folder, f"{os.path.splitext(font_file)[0]}.png")
        image.save(output_image_path)

        # # Optionally display the image using matplotlib (comment this if too many images)
        # plt.imshow(image)
        # plt.axis('off')  # Turn off axis numbers and ticks
        # plt.show()

        print(f"Image saved as {output_image_path}")
