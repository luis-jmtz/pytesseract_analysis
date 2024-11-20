import os
import svgwrite

def generate_alphanumeric_svgs(weight_value, slant_value, width_value, curviness_value):

    # Define alphanumeric characters
    alphanumeric_chars = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

    # Define output folder naming convention
    folder_name = f"weight{weight_value}_slant{slant_value}_width{width_value}_curviness{curviness_value}"
    output_folder = os.path.join(folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # Function to create SVGs for alphanumeric characters
    def create_character_svg(character, folder):
        filename = f"{character}.svg"
        dwg = svgwrite.Drawing(filename=os.path.join(folder, filename), size=("100px", "100px"))

        # Apply text transformations and styling based on parameters
        font_style = f"skewX({-slant_value})"  # Apply slant transformation
        dwg.add(dwg.text(
            character,
            insert=("50%", "50%"),
            text_anchor="middle",
            alignment_baseline="middle",
            font_size="18px",  # Fixed font size
            font_weight=str(weight_value),  # Adjust thickness
            font_family="Arial",  # Simplified styling, can be extended for variety
            style=f"font-stretch:{width_value};",  # Adjust width
            fill="black",
            transform=font_style
        ))
        dwg.save()

    # Generate SVGs for all alphanumeric characters
    for char in alphanumeric_chars:
        create_character_svg(char, output_folder)

"""
Parameters:
    weight_value (int): Line thickness.
    slant_value (int): Font slant in degrees (-ve for backward, +ve for forward).
    width_value (float): Adjusts the proportions of counters, strokes, spacing, and kerning.
    curviness_value (int): Level of curviness (0 is angular, higher values are more curved).
"""

generate_alphanumeric_svgs(700, 0, 0, 0)
