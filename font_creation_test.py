import os
import svgwrite

# Define the folder to save SVG files
output_folder = "alpha_numeric_svgs"
os.makedirs(output_folder, exist_ok=True)

# Define characters to create SVGs for
alphanumeric_chars = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

# Function to create an SVG for a character
def create_svg(character, folder):
    dwg = svgwrite.Drawing(filename=os.path.join(folder, f"{character}.svg"), size=("100px", "100px"))
    dwg.add(dwg.text(character, insert=("50%", "50%"), text_anchor="middle", alignment_baseline="middle",
                     font_size="72px", font_family="Arial", fill="black"))
    dwg.save()

# Generate SVGs for all alphanumeric characters
for char in alphanumeric_chars:
    create_svg(char, output_folder)

output_folder
