import os
import csv
from PIL import Image
import pytesseract
import Levenshtein

# Define the required variables
input_folder = r"data_set_builder\dyslexia_fonts_images"  
ground_truth_file = r"data_set_builder\input.txt"  
output_csv = r"dsylexia_font_analysis.csv"  

# Load the ground truth text from the specified .txt file
with open(ground_truth_file, 'r', encoding='utf-8') as file:
    ground_truth_text = file.read().strip()

# Function to calculate Word Error Rate (WER)
def word_error_rate(ground_truth, ocr_text):
    gt_words = ground_truth.split()
    ocr_words = ocr_text.split()
    return Levenshtein.distance(" ".join(gt_words), " ".join(ocr_words)) / max(len(gt_words), 1)

# Open the output CSV file for writing
with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(['image_name', 'ocr_output', 'character_accuracy', 'levenshtein_distance', 'CER', 'WER'])
    
    # Loop through the files in the specified input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Check if the file is an image based on its extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            try:
                # Extract text from the image using pytesseract
                with Image.open(file_path) as img:
                    ocr_output = pytesseract.image_to_string(img)

                # Calculate Levenshtein Distance
                levenshtein_distance = Levenshtein.distance(ground_truth_text, ocr_output)
                
                # Calculate Character Accuracy
                character_accuracy = 1 - (levenshtein_distance / max(len(ground_truth_text), 1))
                
                # Calculate Character Error Rate (CER)
                cer = levenshtein_distance / max(len(ground_truth_text), 1)
                
                # Calculate Word Error Rate (WER)
                wer = word_error_rate(ground_truth_text, ocr_output)
                
                # Write the data to CSV
                writer.writerow([filename, ocr_output, character_accuracy, levenshtein_distance, cer, wer])
                
                # Print the results
                print(f"Data for {filename}:")
                print(f"  OCR Output: {ocr_output}")
                print(f"  Character Accuracy: {character_accuracy:.2%}")
                print(f"  Levenshtein Distance: {levenshtein_distance}")
                print(f"  Character Error Rate (CER): {cer:.2%}")
                print(f"  Word Error Rate (WER): {wer:.2%}\n")

            except Exception as e:
                print(f"An error occurred with file {filename}: {e}")
