from letter_image_generator import LetterImageGenerator


generator = LetterImageGenerator(
        letter="A",
        num_letters=2,
        letter_spacing=1,
        num_iterations=50,
        output_folder="letters2_space1"
    )

generator.generate_images()
