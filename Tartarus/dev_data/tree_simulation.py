import random
import matplotlib.pyplot as plt
import math
grass_tiles=7472
strees=240
ssapling=130
sgrass=grass_tiles
tree_update=2000
sapling_update=2000
tree_chance=40000
sapling_chance=80000
sim_hours=240

def f(t,ssapling):
    
    try:
        q=ssapling*(2.71828**(t*math.log(200/ssapling)/1460000))
        if q < 300000000:
            return q
        else:
            return 0
    except:
        return 0
def g(t,ssapling):
    
    try:
        q=ssapling*(2.71828**(t*math.log(360/ssapling)/1460000))
        if q < 300000000:
            return q
        else:
            return 0
    except:
        return 0
sim_time=sim_hours*60


data=[]
for i in range(grass_tiles):
    data.append('grass')
for i in range(strees):
    data.append('tree')
for i in range(ssapling):
    data.append('sapling')
tog_values = []
tot_values = []
tos_values = []
time_values = []
sapling_predicted = []
trees_predicted = []
t=0
t_inc=1000
sim_time *= 60
sim_t_total=sim_time*17
while t < sim_t_total:
    tog=0
    tot=0
    tos=0
    t+=t_inc
    if t % tree_update == 0:
        for j in range(len(data)):
            if data[j] == 'grass':
                r=random.randint(0,tree_chance)
                if r == 1:
                    data[j]='tree'
    if t % sapling_update == 0:
        for j in range(len(data)):
            if data[j] == 'grass':
                r=random.randint(0,sapling_chance)
                if r == 1:
                    data[j]='sapling'
    for j in data:
        if j == 'grass':
            tog+=1
        elif j == 'sapling':
            tos+=1
        elif j == 'tree':
            tot+=1
    if t % 20000 == 0:
        print(str(tog)+'-'+str(tot)+'-'+str(tos)+'-'+str(t))
    if t % t_inc == 0:
        tog_values.append(tog)
        tot_values.append(tot)
        tos_values.append(tos)
        time_values.append(t)
        sapling_predicted.append(f(t,ssapling))
        trees_predicted.append(g(t,strees))

     
plt.figure(figsize=(10, 6))
#plt.plot(time_values, tog_values, label='Grass')
plt.plot(time_values, tot_values, label='Tree')
plt.plot(time_values, tos_values, label='Sapling')
#plt.plot(time_values, sapling_predicted, label='Predictive Saplings')
#plt.plot(time_values, trees_predicted, label='Predictive Trees')
plt.xlabel('Time')
plt.ylabel('Count')
plt.title('Simulation of Trees and Saplings Over Time')
plt.legend()
plt.grid(True)
plt.show()

for i in range(len(tog_values)):
    tog_values[i] /= sgrass
for i in range(len(tot_values)):
    tot_values[i] /= strees
for i in range(len(tos_values)):
    tos_values[i] /= ssapling
for i in range(len(sapling_predicted)):
    sapling_predicted[i] /= f(0,ssapling)
for i in range(len(trees_predicted)):
    trees_predicted[i] /= g(0,strees)
plt.figure(figsize=(10, 6))
#plt.plot(time_values, tog_values, label='Grass')
plt.plot(time_values, tot_values, label='Tree')
plt.plot(time_values, tos_values, label='Sapling')
#plt.plot(time_values, sapling_predicted, label='Predictive Saplings')
#plt.plot(time_values, trees_predicted, label='Predictive Trees')
plt.xlabel('Time')
plt.ylabel('Count')
plt.title('Multiplier')
plt.legend()
plt.grid(True)
plt.show()
