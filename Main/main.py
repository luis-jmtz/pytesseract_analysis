from vertical_white_space import whiteSpacer

white_space = 1
spacer = whiteSpacer("Control_Image_cropped.png")


while white_space < 101:
    output_file = spacer.add_white_lines(white_space)
    print(f"Output file: {output_file}")
    white_space += 1
