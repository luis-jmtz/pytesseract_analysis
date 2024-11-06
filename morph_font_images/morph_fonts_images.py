import cv2
import os

morph_operations = {
    'dilation': cv2.MORPH_DILATE,
    'erosion': cv2.MORPH_ERODE,
    'opening': cv2.MORPH_OPEN,
    'closing': cv2.MORPH_CLOSE,
    'gradient': cv2.MORPH_GRADIENT,
    'tophat': cv2.MORPH_TOPHAT,
    'blackhat': cv2.MORPH_BLACKHAT
}

def apply_morphological_changes(input_folder, morphtype, kernel_size, output_folder):
    # Check if the given morphtype is valid
    if morphtype not in morph_operations:
        print(f"Invalid morphtype '{morphtype}'. Please choose from: {', '.join(morph_operations.keys())}")
        return

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the kernel for morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    morph_op = morph_operations[morphtype]

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):  # Process only PNG images
            img_path = os.path.join(input_folder, filename)

            # Read the image
            img = cv2.imread(img_path)
            if img is None:
                print(f"Failed to load {filename}. Skipping.")
                continue

            # Apply the morphological transformation
            morphed_img = cv2.morphologyEx(img, morph_op, kernel)

            # Save the transformed image in the output folder with the same filename
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, morphed_img)
            print(f"Applied {morphtype} and saved {filename} to {output_folder}")



# Variables
input_folder = r'normal_font_images'
morphtype = 'dilation'
kernel_size = 3         
output_folder = 'morph_font_images\dilation_kernal3'


# Run the function
apply_morphological_changes(input_folder, morphtype, kernel_size, output_folder)
