import noise
import os
import subprocess
import numpy as np
from noise import pnoise2
import noise
import matplotlib.pyplot as plt
import random
import math
import pathfinding
import time
import cave_gen
import secrets
import river_generation
import sea_generation
import hills
def generate_3d_perlin_noise_grid(x_size, y_size, z_size, scale=0.1, octaves=1, persistence=0.5, lacunarity=2.0, seed=None):
    # Initialize the 3D grid
    grid = np.zeros((x_size, y_size, z_size), dtype=float)

    if seed == None:
        seed=random.randint(0,95)

    # Fill the grid with Perlin noise values
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
                                            base=seed)
                # Normalize the noise to be between 0 and 1
                grid[x][y][z] = (noise_value + 0.5)

    return grid
def ore_probability_curve(x):
    return .19*x +45

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

    



def generate_perlin_noise_2d(shape, res, seed=None):
    scale = 1
    octaves = 6
    persistence = 0.7
    lacunarity = 2.0

    if seed != 'cotton eyed joe':
        seed = int(time.time())  
        seed=random.random()
        

    random.seed(seed)  

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
    
    
def generate_perlin_noise_pool(shape, res, seed):
    scale = 1
    octaves = 6
    persistence = 0.7
    lacunarity = 2.0

        

    random.seed(seed)  

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
    resolution = random.randint(90,95)
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
    resolution = random.randint(80,90)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_copper.data',arr_iron)
def pool_gen(x,y,seed):
    
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(30,52)
    perlin_array = generate_perlin_noise_pool((width, height), resolution,seed)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_pool.data',arr_iron)

def dense_moss_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(10,20)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_moss.data',arr_iron)

def talc_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(30,50)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_talc.data',arr_iron)  



def tin_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(10,32)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_tin.data',arr_iron)
def aluminum_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(10,32)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_aluminum.data',arr_iron)
def mythril_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(80,90)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_mythril.data',arr_iron)
def magnesite_gen(x,y):
    
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(10,32)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_magnesite.data',arr_iron)
    
def fracter_gen(x,y):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    width = x
    height = y
    resolution = random.randint(80,100)
    perlin_array = generate_perlin_noise_2d((width, height), resolution)
    arr_iron = perlin_array
    np.savetxt(str(maindir)+'/region/region_fracter.data',arr_iron)



   

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

def flower_gen(x,y,d):
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
    
    np.savetxt(str(maindir)+'/region/region_flower.data',trees)
