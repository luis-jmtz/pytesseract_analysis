import cv2
import os


# Variables
input_folder = r'upscaled_font_images_files\normal_font_images'
scale_factor = 1.5
kernel_size = 3     
output_folder = r'upscaled_font_images_files\upscaled_font_images'



def upscale_images(input_folder, scale_factor, kernel_size, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):  # Process only PNG images
            img_path = os.path.join(input_folder, filename)
            
            # Read the image
            img = cv2.imread(img_path)
            if img is None:
                print(f"Failed to load {filename}. Skipping.")
                continue

            # Calculate new dimensions
            new_width = int(img.shape[1] * scale_factor)
            new_height = int(img.shape[0] * scale_factor)
            new_dimensions = (new_width, new_height)

            # Resize (upscale) the image
            upscaled_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_CUBIC)

            # Apply a blur to smooth out the image
            if kernel_size > 1:
                upscaled_img = cv2.GaussianBlur(upscaled_img, (kernel_size, kernel_size), 0)

            # Save the upscaled image to the output folder with the same filename
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, upscaled_img)
            print(f"Upscaled and saved {filename} to {output_folder}")



upscale_images(input_folder, scale_factor, kernel_size, output_folder)
