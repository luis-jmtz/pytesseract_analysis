import os
import json
import csv
from PIL import Image
import pytesseract
import Levenshtein

# Specify the folder path and output CSV file path
folder_path = r"C:\Users\Superuser\Documents\Snr Seminar Images\handwritten_imgs\train" # Replace with the path to your folder
output_csv_path = 'output_data.csv'  # Path for the output CSV file

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

        # Check if the file is an image based on its extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            base_name = os.path.splitext(filename)[0]
            json_file_path = os.path.join(folder_path, f"{base_name}.json")
            
            if os.path.exists(json_file_path):
                try:
                    # OCR text extraction
                    with Image.open(file_path) as img:
                        ocr_output = pytesseract.image_to_string(img)
                    
                    # JSON base truth extraction
                    with open(json_file_path, 'r') as json_file:
                        json_data = json.load(json_file)
                        base_truth = ' '.join(item["text"] for item in json_data if item["text"].isalnum())
                    
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
                    print(f"An error occurred with file {filename} or its JSON: {e}")
            else:
                print(f"No JSON file found for {filename}")
