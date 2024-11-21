from create_svg import SVGGenerator

generator = SVGGenerator()
output_path = generator.generate(weight=1200, slant=0, width=0)

print(f"SVG file created at: {output_path}")