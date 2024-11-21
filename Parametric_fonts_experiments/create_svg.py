import os
import svgwrite
import math


class SVGGenerator:
    def __init__(self):
        # Hardcoded output folder
        self.output_folder = "generated_svgs"
        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def generate(self, weight_value, slant_value, width_value):
        """
        Generates an SVG for the capital letter A with the given parameters.

        Parameters:
            weight_value (int): Line thickness. Range: 100 - 1500
            slant_value (int): Font slant in degrees. Range: -60 - 60
            width_value (float): Adjusts the proportions of text along X-axis. Range: -50 - 75
        """
        # Define the file name based on the naming convention
        file_name = f"weight{weight_value}_slant{slant_value}_width{width_value}.svg"
        file_path = os.path.join(self.output_folder, file_name)

        # Generate SVG for the capital letter A
        self._create_character_svg("A", weight_value, slant_value, width_value, file_path)

        return file_path

    def _create_character_svg(self, character, weight_value, slant_value, width_value, file_path):
        # Base font size to calculate dimensions
        font_size = 18

        # Scaling factors based on width_value
        scale_x = 1 + (width_value / 100)
        scale_y = 1

        # Calculate approximate text dimensions
        text_width = font_size * 0.6 * scale_x  # Adjust width by scale
        text_height = font_size * scale_y  # Adjust height by scale

        # Adjust for slant transformation (calculate extra width required)
        slant_radians = math.radians(slant_value)
        slant_adjustment = text_height * abs(math.tan(slant_radians))

        # Add padding and slant adjustment
        padding = 0.2 * max(text_width, text_height)  # 20% of the largest dimension
        canvas_width = text_width + slant_adjustment + 2 * padding
        canvas_height = text_height + 2 * padding

        # Center character dynamically
        insert_x = canvas_width / 2
        insert_y = canvas_height / 2

        # Create the SVG canvas
        dwg = svgwrite.Drawing(
            filename=file_path,
            size=(f"{canvas_width}px", f"{canvas_height}px")
        )

        # Apply text transformations
        font_style = f"skewX({-slant_value})"  # Apply slant transformation
        transform = f"{font_style} scale({scale_x}, {scale_y})"

        # Calculate effective weight and stroke
        effective_weight = min(weight_value, 900)
        stroke_weight = max(0, (weight_value - 900) * 0.005)

        # Add the character text to the SVG
        dwg.add(dwg.text(
            character,
            insert=(f"{insert_x}px", f"{insert_y}px"),
            text_anchor="middle",
            alignment_baseline="middle",
            font_size=f"{font_size}px",
            font_weight=str(effective_weight),
            font_family="Arial",
            fill="black",
            stroke="black",
            stroke_width=f"{stroke_weight}px",
            transform=transform
        ))

        # Save the SVG
        dwg.save()


# Example usage in main.py
if __name__ == "__main__":
    generator = SVGGenerator()
    output_path = generator.generate(weight_value=500, slant_value=60, width_value=0)
    print(f"SVG file created at: {output_path}")
