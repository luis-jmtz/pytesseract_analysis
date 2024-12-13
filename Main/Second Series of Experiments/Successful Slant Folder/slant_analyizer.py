import os
from PIL import Image
import pytesseract
import pandas as pd

input_folder = r"Slanted_Images"
output_csv = "slant_analysis.csv"

# Initialize an empty list to store the rows for the CSV
data = []

# Loop through files in the specified folder
for file in os.listdir(input_folder):
    if file.endswith(".png"):
        try:
            # Parse the file name
            parts = file.split("_")
            slant_value = int(parts[0])  # Extract the integer before the first underscore
            name = file  # Use the full file name as "Name"

            # Construct the full path to the image
            image_path = os.path.join(input_folder, file)

            # Open the image and run Tesseract OCR
            img = Image.open(image_path)
            detected_text = pytesseract.image_to_string(img).strip()

            # Determine the "Text Detected" value
            text_detected = 1 if detected_text else 0

            # Append the data to the list
            data.append({
                "Name": name,
                "Slant Value": slant_value,
                "Output": detected_text,
                "Text Detected": text_detected
            })
        except Exception as e:
            print(f"Error processing file {file}: {e}")

# Convert the data to a DataFrame and save it as a CSV
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)

print(f"Processing complete. Data saved to {output_csv}")
