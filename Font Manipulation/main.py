from letter_image_generator import LetterImageGenerator


output_folder="size_output"

letter = "A"

#                               (letter, num_letters, letter_spacing, num_iterations, output_folder):
generator = LetterImageGenerator(letter, 1, 0, 50, output_folder)
generator.generate_images()

