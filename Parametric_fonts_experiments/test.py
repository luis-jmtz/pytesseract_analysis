import os
import cairosvg

def convert_svgs_to_pngs(folder_path, output_folder=None):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder {folder_path} does not exist.")
        return

    # Set the output folder
    if output_folder is None:
        output_folder = os.path.join(folder_path, "png_output")
    os.makedirs(output_folder, exist_ok=True)

    # List SVG files in the folder
    svg_files = [f for f in os.listdir(folder_path) if f.endswith('.svg')]
    if not svg_files:
        print(f"No SVG files found in {folder_path}.")
        return

    print(f"Converting {len(svg_files)} SVG files to PNG...")

    for svg_file in svg_files:
        svg_path = os.path.join(folder_path, svg_file)
        png_file = os.path.splitext(svg_file)[0] + ".png"
        png_path = os.path.join(output_folder, png_file)

        try:
            # Convert SVG to PNG
            cairosvg.svg2png(url=svg_path, write_to=png_path)
            print(f"Converted: {svg_file} -> {png_file}")
        except Exception as e:
            print(f"Error converting {svg_file}: {e}")

    print(f"Conversion completed. PNG files saved in {output_folder}.")

# Example usage
folder_path = "weight500_slant0_width0"  # Replace with your folder path
convert_svgs_to_pngs(folder_path)
