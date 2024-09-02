import random
import math
def wave_frequency(t):
    return math.sin(
def start_wave(seed,ymax,t):
    
    random.seed(seed)
    y_elev=random.randint(0,ymax)
    angle=random.choice(-60,-45,-30,0,30,45,60)
    return [y_elev,angle]
