import numpy as np
import noise
import random

def main(x_size, y_size, z_size,direction, scale, octaves, persistence, lacunarity, seed=None):
    # Initialize the 3D grid with zeros
    grid = np.zeros((x_size, y_size, z_size), dtype=int)

    if seed:
        np.random.seed(seed)
        seed_value = np.random.randint(0, 100)
    else:
        seed_value=0  # Default seed

    # Step 1: Fill the grid with 1 where Perlin noise > 0.2
    if direction == 0:
        ths=[.0001,.03,.05,.1,.15,.2,.3,.5,1.2]
        
    
            
    for x in range(x_size):
        for y in range(y_size):
            for z in range(z_size):
                noise_value = noise.pnoise3(x * scale,
                                            y * scale,
                                            z * scale,
                                            octaves=octaves,
                                            persistence=persistence,
                                            lacunarity=lacunarity,
                                            repeatx=x_size,
                                            repeaty=y_size,
                                            repeatz=z_size,
                                            base=seed_value)
                
                threshhold=ths[z]
                if noise_value > threshhold:
                    grid[x][y][z] = 1
                
    if direction == 0:
        
        # Step 2: Identify air cells (set to 2)
        for x in range(x_size):
            for y in range(y_size):
                for z in range(0, z_size):  # Start at z=1 to avoid out of bounds
                    try:
                        # If current cell is 1 and the cell directly below is also 1, set current cell to 2 (air)
                        if grid[x][y][z] == 1 and grid[x][y][z + 1] == 1:
                            grid[x][y][z] = 2
                    except:
                        pass
        for x in range(x_size):
            for y in range(y_size):
                for z in range(0, z_size):
                    try:
                    
                        if grid[x][y][z] == 1:
                            if grid[x+1][y][z + 1] == 1:
                                grid[x][y][z] = 3
                                grid[x][y][z+1] = 4
                        if grid[x][y][z] == 1:
                            if grid[x-1][y][z + 1] == 1:
                                grid[x][y][z] = 3
                                grid[x][y][z+1] = 4
                        if grid[x][y][z] == 1:
                            if grid[x][y+1][z + 1] == 1:
                                grid[x][y][z] = 3
                                grid[x][y][z+1] = 4
                        if grid[x][y][z] == 1:
                            if grid[x][y-1][z + 1] == 1:
                                grid[x][y][z] = 3
                                grid[x][y][z+1] = 4
                    except:
                        pass
        
    return grid

# Example usage

