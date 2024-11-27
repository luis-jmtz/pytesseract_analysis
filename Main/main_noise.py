from noise_generator import noiseMaker

noise_strength = 0.0001
snp = noiseMaker(noise_strength)
snp.process_and_save("Control_Image.png")