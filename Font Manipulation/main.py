import os
import csv
import pytesseract
from PIL import Image
from letter_sizeNnumber import LetterImageGenerator

# CSV file path
csv_file = "output_data.csv"


# Initialize constants
letter = "A"
num_letters = 5  # Fixed number of letters
letter_spacing = 1.5  # Fixed letter spacing
output_folder = "output"
max_iterations = 25  # Iterate up to 25 times

# Prepare CSV file
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Font Size", "Number of Letters", "Letter Spacing", "Text Detected"])

    # Loop through iterations
    for iteration in range(1, max_iterations + 1):
        # Generate the images
        generator = LetterImageGenerator(
            letter=letter,
            num_letters=num_letters,
            letter_spacing=letter_spacing,
            num_iterations=iteration,  # Generate images based on the current iteration
            output_folder=output_folder
        )
        generator.generate_images()

        # Process each generated image
        for current_iteration in range(1, iteration + 1):
            # Construct the image file name
            image_file = os.path.join(output_folder, f"{letter}_{current_iteration}_{num_letters}_{letter_spacing}.png")
            
            # Perform OCR with Tesseract
            if os.path.exists(image_file):
                try:
                    ocr_text = pytesseract.image_to_string(Image.open(image_file)).strip()
                    text_detected = 1 if ocr_text else 0  # 1 if OCR detects text, otherwise 0
                except Exception as e:
                    print(f"Error processing {image_file}: {e}")
                    text_detected = 0
            else:
                print(f"Image file not found: {image_file}")
                text_detected = 0

            # Write to the CSV
            writer.writerow([current_iteration, num_letters, letter_spacing, text_detected])

print(f"Data written to {csv_file}")
