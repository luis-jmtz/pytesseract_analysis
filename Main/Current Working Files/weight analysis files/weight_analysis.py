import cv2
import pytesseract
import os
import csv

# Variables
base_truth = "AAAA"
base_thickness = 3.6176470588235294
output_csv = "weight_analysis_v2.csv"
image_folder = "weight_test_images_v2"

# Function to calculate average line thickness
def calculate_average_thickness(image):
    height, width = image.shape
    total_thickness = 0
    line_count = 0

    for row in range(height):
        line_started = False
        line_thickness = 0

        for col in range(width):
            if image[row, col] == 255:  # Black pixel (inverted logic for black lines)
                if not line_started:
                    line_started = True
                    line_thickness = 1
                else:
                    line_thickness += 1
            else:
                if line_started:
                    total_thickness += line_thickness
                    line_count += 1
                    line_started = False

        if line_started:  # Handle lines ending at the row's end
            total_thickness += line_thickness
            line_count += 1

    return total_thickness / line_count if line_count > 0 else 0

# Create CSV and write headers
with open(output_csv, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Image Name", "Weight", "Line Thickness", "Relative Thickness (%)", "OCR Output", "Accuracy (%)"])

    # Process images in the folder
    for image_name in os.listdir(image_folder):
        if image_name.endswith(".png"):
            image_path = os.path.join(image_folder, image_name)

            # Extract weight from image name
            weight = float(image_name.split("_")[1].split(".png")[0])

            # Load the image and binarize
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            # Calculate line thickness
            avg_thickness = calculate_average_thickness(binary_image)

            # Calculate relative thickness
            relative_thickness = ((avg_thickness - base_thickness) / base_thickness) * 100

            # Perform OCR using Tesseract
            ocr_result = pytesseract.image_to_string(image, config="--psm 6").strip()
            
            # Calculate accuracy
            accuracy = sum(1 for a, b in zip(ocr_result, base_truth) if a == b) / len(base_truth) * 100 if base_truth else 0

            # Write to CSV
            writer.writerow([image_name, weight, avg_thickness, relative_thickness, ocr_result, accuracy])

print(f"Processing complete. Results saved to {output_csv}.")
