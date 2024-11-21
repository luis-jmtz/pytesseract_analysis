import os
import svgwrite

class SVGGenerator:
    def __init__(self):
        # Hardcoded output folder
        self.output_folder = "generated_svgs"
        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def generate(self, weight, slant, width):
        """
        Generates an SVG for the capital letter A with the given parameters.

        Parameters:
            weight (int): Line thickness. Range: 100 - 1500
            slant (int): Font slant in degrees. Range: -60 - 60
            width (float): Adjusts the proportions of text along X-axis. Range: -50 - 75
        """
        # Define the file name based on the naming convention
        file_name = f"weight{weight}_slant{slant}_width{width}.svg"
        file_path = os.path.join(self.output_folder, file_name)

        # Generate SVG for the capital letter A
        self._create_character_svg("A", weight, slant, width, file_path)

        return file_path

    def _create_character_svg(self, character, weight, slant, width, file_path):
        # Padding to ensure the character is visually centered
        padding = 10  # Adjust as needed for better visual appearance

        # Calculate scaling factor for X-axis based on width_value
        scale_x = 1 + (width / 100)  # Positive stretches, negative squeezes
        scale_y = 1  # Keep Y-axis scaling fixed

        # Adjust canvas size dynamically based on scaling
        base_canvas_width = 100  # Base canvas size
        canvas_width = int(base_canvas_width * scale_x)  # Dynamically scale width
        canvas_height = 100  # Fixed height

        # Adjust for padding
        canvas_width_with_padding = canvas_width + 2 * padding
        canvas_height_with_padding = canvas_height + 2 * padding

        # Center character dynamically within the padded area
        insert_x = canvas_width_with_padding / 2
        insert_y = canvas_height_with_padding / 2

        dwg = svgwrite.Drawing(
            filename=file_path,
            size=(f"{canvas_width_with_padding}px", f"{canvas_height_with_padding}px")
        )

        # Apply text transformations and styling based on parameters
        font_style = f"skewX({-slant})"  # Apply slant transformation

        # Use `font-weight` up to 900, and simulate additional weight with stroke
        effective_weight = min(weight, 900)  # Limit font-weight to max 900
        stroke_weight = max(0, (weight - 900) * 0.005)  # Gradual increase in stroke thickness

        # Combine scaling and slant transformations
        transform = f"{font_style} scale({scale_x}, {scale_y})"

        dwg.add(dwg.text(
            character,
            insert=(f"{insert_x}px", f"{insert_y}px"),
            text_anchor="middle",
            alignment_baseline="middle",
            font_size="18px",  # Fixed font size
            font_weight=str(effective_weight),  # Adjust thickness
            font_family="Arial",  # Simplified styling, can be extended for variety
            fill="black",
            stroke="black",  # Add stroke to simulate extra weight
            stroke_width=f"{stroke_weight}px",  # Adjust stroke width for additional weight
            transform=transform  # Apply combined transformations
        ))
        dwg.save()

# Example usage in main.py
if __name__ == "__main__":
    generator = SVGGenerator()
    output_path = generator.generate(weight=500, slant=0, width=0)
    print(f"SVG file created at: {output_path}")
