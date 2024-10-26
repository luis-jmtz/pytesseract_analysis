import os
import json
from PIL import Image
import pytesseract

# Specify the folder path
folder_path = 'Temp_image_folder'  # Replace with the path to your folder

# Loop through files in the specified folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Check if the file is an image based on its extension
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        # Extract the base name of the file without extension
        base_name = os.path.splitext(filename)[0]
        
        # Check for a corresponding .json file
        json_file_path = os.path.join(folder_path, f"{base_name}.json")
        
        if os.path.exists(json_file_path):
            try:
                # Open the image file and extract text
                with Image.open(file_path) as img:
                    text = pytesseract.image_to_string(img)
                    print(f"Text extracted from {filename}:\n{text}\n")

                # Open the JSON file, filter out only the "text" values, and join them into a single string
                with open(json_file_path, 'r') as json_file:
                    json_data = json.load(json_file)
                    
                    # Extract only the "text" values, ignoring entries like "%math%" or "%SC%"
                    base_text = ' '.join(item["text"] for item in json_data if item["text"].isalnum())
                    
                    # Print the cleaned text as a single string
                    print(f"Cleaned text from {base_name}.json:\n{base_text}\n")
                    
            except Exception as e:
                print(f"An error occurred with file {filename} or its JSON: {e}")
        else:
            print(f"No JSON file found for {filename}")
