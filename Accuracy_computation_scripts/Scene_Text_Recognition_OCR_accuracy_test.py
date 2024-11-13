import os
import re
import csv
from PIL import Image
import pytesseract

# Specify folder path and output CSV file path
folder_path = r"D:\Total Text - Scene Text Recognition\img_with_ground_truth"  # Replace with the path to your folder
output_csv_path = 'output_data_txt.csv'  # Output CSV file path

# Function to parse ground truth text from the .txt file
def parse_ground_truth_text(txt_file_path):
    ground_truth_text = []
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.search(r"transcriptions: \[u'(.*?)'\]", line)
            if match:
                transcription = match.group(1)
                # Only add valid transcriptions (exclude placeholders like '#')
                if transcription.isalnum():
                    ground_truth_text.append(transcription)
    return ' '.join(ground_truth_text)

# Function to calculate character accuracy
def calculate_character_accuracy(ground_truth, ocr_text):
    matches = sum(1 for gt_char, ocr_char in zip(ground_truth, ocr_text) if gt_char == ocr_char)
    total_chars = max(len(ground_truth), 1)
    return matches / total_chars

# Open the CSV file for writing
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(['image_name', 'base_truth', 'ocr_output', 'character_accuracy'])
    
    total_accuracy = 0
    count = 0
    
    # Loop through files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Extract the base name (e.g., "img11" from "img11.jpg")
            base_name = re.sub(r'\.[^.]+$', '', filename)
            
            # Search for the corresponding .txt file
            txt_file_path = os.path.join(folder_path, f"poly_gt_{base_name}.txt")
            
            if os.path.exists(txt_file_path):
                try:
                    # OCR text extraction
                    with Image.open(file_path) as img:
                        ocr_output = pytesseract.image_to_string(img)
                    
                    # Parse ground truth from the .txt file
                    base_truth = parse_ground_truth_text(txt_file_path)
                    
                    # Calculate Character Accuracy
                    character_accuracy = calculate_character_accuracy(base_truth, ocr_output)
                    total_accuracy += character_accuracy
                    count += 1
                    
                    # Write the data to CSV
                    writer.writerow([filename, base_truth, ocr_output, f"{character_accuracy:.2%}"])
                    
                    # Print the results
                    print(f"Data for {filename}:")
                    print(f"  Character Accuracy: {character_accuracy:.2%}\n")
                    
                except Exception as e:
                    print(f"An error occurred with file {filename} or its TXT: {e}")
            else:
                print(f"No TXT file found for {filename}")

    # Calculate and write average accuracy if there was any valid data
    if count > 0:
        avg_accuracy = total_accuracy / count
        writer.writerow([])
        writer.writerow(['Average Accuracy', '', '', f"{avg_accuracy:.2%}"])
        print(f"Average Character Accuracy: {avg_accuracy:.2%}")
    else:
        print("No valid data processed.")
