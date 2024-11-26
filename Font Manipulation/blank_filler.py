import os
from PIL import Image

# Path to the folder containing the images
folder_path = "Slanted_Images"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is an image (you can add more extensions if needed)
    if filename.lower().endswith(('.png')):
        try:
            # Open the image
            with Image.open(file_path) as img:
                # Check if the image has an alpha channel (transparency)
                if img.mode == "RGBA":
                    # Create a white background image
                    white_background = Image.new("RGBA", img.size, (255, 255, 255, 255))
                    # Composite the image onto the white background
                    composite = Image.alpha_composite(white_background, img)
                    # Convert back to RGB to remove alpha channel
                    final_image = composite.convert("RGB")
                else:
                    # If no alpha channel, no modification needed
                    final_image = img.convert("RGB")
                
                # Save the modified image back to its original path
                final_image.save(file_path)
                print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
