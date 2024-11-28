import os
import csv
import pytesseract
from PIL import Image
import pandas as pd

# Input folder containing the images
input_folder = r"perlin_images2-2"
# Output CSV file
output_csv = "perlin_noise_analysis2-2.csv"
# Base truth for comparison
base_truth = "AAAA"
# Data list to store rows for the CSV
data = []

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".png"):
            try:
                # Extract noise strength (number before "_") and round to the fourth decimal place
                noise_strength = round(float(file.split("_")[0]), 4)
                image_path = os.path.join(root, file)

                # Open the image
                img = Image.open(image_path)
                # Perform OCR
                
                print(image_path + " opened")
                
                detected_text = pytesseract.image_to_string(img).strip()

                # Determine if any text was detected
                text_detected = 1 if detected_text else 0

                # Compare detected text with the base truth
                detected_text_array = list(detected_text)
                base_truth_array = list(base_truth)

                # Calculate the number of matched characters
                matched_chars = sum(1 for i, char in enumerate(detected_text_array) 
                                    if i < len(base_truth_array) and char == base_truth_array[i])
                # Compute accuracy
                accuracy = matched_chars / len(base_truth_array) if base_truth_array else 0

                # Append data row
                data.append({
                    "Noise Strength": noise_strength,
                    "Text Detected": text_detected,
                    "OCR Output": detected_text,
                    "Accuracy": round(accuracy * 100, 2)
                })
            except Exception as e:
                print(f"Error processing file {file}: {e}")

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)

print(f"Analysis Complete")

