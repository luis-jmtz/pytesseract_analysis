import os
import pytesseract
import cv2
import pandas as pd
import re
from collections import Counter

def process_images(image_folder_path, ground_truth_path, csv_filename, column_value_name='Value'):
    """
    Processes images in a folder, compares their OCR text against a shared ground truth,
    calculates accuracy based on character frequency matches, and saves results to a CSV file.

    Parameters:
        image_folder_path (str): Path to the folder containing PNG images.
        ground_truth_path (str): Path to the text file containing the ground truth.
        csv_filename (str): Name of the CSV file to save results.
        column_value_name (str): Custom name for the column storing extracted values.

    Returns:
        None
    """
    # Define the column headers
    column_image_name = 'Image Name'
    column_accuracy = 'OCR Accuracy'
    column_output_text = 'Tesseract Output'

    # Create a list to store results
    results = []

    # Load and normalize the ground truth text (removing spaces and newlines)
    with open(ground_truth_path, 'r') as file:
        ground_truth = file.read().replace(' ', '').replace('\n', '').strip()

    # Count the frequency of each character in the ground truth
    ground_truth_counter = Counter(ground_truth)

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
                extracted_text = pytesseract.image_to_string(img).replace(' ', '').replace('\n', '').strip()

                # Count the frequency of each character in the extracted text
                extracted_text_counter = Counter(extracted_text)

                # Calculate the match based on frequency of characters
                total_matches = 0
                total_chars_in_ground_truth = sum(ground_truth_counter.values())  # Total characters in the ground truth

                for char, count in ground_truth_counter.items():
                    if char in extracted_text_counter:
                        total_matches += min(count, extracted_text_counter[char])

                # Calculate the accuracy as the ratio of matched characters to the total number of characters in the ground truth
                accuracy = total_matches / total_chars_in_ground_truth if total_chars_in_ground_truth > 0 else 0.0

                # Append the result to the list
                results.append({
                    column_image_name: image_name,
                    column_value_name: value,  # Use the dynamic column name
                    column_accuracy: accuracy,
                    column_output_text: extracted_text  # Extracted text for reference
                })

    # Create a DataFrame from the results list
    df = pd.DataFrame(results)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_filename, index=False)

    print(f"Results saved to {csv_filename}")

# Example usage
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
