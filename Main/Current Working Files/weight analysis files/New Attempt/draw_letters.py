from PIL import Image, ImageDraw

def draw_letter_a(line_thickness):
    # Image dimensions
    image_width, image_height = 500, 500

    # Create a blank image with white background
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)

    # Dimensions and spacing of the "A"
    a_height = 20  # Height of each "A"
    base_spacing = 12  # Space between the bases of the "A"s
    a_width = a_height // 2  # Proportional width of "A"
    half_width = a_width // 2

    # Calculate horizontal positions for the "A"s
    total_width = 4 * a_width + 3 * base_spacing
    start_x = (image_width - total_width) // 2
    y_top = (image_height - a_height) // 2

    for i in range(4):
        # Base X position of the current "A"
        base_x = start_x + i * (a_width + base_spacing)

        # Points for the "A"
        left_leg = (base_x, y_top + a_height)
        right_leg = (base_x + a_width, y_top + a_height)
        top = (base_x + half_width, y_top)
        crossbar_left = (base_x + a_width // 4, y_top + a_height // 2)
        crossbar_right = (base_x + 3 * a_width // 4, y_top + a_height // 2)

        # Draw the "A"
        draw.line([left_leg, top], fill='black', width=int(line_thickness))
        draw.line([right_leg, top], fill='black', width=int(line_thickness))
        draw.line([crossbar_left, crossbar_right], fill='black', width=int(line_thickness))

    # Save the image
    image.save("letter_as.png")
    print("Image saved as 'letter_as.png'")


thickness = 20
draw_letter_a(thickness)
