from create_svg import SVGGenerator
from svg_to_png import SVGToPNG

"""
Parameters:
    weight_value (int): Line thickness. range: 100 - 1500
    slant_value (int): Font slant in degrees. range: -60 - 60
    width_value (float): Adjusts the proportions of text along X-axis. range: -50 - 50
"""

# Default values: weight400, slant0, width0
generator = SVGGenerator()
output_folder = "generated_svgs"  # Define the folder to store SVG files
output_path = generator.generate(weight_value=1200, slant_value=60, width_value=50)

print(f"SVG file created at: {output_path}")

# Input folder for SVGs (not the file path)
input_folder = output_folder

# Output folder for converted PNGs
png_output_folder = "converted_svgs"

converter = SVGToPNG(input_folder=input_folder, output_folder=png_output_folder)
converter.convert_all()
