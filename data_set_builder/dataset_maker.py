from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Define file paths
input_file_path = r"data_set_builder\input.txt"  # Path to the input text file
font_file_path = r"data_set_builder\fonts\Roboto-Regular.ttf"   # Path to the font file
output_image_path = 'output_image.png'  # Path to the output image file


# Load text from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Create a new image
width, height = 800, 600  # Adjust dimensions as needed
image = Image.new('RGB', (width, height), color='white')

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Specify font and size
try:
    # Load the specified TTF font
    font = ImageFont.truetype(font_file_path, 16)  # You can change the font size here
except IOError:
    font = ImageFont.load_default()  # Fallback to default font

# Set the starting position for the text
x, y = 10, 10
line_height = 20  # Adjust line height

# Wrap text and draw it onto the image
for line in text.split('\n'):
    # Split the line into words
    words = line.split()
    current_line = ""

    for word in words:
        # Check the width of the current line with the new word added
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

# Save the image
image.save(output_image_path)

# Optionally display the image using matplotlib
plt.imshow(image)
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()

print(f"Image saved as {output_image_path}")