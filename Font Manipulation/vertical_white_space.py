from PIL import Image

def add_white_lines_to_image(image_path, num_lines):
    try:
        # Open the original image
        img = Image.open(image_path)
        width, height = img.size  # Get the dimensions of the original image

        # New dimensions with `num_lines` white lines on top and bottom
        new_height = height + (2 * num_lines)
        new_width = width

        # Create a new image with a white background
        new_img = Image.new("RGB", (new_width, new_height), "white")

        # Paste the original image onto the new image
        new_img.paste(img, (0, num_lines))  # Paste at (0, num_lines) for proper padding

        # Generate output file name based on `num_lines` parameter
        output_path = f"{num_lines}_whiteSpace.png"
        new_img.save(output_path)

        print(f"Image saved successfully to {output_path}")
        return output_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


input_image = "Control_Image_cropped.png"
num_lines = 5
add_white_lines_to_image(input_image, num_lines)
