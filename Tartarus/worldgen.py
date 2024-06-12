import noise
import os
import subprocess
import numpy as np
from noise import pnoise2
import matplotlib.pyplot as plt
import random
import math
import time


def simulate_rain(arr,shape,years):
    for k in range(years):
        for i in range(shape[0]):
            for j in range(shape[1]):
                arr[i][j]*=random.uniform(.99,1.01)
    return arr
    


def perlin_array(years=200, shape = (600, 1200),
			scale=100, octaves = 6, 
			persistence = .5, 
			lacunarity = 2.0, 
			seed = None):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   

    if not seed:

        seed = np.random.randint(0, 100000)
        print("seed was {}".format(seed))

    arr = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            arr[i][j] = pnoise2(i / scale,
                                        j / scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=1024,
                                        repeaty=1024,
                                        base=seed)
    max_arr = np.max(arr)
    min_arr = np.min(arr)
    norm_me = lambda x: (x-min_arr)/(max_arr - min_arr)
    norm_me = np.vectorize(norm_me)
    arr = norm_me(arr)
    arr*=90

    #save data
    
    np.savetxt(str(maindir)+'/world/world_elev.data',arr)

    #save graphic
    perlin_img=arr

    f=open(str(maindir)+'/world/graphic.data','w')
    for i in range(shape[0]):
        line=''
        for j in range(shape[1]):
        
            if perlin_img[i][j] < 10:
                line += '.'
            elif perlin_img[i][j] < 20:
                line += ','
            elif perlin_img[i][j] < 30:
                line += ':'
            elif perlin_img[i][j] < 40:
                line += ';'
            elif perlin_img[i][j] < 50:
                line += '+'
            elif perlin_img[i][j] < 60:
                line += '*'
            elif perlin_img[i][j] < 70:
                line += '%'
            elif perlin_img[i][j] < 80:
                line += '#'
            else:
                line += '@'
        f.write(line+'\n')
    f.close()
        
    #rainfall      

    arr_rain = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            arr_rain[i][j] = pnoise2(i / scale,
                                        j / scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=1024,
                                        repeaty=1024,
                                        base=seed+random.randint(1,8))
    max_arr = np.max(arr_rain)
    min_arr = np.min(arr_rain)
    norm_me = lambda x: (x-min_arr)/(max_arr - min_arr)
    norm_me = np.vectorize(norm_me)
    arr_rain = norm_me(arr_rain)

    new_rain=simulate_rain(arr_rain,shape,years)
    np.savetxt(str(maindir)+'/world/world_rain.data',new_rain)

    f=open(str(maindir)+'/world/world_size.data','w')
    f.write(str(shape[0])+'x'+str(shape[1]))
    f.close()



    #temp

    arr_temp = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            arr_temp[i][j] = pnoise2(i / scale,
                                        j / scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=1024,
                                        repeaty=1024,
                                        base=seed+1)
    max_arr = np.max(arr_temp)
    min_arr = np.min(arr_temp)
    norm_me = lambda x: (x-min_arr)/(max_arr - min_arr)
    norm_me = np.vectorize(norm_me)
    arr_temp = norm_me(arr_temp)

    np.savetxt(str(maindir)+'/world/world_temp.data',arr_temp)

    
#update as game development progresses
#To do: River,Cave,Lava,Fun

def generate_perlin_noise_2d(shape, res, seed=None):
    scale = 1
    octaves = 6
    persistence = 0.7
    lacunarity = 2.0

    if seed != 'cotton eyed joe':
        seed = int(time.time())  # Generate a random seed if none is provided
        seed=random.random()
        

    random.seed(seed)  # Set the seed for the noise function

    world = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i / res,
                                         j / res,
                                         octaves=octaves,
                                         persistence=persistence,
                                         lacunarity=lacunarity,
                                         repeatx=1024,
                                         repeaty=1024,
                                         base=0) * scale
    return world
    
    
    
    
def iron_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(7,12)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_iron.data',arr_iron)
def gold_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(10,32)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_gold.data',arr_iron)
def silver_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = 10
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_silver.data',arr_iron)
def copper_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(10,50)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_copper.data',arr_iron)
def pool_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(10,30)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_pool.data',arr_iron)
    
    

def tree_gen(x,y,d):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    trees = np.zeros((x,y), dtype=object)
    x=int(x)
    y=int(y)
    
    
    d=int(d)
    trees = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            r=random.randint(1,d)
            if r == 1:
                trees[i][j] = 1
    
    np.savetxt(str(maindir)+'/region/region_trees.data',trees)
