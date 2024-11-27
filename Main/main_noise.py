from noise_generator import noiseMaker

noise_strength = 0.1




while noise_strength < 1:
    snp = noiseMaker(noise_strength)
    snp.process_and_save("Control_Image.png")
    noise_strength += 0.1