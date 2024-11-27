from noise_generator import noiseMaker

noise_strength = 0.09




while noise_strength < 1.01:
    snp = noiseMaker(noise_strength)
    snp.process_and_save("Control_Image.png")
    noise_strength += 0.01