def sapling_gen(x,y,d):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    trees = np.zeros((x,y), dtype=object)
    x=int(x)
    y=int(y)
    d=int(d)
    trees = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            r=random.randint(1,d)
            if r == 1:
                trees[i][j] = 1


    np.savetxt(str(maindir)+'/region/region_saplings.data',trees)
def nettle_gen(x,y,d):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    trees = np.zeros((x,y), dtype=object)
    x=int(x)
    y=int(y)
    d=int(d)
    trees = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            r=random.randint(1,d)
            if r == 1:
                trees[i][j] = 1
    
    np.savetxt(str(maindir)+'/region/region_nettle.data',trees)
def crabgrass_gen(x,y,d):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    trees = np.zeros((x,y), dtype=object)
    x=int(x)
    y=int(y)
    d=int(d)
    trees = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            r=random.randint(1,d)
            if r == 1:
                trees[i][j] = 1
    
    np.savetxt(str(maindir)+'/region/region_crabgrass.data',trees)

def densegrass_gen(x,y,d):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    trees = np.zeros((x,y), dtype=object)
    x=int(x)
    y=int(y)
    d=int(d)
    trees = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            r=random.randint(1,d)
            if r == 1:
                trees[i][j] = 1
    
    np.savetxt(str(maindir)+'/region/region_densegrass.data',trees)
