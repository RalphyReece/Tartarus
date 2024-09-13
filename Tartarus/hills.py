from noise import snoise2

import numpy as np

def generate_perlin_noise(x, y, seed, scale=10.0, octaves=6, persistence=0.5, lacunarity=2.0):
    array=np.zeros((x,y))
    """
    Generate Perlin noise at coordinates (x, y) with a given seed.

    :param x: The x coordinate.
    :param y: The y coordinate.
    :param scale: The scale of the noise.
    :param octaves: The number of octaves.
    :param persistence: The persistence of the noise.
    :param lacunarity: The lacunarity of the noise.
    :param seed: The seed value for generating noise.
    :return: Noise value between 0 and 1.
    """
    # Generate Perlin noise with the specified seed
    for i in range(x):
        for j in range(y):
            noise_value = snoise2(i / scale, j / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=2048, repeaty=2048, base=seed)

            # Normalize noise value to range 0-1
            normalized_value = (noise_value + 1) / 2
            array[i][j]=normalized_value
    

    return array

# Example usage



