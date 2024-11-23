from letter_image_generator import LetterImageGenerator


generator = LetterImageGenerator(
        letter="A",
        num_letters=4,
        letter_spacing=4,
        num_iterations=50,
        output_folder="letters4_space4"
    )

generator.generate_images()
