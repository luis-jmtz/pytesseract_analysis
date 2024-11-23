import os
import csv
import pytesseract
from PIL import Image
from letter_sizeNnumber import LetterImageGenerator


# Parameters
letter = "A"
num_letters = 1
letter_spacing = 0
output_folder = "output"
iterations = 10
csv_file = "output_data.csv"

generator = LetterImageGenerator(letter, num_letters, letter_spacing, iterations, output_folder)

# Step 2: Perform OCR and Write Results to CSV
print("Performing OCR and writing results to CSV...")
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write the CSV header
    writer.writerow(["Font Size", "Number of Letters", "Letter Spacing", "Text Detected"])

    # Loop through the images in the output folder
    for filename in sorted(os.listdir(output_folder)):
        if filename.endswith(".png"):
            # Extract metadata from the filename
            parts = filename.replace(".png", "").split("_")
            font_size = int(parts[1])  # Extract iteration (used as font size)
            num_letters = int(parts[2])  # Extract number of letters
            letter_spacing = float(parts[3])  # Extract letter spacing

            # Perform OCR on the image
            image_path = os.path.join(output_folder, filename)
            try:
                ocr_text = pytesseract.image_to_string(Image.open(image_path)).strip()
                text_detected = 1 if ocr_text else 0  # 1 if OCR detects text, 0 otherwise
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                text_detected = 0

            # Write the row to the CSV
            writer.writerow([font_size, num_letters, letter_spacing, text_detected])

print(f"Data written to {csv_file}")
