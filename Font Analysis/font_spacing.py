import os
import csv
from fontTools.ttLib import TTFont

def get_default_character_spacing(font_path):

    # Load the font using fonttools
    font = TTFont(font_path)
    
    # Retrieve the horizontal metrics (hmtx) table
    hmtx_table = font['hmtx']
    
    # Retrieve the glyph names from the 'cmap' table
    cmap_table = font['cmap']
    unicode_map = cmap_table.getBestCmap()
    
    # Calculate the total advance width of all characters
    total_advance_width = 0
    total_chars = 0

    # Iterate over all characters in the unicode map and fetch their advance width
    for char, glyph_id in unicode_map.items():
        # Get the advance width for this character using its glyph ID
        if glyph_id in hmtx_table.metrics:
            advance_width, _ = hmtx_table.metrics[glyph_id]
            total_advance_width += advance_width
            total_chars += 1
    
    # Calculate average advance width (default spacing)
    if total_chars > 0:
        average_advance_width = total_advance_width / total_chars
        return average_advance_width
    else:
        return None

def process_fonts_in_folder(fonts_folder, output_csv_path):

    # Create or open the CSV file for writing the results
    with open(output_csv_path, mode='w', newline='') as csvfile:
        fieldnames = ['Font Name', 'Default Character Spacing (Advance Width)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header to the CSV
        writer.writeheader()
        
        # Loop through each .ttf font file in the fonts folder
        for font_filename in os.listdir(fonts_folder):
            if font_filename.endswith('.ttf'):
                font_path = os.path.join(fonts_folder, font_filename)
                font_name = os.path.splitext(font_filename)[0]  # Get the font name without extension
                
                # Get the default character spacing for this font
                default_spacing = get_default_character_spacing(font_path)
                
                # If spacing is valid, write the result to the CSV
                if default_spacing is not None:
                    writer.writerow({'Font Name': font_name, 'Default Character Spacing (Advance Width)': default_spacing})
                else:
                    print(f"Could not calculate spacing for font: {font_name}")

# Example usage:
fonts_folder = r'Low Accuracy Fonts'  
output_csv_path = r'low_acc_font_spacing_results.csv' 

process_fonts_in_folder(fonts_folder, output_csv_path)
print(f"Font spacing data has been saved to: {output_csv_path}")
