#https://www.geeksforgeeks.org/python-noise-function-in-wand/

# wand image effects: https://docs.wand-py.org/en/0.6.12/guide/effect.html

import wand
from wand.image import Image
from wand.display import display

'''Types of Noise:
gaussian
impulse
laplacian
multiplicative_gaussian
poisson
random
uniform
'''

# The amount of noise can be adjusted by passing an 
# attenuate kwarg where the value can be between 0.0 and 1.0.

# Parameters
#wand.image.noise(noise_type, attenuate, channel)


# Read image using Image() function
with Image(filename ="OpenDyslexic-Bold-Italic.png") as img:
 
    # Generate noise image using noise() function
    img.noise("uniform", attenuate = 0.9)
    img.save(filename = r"wand noise images\uniform0.9_OpenDyslexic-Bold-Italic.png")
