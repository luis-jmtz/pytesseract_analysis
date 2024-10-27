import os
import re
import csv
from PIL import Image
import pytesseract
import Levenshtein

# Specify folder path and output CSV file path
folder_path = 'Temp_image_folder'  # Replace with the path to your folder
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

# Function to calculate WER
def word_error_rate(ground_truth, ocr_text):
    gt_words = ground_truth.split()
    ocr_words = ocr_text.split()
    return Levenshtein.distance(" ".join(gt_words), " ".join(ocr_words)) / max(len(gt_words), 1)

# Open the CSV file for writing
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(['image_name', 'base_truth', 'ocr_output', 'character_accuracy', 'levenshtein_distance', 'CER', 'WER'])
    
    # Loop through files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
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
                    
                    # Calculate Levenshtein Distance
                    levenshtein_distance = Levenshtein.distance(base_truth, ocr_output)
                    
                    # Calculate Character Accuracy
                    character_accuracy = 1 - (levenshtein_distance / max(len(base_truth), 1))
                    
                    # Calculate CER
                    cer = levenshtein_distance / max(len(base_truth), 1)
                    
                    # Calculate WER
                    wer = word_error_rate(base_truth, ocr_output)
                    
                    # Write the data to CSV
                    writer.writerow([filename, base_truth, ocr_output, character_accuracy, levenshtein_distance, cer, wer])
                    
                    # Print the results
                    print(f"Data for {filename}:")
                    print(f"  Character Accuracy: {character_accuracy:.2%}")
                    print(f"  Levenshtein Distance: {levenshtein_distance}")
                    print(f"  CER: {cer:.2%}")
                    print(f"  WER: {wer:.2%}\n")
                    
                except Exception as e:
                    print(f"An error occurred with file {filename} or its TXT: {e}")
            else:
                print(f"No TXT file found for {filename}")
