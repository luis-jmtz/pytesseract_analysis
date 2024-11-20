import os
import pytesseract
import cv2
import pandas as pd
import re

def process_images(image_folder_path, ground_truth_path, csv_filename, column_value_name='Value'):

    # Define the column headers
    column_image_name = 'Image Name'
    column_accuracy = 'OCR Accuracy'
    column_output_text = 'Tesseract Output'

    # Create a list to store results
    results = []

    # Load and normalize the ground truth text
    with open(ground_truth_path, 'r') as file:
        ground_truth = file.read().lower().replace('\n', ' ').replace('  ', ' ').strip()

    # Loop through each file in the image folder
    for filename in os.listdir(image_folder_path):
        if filename.endswith('.png'):
            # Extract the value from the filename using regex
            match = re.match(r".*_(\-?\d+)(?:_[^_]*)?\.png", filename)
            if match:
                image_name = filename
                value = match.group(1)  # Extract the numeric value after the last underscore

                # Load the image using OpenCV
                image_path = os.path.join(image_folder_path, filename)
                img = cv2.imread(image_path)

                # Run pytesseract to extract text from the image
                extracted_text = pytesseract.image_to_string(img).lower().replace('\n', ' ').replace('  ', ' ').strip()

                # Compute character-level accuracy (ignoring case, spaces, and newlines)
                max_len = max(len(extracted_text), len(ground_truth))
                if max_len > 0:
                    padded_extracted = extracted_text.ljust(max_len)
                    padded_ground_truth = ground_truth.ljust(max_len)
                    matches = sum(1 for a, b in zip(padded_extracted, padded_ground_truth) if a == b)
                    accuracy = matches / max_len
                else:
                    accuracy = 0.0  # No ground truth or extracted text

                # Append the result to the list
                results.append({
                    column_image_name: image_name,
                    column_value_name: value,  # Use the dynamic column name
                    column_accuracy: accuracy,
                    column_output_text: pytesseract.image_to_string(img).strip()  # Original output for reference
                })

    # Create a DataFrame from the results list
    df = pd.DataFrame(results)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_filename, index=False)

    print(f"Results saved to {csv_filename}")


image_folder = r'Images\Grade'  
ground_truth = r'test_text.txt'
output_csv = 'grade_accuracy.csv' 
custom_column_name = 'Grade'  

process_images(image_folder, ground_truth, output_csv, column_value_name=custom_column_name)

image_folder = r'Images\Slant'  
output_csv = 'slant_accuracy.csv' 
custom_column_name = 'Slant'  

process_images(image_folder, ground_truth, output_csv, column_value_name=custom_column_name)

image_folder = r'Images\Weight'  
output_csv = 'Weight_accuracy.csv' 
custom_column_name = 'Weight'  

process_images(image_folder, ground_truth, output_csv, column_value_name=custom_column_name)

image_folder = r'Images\Width'  
output_csv = 'Width_accuracy.csv' 
custom_column_name = 'Width'  

process_images(image_folder, ground_truth, output_csv, column_value_name=custom_column_name)
