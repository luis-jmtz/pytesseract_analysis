import os
import json
import csv
from PIL import Image
import pytesseract

# Specify the folder path and output CSV file path
folder_path = r"C:\Users\Superuser\Documents\Snr Seminar Images\handwritten_imgs\train" 
output_csv_path = r'Test_Data\GNHK_dataset_accuracy_test.csv'  # Path for the output CSV file

# Function to calculate character accuracy
def character_accuracy(ground_truth, ocr_text):
    # Counts characters that match between ground truth and OCR output
    matches = sum(1 for gt_char, ocr_char in zip(ground_truth, ocr_text) if gt_char == ocr_char)
    return matches / max(len(ground_truth), 1)  # Avoid division by zero if ground_truth is empty

# Open the CSV file for writing
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(['image_name', 'base_truth', 'ocr_output', 'character_accuracy'])
    
    total_accuracy = 0  # For calculating average accuracy
    processed_images = 0  # Count of images processed

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
                    
                    # Calculate character accuracy
                    accuracy = character_accuracy(base_truth, ocr_output)
                    
                    # Write the data to CSV
                    writer.writerow([filename, base_truth, ocr_output, accuracy])
                    
                    # Print the results
                    print(f"Data for {filename}:")
                    print(f"  Character Accuracy: {accuracy:.2%}\n")
                    
                    # Accumulate for average accuracy
                    total_accuracy += accuracy
                    processed_images += 1
                    
                except Exception as e:
                    print(f"An error occurred with file {filename} or its JSON: {e}")
            else:
                print(f"No JSON file found for {filename}")
    
    # Calculate average accuracy if at least one image was processed
    if processed_images > 0:
        average_accuracy = total_accuracy / processed_images
        writer.writerow([])  # Empty row for separation
        writer.writerow(['Average Accuracy', '', '', average_accuracy])
        
        print(f"\nAverage Character Accuracy across all images: {average_accuracy:.2%}")
