from create_svg import SVGGenerator

generator = SVGGenerator()
output_path = generator.generate(weight_value=500, slant_value=60, width_value=0)

print(f"SVG file created at: {output_path}")