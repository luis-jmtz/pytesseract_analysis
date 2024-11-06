import os
import csv
from PIL import Image
import pytesseract
from collections import Counter

# Define the required variables
input_folder = r"data_set_builder\Standard Fonts Images"  
ground_truth_file = r"data_set_builder\input.txt"  
output_csv = r"standard_font_analysis.csv"  

# Load the ground truth text from the specified .txt file
with open(ground_truth_file, 'r', encoding='utf-8') as file:
    ground_truth_text = file.read().strip()

# Function to calculate character accuracy based on character frequencies
def character_accuracy(ground_truth, ocr_text):
    # Count characters in both ground truth and OCR output
    ground_truth_counts = Counter(ground_truth)
    ocr_counts = Counter(ocr_text)
    
    # Calculate the number of correctly matched characters (min count of each character in both texts)
    matched_characters = sum(min(ground_truth_counts[char], ocr_counts[char]) for char in ground_truth_counts)
    
    # Calculate accuracy as matched characters over the total characters in the ground truth
    return matched_characters / max(len(ground_truth), 1)  # Avoid division by zero if ground_truth is empty

# Open the output CSV file for writing
with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(['image_name', 'ocr_output', 'character_accuracy'])
    
    total_accuracy = 0  # Accumulate character accuracy for all images
    processed_images = 0  # Count of processed images

    # Loop through the files in the specified input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Check if the file is an image based on its extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            try:
                # Extract text from the image using pytesseract
                with Image.open(file_path) as img:
                    ocr_output = pytesseract.image_to_string(img)

                # Calculate character accuracy
                accuracy = character_accuracy(ground_truth_text, ocr_output)
                
                # Write the data to CSV
                writer.writerow([filename, ocr_output, accuracy])
                
                # Print the results
                print(f"Data for {filename}:")
                print(f"  OCR Output: {ocr_output}")
                print(f"  Character Accuracy: {accuracy:.2%}\n")
                
                # Accumulate for average accuracy
                total_accuracy += accuracy
                processed_images += 1

            except Exception as e:
                print(f"An error occurred with file {filename}: {e}")

    # Calculate and write average accuracy if at least one image was processed
    if processed_images > 0:
        average_accuracy = total_accuracy / processed_images
        writer.writerow([])  # Empty row for separation
        writer.writerow(['Average Accuracy', '', average_accuracy])
        
        print(f"\nAverage Character Accuracy across all images: {average_accuracy:.2%}")
