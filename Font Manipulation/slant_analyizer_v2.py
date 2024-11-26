import os
from PIL import Image
import pytesseract
import pandas as pd

input_folder = r"Slanted_Images"
output_csv = "output.csv"
base_truth = "AAAA" 

# Function to calculate accuracy without considering position
def calculate_accuracy(base_truth, detected_text):
    # Remove spaces and convert to lists of characters
    base_chars = list(base_truth.replace(" ", ""))
    detected_chars = list(detected_text.replace(" ", ""))

    # Count correct matches regardless of position
    correct_count = 0
    base_count = {char: base_chars.count(char) for char in set(base_chars)}
    detected_count = {char: detected_chars.count(char) for char in set(detected_chars)}

    for char in base_count:
        if char in detected_count:
            correct_count += min(base_count[char], detected_count[char])

    # Penalize for mismatched length
    total_possible = max(len(base_chars), len(detected_chars))
    accuracy = correct_count / total_possible if total_possible > 0 else 0
    return round(accuracy * 100, 2)  # Return percentage rounded to 2 decimal places

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

            # Calculate accuracy
            accuracy = calculate_accuracy(base_truth, detected_text)

            # Append the data to the list
            data.append({
                "Name": name,
                "Slant Value": slant_value,
                "Output": detected_text,
                "Text Detected": text_detected,
                "Accuracy": accuracy
            })
        except Exception as e:
            print(f"Error processing file {file}: {e}")

# Convert the data to a DataFrame and save it as a CSV
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)

print(f"Processing complete. Data saved to {output_csv}")