def micro_region(biome,elev,stdscr):
    result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
    maindir=result.stdout
    maindir = maindir[:-1]   
    x=60
    x_len=x
    z=40
    z_len=z
    y=60
    y_len=y
    xu=60
    region=np.empty((x,y,z), dtype=object)


    
    for i in range(x):
            for j in range(y):
                for k in range(z):
                    region[i][j][k] = 'slate'
    '''
    if biome == 'plain':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'slate'
    if biome == 'rainforest':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'slate'
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
                region[i][j] = 'slate'
    if biome == 'slop':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'mudstone'
    if biome == 'alpine':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'slate'
    if biome == 'marsh':
        for i in range(x):
            for j in range(y):
                region[i][j] = 'slate'





    '''
    '''
    iron_gen(x,y)
    random.uniform(1,3290)
    
    random.random()
    copper_gen(x,y)
    
    random.random()
    silver_gen(x,y)
    
    gold_gen(x,y)
    random.randint(1,45)
    pool_gen(x,y,random.randint(1,99))

    ##
    tin_gen(x,y)
    r=random.random()
    aluminum_gen(x,y)
    r=random.random()
    magnesite_gen(x,y)
    r=random.random()
    mythril_gen(x,y)


    '''
    ##3D terrain
    q=hills.generate_perlin_noise(x, y, random.randint(0,88), scale=20.0, octaves=4, persistence=0.4, lacunarity=1.5)

    
    if biome == 'forest':
        top='grass'
    elif biome=='rainforest':
        top='bush'
    elif biome=='savannah':
        top='grass'
    elif biome=='alpine':
        top='grass'
    elif biome == 'plain':
        top='grass'
    elif biome =='slop':
        top='mud'
    elif biome=='glacier':
        top='snow'
    else:
        top='sand'
    for i in range(x_len):
        for j in range(y_len):
            for k in range(5):
                region[i][j][k]='air'
    
    for i in range(x_len):
        for j in range(y_len):
            
                #if q[i][j] < .4:
                #region[i][j][5]=top
                if q[i][j] < .55:
                    region[i][j][4]=top
                elif q[i][j] < .7:
                    region[i][j][3]=top
                elif q[i][j] < .85:
                    region[i][j][2]=top
                else:
                    region[i][j][1]=top
    for i in range(x_len):
        for j in range(y_len):
            for k in range(4):
                if region[i][j][k] != 'air':
                    if region[i][j][k+1]=='air':
                        region[i][j][k+1]='slate'
    for i in range(x):
        for j in range(y):
            for k in range(z):
                try:
                    if region[i][j][k]=='grass':
                        if region[i+1][j][k+1]=='grass':
                            region[i+1][j][k]='soil_down_ramp'
                            region[i+1][j][k+1]='soil_up_ramp'
                    if region[i][j][k]=='grass':
                        if region[i-1][j][k+1]=='grass':
                            region[i-1][j][k]='soil_down_ramp'
                            region[i-1][j][k+1]='soil_up_ramp'
                    if region[i][j][k]=='grass':
                        if region[i][j+1][k+1]=='grass':
                            region[i][j+1][k]='soil_down_ramp'
                            region[i][j+1][k+1]='soil_up_ramp'
                    if region[i][j][k]=='grass':
                        if region[i][j-1][k+1]=='grass':
                            region[i][j-1][k]='soil_down_ramp'
                            region[i][j-1][k+1]='soil_up_ramp'
                except:
                    pass
                
    
    
    
    if biome == 'forest':
        sapling_gen(xu,y,100)
        tree_gen(xu,y,50)
        nettle_gen(xu,y,10)
        crabgrass_gen(xu,y,13)
        densegrass_gen(xu,y,5)
    if biome == 'rainforest':
                sapling_gen(xu,y,50)
                tree_gen(xu,y,25)
                nettle_gen(xu,y,13)
                crabgrass_gen(xu,y,20)
                densegrass_gen(xu,y,3)
    if biome == 'desert':
                sapling_gen(xu,y,400)
                tree_gen(xu,y,200)
                crabgrass_gen(xu,y,100)
    if biome == 'glacier':
                nettle_gen(xu,y,130)
                sapling_gen(xu,y,320)
                tree_gen(xu,y,160)
                crabgrass_gen(xu,y,1000)
    if biome == 'alpine':
                sapling_gen(xu,y,120)
                tree_gen(xu,y,60)
                nettle_gen(xu,y,20)
                crabgrass_gen(xu,y,10)
    if biome == 'savannah':
                densegrass_gen(xu,y,62)
                nettle_gen(xu,y,23)
                sapling_gen(xu,y,220)
                tree_gen(xu,y,300)
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
    
                
    
    trees=np.loadtxt(str(maindir)+'/region/region_trees.data')
    for i in range(xu):
        for j in range(y):
            for k in range(6):
                if trees[i][j] == 1 and region[i][j][k]!='slate' and region[i][j][k]!='air':
                    region[i][j][k] = 'tree'
    trees=np.loadtxt(str(maindir)+'/region/region_saplings.data')
    for i in range(xu):
        for j in range(y):
            for k in range(6):
                if trees[i][j] == 1 and region[i][j][k]!='slate' and region[i][j][k]!='air':
            
                    region[i][j][k] = 'sapling'
    trees=np.loadtxt(str(maindir)+'/region/region_nettle.data')
    for i in range(xu):
        for j in range(y):
            for k in range(6):
                if trees[i][j] == 1 and region[i][j][k]!='slate' and region[i][j][k]!='air':
            
                    region[i][j][k] = 'nettle'
    trees=np.loadtxt(str(maindir)+'/region/region_crabgrass.data')
    for i in range(xu):
        for j in range(y):
            for k in range(6):
                if trees[i][j] == 1 and region[i][j][k]!='slate' and region[i][j][k]!='air':
            
                    region[i][j][k] = 'crabgrass'

    
    #ore
    fracter_gen(x,y)
    random.seed(time.time())
    irone=int((100+(3*elev))//1)
    golds=600
    silvers=int(400-(2*elev //1))
    silvere=500
    coppere=420
    coppers=300
    magnesites=600
    magnesitee=int((400+(4*elev))//1)
    mythrils=700
    tins=300
    tine=500
    fracters=270
    fractere=410
    '''
    
    prob=ore_probability_curve(elev)
    r=secrets.randbelow(101)
    if prob >= r:
        trees=np.loadtxt(str(maindir)+'/region/region_iron.data')

        for i in range(irone):
            for j in range(y):
                if trees[i][j] >random.uniform(.14,.28):
                    if region[i][j] == 'slate':
                        region[i][j] = 'iron-ore'

    
    trees=np.loadtxt(str(maindir)+'/region/region_copper.data')
    r=secrets.randbelow(101)
    if prob >= r:
        for i in range(coppere-coppers):
            for j in range(y):
                if trees[i][j] >random.uniform(.07+(2.5/elev),.23):
                    if region[i+coppers][j] == 'slate':
                        region[i+coppers][j] = 'copper-ore'
    
    trees=np.loadtxt(str(maindir)+'/region/region_silver.data')

    r=secrets.randbelow(101)
    if prob >= r:
        for i in range(int(silvere-silvers)):
            for j in range(y):
                if trees[i][j] >random.uniform(.12+(3/elev),.2):
                    if region[i+silvers][j] == 'slate':
                        region[i+silvers][j] = 'silver-ore'
    
    trees=np.loadtxt(str(maindir)+'/region/region_gold.data')
    r=secrets.randbelow(101)
    if prob >= r:
        for i in range(int(x-golds)):
            for j in range(y):
                if trees[i][j] >random.uniform(.15+(2/elev),.3):
                    if region[i+golds][j] == 'slate' or region[i+golds][j] == 'silver-ore':
                        region[i+golds][j] = 'gold-ore'

    trees=np.loadtxt(str(maindir)+'/region/region_tin.data')
    r=secrets.randbelow(101)
    if prob >= r:
        for i in range(int(tine-tins)):
            for j in range(y):
                if trees[i][j] >random.uniform(.12+(2/elev),.3):
                    if region[i+tins][j] == 'slate':
                        region[i+tins][j] = 'tin-ore'
    trees=np.loadtxt(str(maindir)+'/region/region_magnesite.data')
    r=secrets.randbelow(101)
    if prob >= r:
        for i in range(int(magnesitee-magnesites)):
            for j in range(y):
                if trees[i][j] >random.uniform(.12+(2/elev),.35):
                    if region[i+magnesites][j] == 'slate':
                        region[i+magnesites][j] = 'magnesite-ore'

    trees=np.loadtxt(str(maindir)+'/region/region_mythril.data')
    r=secrets.randbelow(101)
    if prob >= r:
        for i in range(int(x-mythrils)):
            for j in range(y):
                if trees[i][j] >random.uniform(.12+(2/elev),.3):
                    if region[i+mythrils][j] == 'slate':
                        region[i+mythrils][j] = 'mythril-ore'
    trees=np.loadtxt(str(maindir)+'/region/region_fracter.data')
    r=secrets.randbelow(101)
    if prob >= r:
        for i in range(int(fractere-fracters)):
            for j in range(y):
                if trees[i][j] >random.uniform(.1,.2):
                    if region[i+fracters][j] == 'slate':
                        region[i+fracters][j] = 'fracter-ore'
    

    '''
    for i in range(xu):
        for j in range(y):
            for k in range(6):
                if region[i][j][k]=='grass':
                    r=random.randint(0,4)
                    if r == 1:
                        region[i][j][k]='sparse_grass'
   
    
    ##
    
    ##
                        
    


    #water pools
    trees=np.loadtxt(str(maindir)+'/region/region_pool.data')
    if biome == 'forest':
        for i in range(x):
                for j in range(y):
                    if trees[i][j] >.25:
                        if region[i][j][4] == 'grass':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'tree':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'sapling':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'nettle':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'crabgrass':
                            region[i][j][4] = 'water'
    if biome == 'marsh':
        for i in range(x):
                for j in range(y):
                    if trees[i][j] >.07:
                        if region[i][j][4] == 'peat':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'tree':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'sapling':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'nettle':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'crabgrass':
                            region[i][j][4] = 'water'
    if biome == 'alpine':
        for i in range(x):
                for j in range(y):
                    if trees[i][j] >.13:
                        if region[i][j][4] == 'grass':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'tree':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'sapling':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'nettle':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'crabgrass':
                            region[i][j][4] = 'water'
    if biome == 'slop':
        for j in range(x):
                for i in range(y):
                    if trees[i][j] >.04:
                        if region[i][j][4] == 'mud':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'tree':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'sapling':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'nettle':
                            region[i][j][4] = 'water'
                        if region[i][j][4] == 'crabgrass':
                            region[i][j][4] = 'water'



    #densegrass creation
    
    if biome == 'forest':
        densegrass_gen(xu,y,5)
        trees=np.loadtxt(str(maindir)+'/region/region_densegrass.data')
        for i in range(xu):
                for j in range(y):
                    for k in range(6):
                        if trees[i][j] ==1:
                            if region[i][j][k] == 'grass':
                                region[i][j][k] = 'densegrass'
                        
   
                        
    if biome == 'alpine':
        densegrass_gen(xu,y,3)
        trees=np.loadtxt(str(maindir)+'/region/region_densegrass.data')
        for i in range(xu):
                for j in range(y):
                    for k in range(6):
                        if trees[i][j] >.18:
                            if region[i][j][k] == 'grass':
                                region[i][j][k] = 'densegrass'
    if biome == 'marsh':
        densegrass_gen(xu,y,2)
        trees=np.loadtxt(str(maindir)+'/region/region_densegrass.data')
        for i in range(xu):
                for j in range(y):
                    for k in range(6):
                        if trees[i][j] >.18:
                            if region[i][j][k] == 'grass':
                                region[i][j][k] = 'densegrass'
    if biome == 'plain':
        densegrass_gen(xu,y,17)
        trees=np.loadtxt(str(maindir)+'/region/region_densegrass.data')
        for i in range(xu):
                for j in range(y):
                    for k in range(6):
                        if trees[i][j] >.18:
                            if region[i][j][k] == 'grass':
                                region[i][j][k] = 'densegrass'
                            
                      
   
                      
     #flowers creation
    if biome == 'forest':
        flower_gen(xu,y,50)
        trees=np.loadtxt(str(maindir)+'/region/region_flower.data')
        for i in range(xu):
                for j in range(y):
                    for k in range(6):
                        if trees[i][j] ==1:
                            if region[i][j][k] == 'grass':
                                region[i][j][k] = 'aerath'
    if biome == 'alpine':
        flower_gen(xu,y,30)
        trees=np.loadtxt(str(maindir)+'/region/region_flower.data')
        for i in range(xu):
                for j in range(y):
                    for k in range(6):
                        if trees[i][j] ==1:
                            if region[i][j][k] == 'grass':
                                region[i][j][k] = 'aerath'
                            
                            

    #cave generation
    #60 and top 100 must be changed in both files
    cavex=0
    scale=.04
    octaves=4
    persistence=.5
    lacunarity=1.5
    for direction in range(1):
        cave=cave_gen.main(x, y, 8, direction, scale, octaves, persistence, lacunarity, seed=random.randint(0,100))

        cave_depth=10
        for j in range(60):
            for i in range(60):
                for k in range(8):
                    if cave[i][j][k] == 1:
                        region[j+cavex][i][cave_depth+k] = 'undiscovered_moss1'
        for j in range(60):
            for i in range(60):
                for k in range(8):
                    if cave[i][j][k] == 2:
                        region[j+cavex][i][cave_depth+k] = 'undiscovered_air'
        for j in range(60):
            for i in range(60):
                for k in range(8):
                    if cave[i][j][k] == 3:
                        region[j+cavex][i][cave_depth+k] = 'undiscovered_down_ramp'
        for j in range(60):
            for i in range(60):
                for k in range(8):
                    if cave[i][j][k] == 4:
                        region[j+cavex][i][cave_depth+k] = 'undiscovered_up_ramp'
    

    tree_gen(x,y,32)
    trees=np.loadtxt(str(maindir)+'/region/region_trees.data')
    for i in range(x):
        for j in range(y):
            for k in range(8):
                if region[i][j][cave_depth+k] == 'undiscovered_moss1':
                    if trees[i][j] == 1:
                        region[i][j][cave_depth+k] = 'fungi-tree'
    flower_gen(x,y,50)
    trees=np.loadtxt(str(maindir)+'/region/region_flower.data')
    for i in range(x):
        for j in range(y):
            for k in range(8):
                if region[i][j][cave_depth+k] == 'undiscovered_moss1':
                    if trees[i][j] == 1:
                        region[i][j][cave_depth+k] = 'undiscovered_rock_bush1'
                            

    dense_moss_gen(x,y)                       
    trees=np.loadtxt(str(maindir)+'/region/region_moss.data')
    
    for i in range(x):
        for j in range(y):
            for k in range(8):
                if region[i][j][cave_depth+k] == 'undiscovered_moss1':
                    if trees[i][j] >=.1:
                        region[i][j][cave_depth+k] = 'undiscovered_dense_moss1'
                            
    
    trees=generate_3d_perlin_noise_grid(x,y,z)                       
    
    
    for i in range(x):
                for j in range(y):
                    for k in range(z):
                        if k < 12:
                            if trees[i][j][k] >.4:
                                if region[i][j][k] == 'slate':
                                    region[i][j][k] = 'talc'
    
    trees=generate_3d_perlin_noise_grid(x,y,z)    
    
    for i in range(x):
                for j in range(y):
                    for k in range(z):
                        if k > 10:
                            if trees[i][j][k] >.4:
                                if region[i][j][k] == 'slate':
                                    region[i][j][k] = 'basalt'    
            
    
    

    for i in range(x-1):
        for j in range(y-1):
            if region[i+1][j][4]=='water' and region[i-1][j][4]=='water':
                region[i][j][4]='water'
    for i in range(x-1):
        for j in range(y-1):
            if region[i][j+1][4]=='water' and region[i][j-1][4]=='water':
                region[i][j][4]='water'
    
        
    region_copy = np.copy(region)
    #river generation
    if elev > 47:
        x, y = 140, 40


        river_array = np.zeros((x, y))


        river_array = river_generation.create_river(river_array)
        r=random.randint(8,22)
        for i in range(xu):
            for j in range(y):
                
                    try:
                        if river_array[i][j] == 1:
                            region[j+r][i][4] = 'river'
                    except:
                        pass
                
    else:
        
        for i in range(20):
            for j in range(60):
                region[i][j][4]='great_sea'
        cave=sea_generation.main()
        for k in range(5):
            for i in range(26):
                for j in range(60):
                    if cave[i][j] >.1+ .03*k:
                        region[i][j][4+k]='great_sea'
        for i in range(80):
            for j in range(100):
                try:
                    if region[i+1][j][4]=='great_sea' or region[i-1][j][4]=='great_sea' or region[i][j+1][4]=='great_sea' or region[i][j-1][4]=='great_sea':
                        r=random.randint(0,100)
                        #if not at least 50 then bad things happen
                        if r > 50:
                            region[i][j][4]='great_sea'
                except:
                    pass
        for i in range(x_len):
            for j in range(y_len):
                cccc=0
                try:
                    if region[i+1][j][4]=='great_sea':
                        cccc+=1
                    if region[i-1][j][4]=='great_sea':
                            cccc+=1
                    if region[i][j+1][4]=='great_sea':
                                cccc+=1
                    if region[i][j-1][4]=='great_sea':
                                    cccc+=1
                    if cccc >=3:
                        region[i][j][4]='great_sea'
                except:
                    pass
        x_2=np.zeros((x_len,y_len))
        ccc=0
        for j in range(x_len):
                ccc+=1
                for i in range(y_len):
                    x_2[j][i]=1
                    
                    if region[j][i][4] == 'great_sea':
                        x_2[j][i] = 0
                        
                        break
        for i in range(x_len):
            for j in range(y_len):
                if region[i][j][4]=='great_sea':
                    region[i][j][3]='air'
                    region[i][j][2]='air'
                    region[i][j][1]='air'
                    region[i][j][0]='air'
        
        
                            
                    
    #Make actual liquid
    for i in range(x_len):
        for j in range(y_len):
            for k in range(z_len):
                if region[i][j][k]=='river':
                    region[i][j][k+1]='water_7/7'
                if k != 4 and region[i][j][k]=='great_sea':
                    region[i][j][k]='water_7/7'
                    
    ##Trees -> multi-tile
    for I in range(8):
        for i in range(x_len):
            for j in range(y_len):
                for k in range(z_len):
                    try:
                        if region[i][j][k]=='tree':
                            region[i][j][k-1]='tree'
                    except:
                        pass
    
                    
        
        '''                
        #Converts intersecting pools to seas. Bad method but faster than pathfinding.
        for b in range(100):
            
            for i in range(xu):
                for j in range(y):
                    try:
                        if region[i][j]=='water':
                            if region[i+1][j] == 'great_sea':
                                region[i][j]='great_sea'
                            elif region[i-1][j] == 'great_sea':
                                region[i][j]='great_sea'
                            elif region[i][j-1] == 'great_sea':
                                region[i][j]='great_sea'
                            elif region[i][j+1] == 'great_sea':
                                region[i][j]='great_sea'
                            
                    except:
                        pass
                    
                        
        '''
        '''
        #SWITCH TO xu y_len after testing ENDS
        #CPU INTENSIVE 
        for i in range(xu):
            if i % 2 == 0:
                stdscr.addstr(15,9,"[")
                stdscr.addstr(15,10+int(xu/2),']')
                
                stdscr.addstr(15,10+int(i/2),'o')
                stdscr.addstr(10,20,"Generating Sea")
                stdscr.refresh()
            for j in range(y_len):
                if region[i][j]=='great_sea':
                
                    #check if sea is cohesive. Eliminate all non-connecting bodies of water.
                        zz=pathfinding.main_short(x_2,(1, 1),(i, j) )
                        if zz == None:
                            region[i][j]=region_copy[i][j]
        #running sea conversions another iteration. maybe removed at some point
        
        for i in range(x_len):
            for j in range(y_len):
                cccc=0
                try:
                    if region[i+1][j]=='great_sea':
                        cccc+=1
                    if region[i-1][j]=='great_sea':
                            cccc+=1
                    if region[i][j+1]=='great_sea':
                                cccc+=1
                    if region[i][j-1]=='great_sea':
                                    cccc+=1
                    if cccc >=3:
                        region[i][j]='great_sea'
                except:
                    pass
        
                            
                        
                            
        
                
                            
                
    


        '''
    region_copy = np.copy(region)
    for i in range(100):
        try:
            for j in range(x_len):
                for k in range(y_len):
                    
                    region_copy[j][k][i]='Formless'
        except:
            pass
    for i in range(100):
        try:
            for j in range(x_len):
                for k in range(y_len):
                    
                    region_copy[j][k][int(2*i)]=region[j][k][i]
        except:
            pass
    #Cave system inter-layer ramp system.
    for i in range(100):
        try:
            for j in range(x_len):
                for k in range(y_len):
                    if region_copy[j][k][i] == 'undiscovered_down_ramp':
                        #if cave layer at bottom layer, will cause issues.
                        region_copy[j][k][i+1] = 'up_ramp'
                    if region_copy[j][k][i]=='soil_down_ramp':
                        region_copy[j][k][i+1]='up_ramp'
                    
                    
        except:
            pass
    
    np.save(str(maindir) + '/region/region.npy', region_copy)
    
    #f=open(str(maindir)+'/dev_data/rcounts'+str(time.time())+'.data','w')

    solids = [
                'tree', 'slate', 'iron-ore', 'copper-ore', 'silver-ore', 'gold-ore', 'mudstone', 'ozone','magnesite-ore','mythril-ore','tin-ore',
                'undiscovered_moss1','fungi-tree','water','undiscovered_rock_bush1','undiscovered_dense_moss1','fracter-ore','grass','sapling'
        ]
    '''
    #resource counter
    for k in solids:
        c=0
        for i in range(x):
            for j in range(y):
                if region[i][j] == k:
                    c+=1
    
        f.write(str(k)+str(c)+'\n')
    f.close
    '''
    
                


    
            

