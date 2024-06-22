import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2

def generate_perlin_noise_2d(shape, scale, octaves, persistence, lacunarity, seed=None):
    if seed is not None:
        np.random.seed(seed)
    noise = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            noise[i][j] = pnoise2(i / scale, 
                                  j / scale, 
                                  octaves=octaves, 
                                  persistence=persistence, 
                                  lacunarity=lacunarity, 
                                  repeatx=1024, 
                                  repeaty=1024, 
                                  base=seed)
    return noise

def generate_cave(shape, threshold, noise_params):
    noise = generate_perlin_noise_2d(shape, **noise_params)
    cave = np.zeros(shape)
    cave[noise > threshold] = 1
    return cave
def main():

    noise_params = {
        'scale': 50,
        'octaves': 20,
        'persistence': 0.64,
        'lacunarity': 6.0,
        'seed': 42
    }


    shape = (30, 200)
    threshold = 0.08
    cave = generate_cave(shape, threshold, noise_params)
    return cave


