import os
import svgwrite

def generate_alphanumeric_svgs(weight_value, slant_value, width_value):
    # Define alphanumeric characters
    numbers = [chr(i) for i in range(48, 58)]  # Digits 0-9
    uppercase = [chr(i) for i in range(65, 91)]  # Uppercase A-Z
    lowercase = [chr(i) for i in range(97, 123)]  # Lowercase a-z

    # Combine all characters
    alphanumeric_chars = numbers + uppercase + lowercase

    # Define output folder naming convention
    folder_name = f"weight{weight_value}_slant{slant_value}_width{width_value}"
    output_folder = os.path.join(folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # Function to create SVGs for alphanumeric characters
    def create_character_svg(character, folder):
        if character.isupper():
            filename = f"{character}_upper.svg"
        elif character.islower():
            filename = f"{character}_lower.svg"
        else:  # Digits
            filename = f"{character}.svg"

        # Adjust canvas size based on slant
        canvas_width = 100 + abs(slant_value) * 2  # Expand canvas width to account for extreme slant
        canvas_height = 100

        # Adjust text insertion point
        x_offset = abs(slant_value) if slant_value < 0 else 0
        insert_x = 50 + x_offset
        insert_y = "50%"

        dwg = svgwrite.Drawing(filename=os.path.join(folder, filename), size=(f"{canvas_width}px", f"{canvas_height}px"))

        # Apply text transformations and styling based on parameters
        font_style = f"skewX({-slant_value})"  # Apply slant transformation
        dwg.add(dwg.text(
            character,
            insert=(f"{insert_x}px", insert_y),
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
"""

# Generate SVGs with specified parameters
generate_alphanumeric_svgs(100, -45, 0)
