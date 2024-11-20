import os
import svgwrite

# Define the folder to save SVG files
output_folder = "alpha_numeric_svgs"
os.makedirs(output_folder, exist_ok=True)

# Define characters to create SVGs for
alphanumeric_chars = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

# Function to create an SVG with proper naming convention
def create_svg_with_naming(character, folder):
    if character.isupper():
        filename = f"upper_{character}.svg"
    elif character.islower():
        filename = f"lower_{character}.svg"
    else:
        filename = f"{character}.svg"  # For numbers
    dwg = svgwrite.Drawing(filename=os.path.join(folder, filename), size=("100px", "100px"))
    dwg.add(dwg.text(character, insert=("50%", "50%"), text_anchor="middle", alignment_baseline="middle",
                     font_size="72px", font_family="Arial", fill="black"))
    dwg.save()

# Generate SVGs for all alphanumeric characters with proper naming
for char in alphanumeric_chars:
    create_svg_with_naming(char, output_folder)

output_folder