def micro_region(biome,elev):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    x=180
    y=60
    xu=150
    region=np.empty((x,y), dtype=object)


    if biome == 'forest':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'stone'
    if biome == 'plain':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'stone'
    if biome == 'rainforest':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'stone'
    if biome == 'glacier':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'ozone'
    if biome == 'desert':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'sandstone'
    if biome == 'savannah':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'stone'
    if biome == 'slop':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'mudstone'
    if biome == 'alpine':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'stone'
    if biome == 'marsh':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'stone'






    iron_gen(x,y)
    random.uniform(1,3290)
    time.sleep(1)
    random.random()
    copper_gen(x,y)
    time.sleep(1)
    random.random()
    silver_gen(x,y)
    time.sleep(1)
    gold_gen(x,y)
    random.randint(1,45)
    pool_gen(x,y)


    
    if biome == 'forest':
        sapling_gen(xu,y,100)
        tree_gen(xu,y,50)
        nettle_gen(xu,y,10)
        crabgrass_gen(xu,y,13)
        densegrass_gen(xu,y,5)
    if biome == 'rainforest':
                sapling_gen(xu,y,50)
                tree_gen(xu,y,25)
                crabgrass_gen(xu,y,20)
                densegrass_gen(xu,y,3)
    if biome == 'desert':
                sapling_gen(xu,y,400)
                tree_gen(xu,y,200)
                crabgrass_gen(xu,y,100)
    if biome == 'glacier':
                sapling_gen(xu,y,320)
                tree_gen(xu,y,160)
                crabgrass_gen(xu,y,1000)
    if biome == 'alpine':
                sapling_gen(xu,y,120)
                tree_gen(xu,y,60)
                nettle_gen(xu,y,20)
                crabgrass_gen(xu,y,10)
    if biome == 'savannah':
                sapling_gen(xu,y,220)
                tree_gen(xu,y,110)
                nettle_gen(xu,y,50)
                crabgrass_gen(xu,y,10)
    if biome == 'marsh':
                sapling_gen(xu,y,152)
                tree_gen(xu,y,76)
                nettle_gen(xu,y,9)
                crabgrass_gen(xu,y,12)
    if biome == 'slop':
                sapling_gen(xu,y,206)
                tree_gen(xu,y,103)
                nettle_gen(xu,y,90)
                crabgrass_gen(xu,y,108)
    if biome == 'plain':
                sapling_gen(xu,y,240)
                tree_gen(xu,y,120)
                crabgrass_gen(xu,y,6)
                densegrass_gen(xu,y,50)
    for i in range(xu):
        for j in range(y):
            if biome == 'forest':
               
                region[i][j]='grass'
            if biome == 'rainforest':
               
                region[i][j]='bush'
            if biome == 'desert':
            
                region[i][j]='sand'
            if biome == 'glacier':
               
                region[i][j]='snow'
            if biome == 'alpine':
               
                region[i][j]='grass'
            if biome == 'savannah':
               
                region[i][j]='dead shrub'
            if biome == 'marsh':
               
                region[i][j]='peat'
            if biome == 'slop':
                
                region[i][j]='mud'
            if biome == 'plain':
               
                region[i][j]='grass'
    trees=np.loadtxt(str(maindir)+'/region/region_trees.data')
    for i in range(xu):
        for j in range(y):
            if trees[i][j] == 1:
                region[i][j] = 'tree'
    trees=np.loadtxt(str(maindir)+'/region/region_saplings.data')
    for i in range(xu):
        for j in range(y):
            if trees[i][j] == 1:
                region[i][j] = 'sapling'
    trees=np.loadtxt(str(maindir)+'/region/region_nettle.data')
    for i in range(xu):
        for j in range(y):
            if trees[i][j] == 1:
                region[i][j] = 'nettle'
    trees=np.loadtxt(str(maindir)+'/region/region_crabgrass.data')
    for i in range(xu):
        for j in range(y):
            if trees[i][j] == 1:
                region[i][j] = 'crabgrass'


    #ore
                
    trees=np.loadtxt(str(maindir)+'/region/region_iron.data')

    for i in range(x):
        for j in range(y):
            if trees[i][j] >random.uniform(.2,.3):
                if region[i][j] == 'stone':
                    region[i][j] = 'iron-ore'

    if elev > 60:
        trees=np.loadtxt(str(maindir)+'/region/region_copper.data')

        for i in range(x):
            for j in range(y):
                if trees[i][j] >random.uniform(.07,.32):
                    if region[i][j] == 'stone':
                        region[i][j] = 'copper-ore'
    if elev > 70:
        trees=np.loadtxt(str(maindir)+'/region/region_silver.data')

        for i in range(x):
            for j in range(y):
                if trees[i][j] >random.uniform(.15,.38):
                    if region[i][j] == 'stone':
                        region[i][j] = 'silver-ore'
    if elev > 80:
        trees=np.loadtxt(str(maindir)+'/region/region_gold.data')

        for i in range(x):
            for j in range(y):
                if trees[i][j] >random.uniform(.45,.699):
                    if region[i][j] == 'stone':
                        region[i][j] = 'gold-ore'



    #wagon
    region[10][10]='wood-wall'
    region[10][11]='wood-wall'
    region[10][12]='wood-wall'
    region[11][10]='wood-wall'
    region[12][10]='wood-wall'
    region[13][10]='wood-wall'
    region[10][13]='wood-wall'
    region[13][10]='wood-wall'
    region[13][11]='wood-wall'
    region[13][12]='wood-wall'
    
    region[13][13]='wood-wall'


    #water pools
    trees=np.loadtxt(str(maindir)+'/region/region_pool.data')
    if biome == 'forest':
        for i in range(x):
                for j in range(y):
                    if trees[i][j] >.2:
                        if region[i][j] == 'grass':
                            region[i][j] = 'water'
                        if region[i][j] == 'tree':
                            region[i][j] = 'water'
                        if region[i][j] == 'sapling':
                            region[i][j] = 'water'
                        if region[i][j] == 'nettle':
                            region[i][j] = 'water'
    if biome == 'marsh':
        for i in range(x):
                for j in range(y):
                    if trees[i][j] >.07:
                        if region[i][j] == 'peat':
                            region[i][j] = 'water'
                        if region[i][j] == 'tree':
                            region[i][j] = 'water'
                        if region[i][j] == 'sapling':
                            region[i][j] = 'water'
                        if region[i][j] == 'nettle':
                            region[i][j] = 'water'
    if biome == 'alpine':
        for i in range(x):
                for j in range(y):
                    if trees[i][j] >.13:
                        if region[i][j] == 'grass':
                            region[i][j] = 'water'
                        if region[i][j] == 'tree':
                            region[i][j] = 'water'
                        if region[i][j] == 'sapling':
                            region[i][j] = 'water'
                        if region[i][j] == 'nettle':
                            region[i][j] = 'water'
    if biome == 'slop':
        for j in range(x):
                for i in range(y):
                    if trees[i][j] >.04:
                        if region[i][j] == 'mud':
                            region[i][j] = 'water'
                        if region[i][j] == 'tree':
                            region[i][j] = 'water'
                        if region[i][j] == 'sapling':
                            region[i][j] = 'water'
                        if region[i][j] == 'nettle':
                            region[i][j] = 'water'



    #densegrass creation
    
    if biome == 'forest':
        densegrass_gen(xu,y,5)
        trees=np.loadtxt(str(maindir)+'/region/region_densegrass.data')
        for i in range(xu):
                for j in range(y):
                    if trees[i][j] ==1:
                        if region[i][j] == 'grass':
                            region[i][j] = 'densegrass'
                        
   
                        
    if biome == 'alpine':
        densegrass_gen(xu,y,3)
        trees=np.loadtxt(str(maindir)+'/region/region_densegrass.data')
        for i in range(xu):
                for j in range(y):
                    if trees[i][j] >.18:
                        if region[i][j] == 'grass':
                            region[i][j] = 'densegrass'
                      
   
                      
                            
                            


    

    
    
        
    




                
    np.savetxt(str(maindir)+'/region/region.data',region,fmt='%s')



    
            

