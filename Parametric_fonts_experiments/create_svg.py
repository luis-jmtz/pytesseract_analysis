import os


class SVGGenerator:
    def __init__(self, output_folder="generated_svgs", font_size=15, padding_scale=0.2, slant_adjustment_factor=1.5):
        self.output_folder = output_folder
        self.font_size = font_size  # Fixed font size
        self.padding_scale = padding_scale  # Padding scale relative to font size
        self.slant_adjustment_factor = slant_adjustment_factor  # Extra adjustment for slant effects

        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def _calculate_canvas_adjustments(self, slant_value, width_value, text_length):
        """
        Calculate additional padding and canvas width adjustments based on slant and width scaling.
        """
        slant_factor = abs(slant_value) / 60  # Proportion of slant (max 60 degrees)
        width_factor = max(0.5, 1 + width_value / 100)  # Adjust width scale
        base_width = text_length * self.font_size * width_factor // 2

        # Adjustments for slant
        extra_left = self.font_size * slant_factor * self.slant_adjustment_factor if slant_value < 0 else 0
        extra_right = self.font_size * slant_factor * self.slant_adjustment_factor if slant_value > 0 else 0

        # Adjusted width
        adjusted_width = base_width + extra_left + extra_right

        return adjusted_width, extra_left, extra_right

    def generate(self, weight_value=400, slant_value=0, width_value=0, text="AB ab"):
        """
        Generates an SVG with the given parameters and text, dynamically adjusting the canvas size.

        Parameters:
            weight_value (int): Line thickness (100 - 1500).
            slant_value (int): Font slant in degrees (-60 to 60).
            width_value (float): Adjusts text proportions along the X-axis (-50 to 50).
            text (str): The text to be rendered in the SVG.
        """
        # Calculate canvas adjustments
        text_length = len(text)
        adjusted_width, extra_left, extra_right = self._calculate_canvas_adjustments(slant_value, width_value, text_length)

        # Base padding
        dynamic_padding = self.font_size * self.padding_scale
        canvas_width = adjusted_width + 2 * dynamic_padding
        canvas_height = self.font_size + 2 * dynamic_padding

        # Calculate text starting position
        x_position = dynamic_padding + extra_left
        y_position = dynamic_padding + self.font_size

        # Generate file name based on parameters
        file_name = f"weight{weight_value}_slant{slant_value}_width{width_value}.svg"

        # Start SVG content
        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}px" height="{canvas_height}px" viewBox="0 0 {canvas_width} {canvas_height}">
            <rect width="100%" height="100%" fill="white"/>
        """

        # Add text element to SVG
        svg_content += f"""<text x="{x_position}" y="{y_position}" font-family="Arial" 
            font-size="{self.font_size}" font-weight="{weight_value}" 
            transform="skewX({slant_value}) scale({1 + width_value / 100}, 1)" fill="black">{text}</text>"""

        # Close SVG content
        svg_content += "</svg>"

        # Write SVG to file
        output_path = os.path.join(self.output_folder, file_name)
        with open(output_path, "w") as svg_file:
            svg_file.write(svg_content)

        print(f"SVG created: {output_path}")
        return output_path
