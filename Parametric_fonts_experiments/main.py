from create_svg import SVGGenerator

generator = SVGGenerator()
output_path = generator.generate(weight=500, slant=60, width=0)

print(f"SVG file created at: {output_path}")