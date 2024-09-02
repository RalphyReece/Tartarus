import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2
import random

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

def generate_sea(shape, threshold, noise_params):
    noise = generate_perlin_noise_2d(shape, **noise_params)
    cave = np.zeros(shape)
    cave[noise > threshold] = 1
    return cave
def main():

    noise_params = {
        'scale': 40,
        'octaves': 6,
        'persistence': .2,
        'lacunarity': 2.0,
        'seed': random.randint(0,1000)
    }


    shape = (56, 100)
    threshold = .1
    cave = generate_sea(shape, threshold, noise_params)
    return cave


