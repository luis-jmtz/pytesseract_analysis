from create_svg import SVGGenerator
"""
Parameters:
    weight_value (int): Line thickness. range: 100 - 1500
    slant_value (int): Font slant in degrees. range: -60 - 60
    width_value (float): Adjusts the proportions of text along X-axis. range: -50 - 50
"""

generator = SVGGenerator()
output_path = generator.generate(weight_value=400, slant_value=0, width_value=0)

print(f"SVG file created at: {output_path}")