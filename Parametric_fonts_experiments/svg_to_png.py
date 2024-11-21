import os
from cairosvg import svg2png


class SVGToPNG:
    def __init__(self, input_folder, output_folder):
        """
        Initializes the converter with input and output folder paths.

        Parameters:
            input_folder (str): Path to the folder containing SVG files.
            output_folder (str): Path to the folder where PNG files will be saved.
        """
        self.input_folder = input_folder
        self.output_folder = output_folder

        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def convert_all(self):
        """
        Converts all SVG files in the input folder to PNG files in the output folder.
        The PNG files retain the same names as the SVG files, with a white background.
        """
        # Get a list of all SVG files in the input folder
        svg_files = [f for f in os.listdir(self.input_folder) if f.lower().endswith('.svg')]

        # Convert each SVG file to PNG
        for svg_file in svg_files:
            input_path = os.path.join(self.input_folder, svg_file)
            output_file = os.path.splitext(svg_file)[0] + '.png'  # Replace .svg with .png
            output_path = os.path.join(self.output_folder, output_file)

            # Read SVG and add white background
            with open(input_path, 'rb') as svg_input:
                svg_data = svg_input.read()
                # Convert SVG to PNG with a white background
                svg2png(bytestring=svg_data, write_to=output_path, output_width=None, background_color="white")

            print(f"Converted: {svg_file} -> {output_file}")

        print(f"All SVG files have been converted and saved to: {self.output_folder}")
