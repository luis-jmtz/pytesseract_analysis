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

        # Adjust canvas size and offsets dynamically
        slant_padding = abs(slant_value) * 2
        canvas_width = 100 + slant_padding  # Increase canvas width to accommodate slant
        canvas_height = 100
        insert_x = canvas_width / 2  # Center character horizontally
        insert_y = "50%"  # Center character vertically

        dwg = svgwrite.Drawing(filename=os.path.join(folder, filename), size=(f"{canvas_width}px", f"{canvas_height}px"))

        # Calculate scaling for width adjustment
        scale_x = 1 + width_value  # Stretch/squeeze x-axis; width_value=0 is default
        scale_x = max(0.1, scale_x)  # Prevent scale from collapsing completely (set a lower limit)

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
            fill="black",
            transform=f"{font_style} scale({scale_x}, 1)",  # Scale x-axis only
        ))
        dwg.save()

    # Generate SVGs for all alphanumeric characters
    for char in alphanumeric_chars:
        create_character_svg(char, output_folder)


"""
Parameters:
    weight_value (int): Line thickness. range: 100 - 1500
    slant_value (int): Font slant in degrees. range: -60 - 60
    width_value (float): squeezing or stretching only on the x axis. range -0.5 - 1 (where 1 is a 100% increase)
"""

generate_alphanumeric_svgs(100, 0, -0.5)
