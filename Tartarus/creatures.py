import random
import subprocess
import pathfinding
result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
maindir=result.stdout
maindir = maindir[:-1]
class Creature:
    def __init__(self, shape, color, posx, posy, name, strength, agility, size, speed, litter, birth,tame,health,state,behav):
        
        self.shape=shape
        self.golex=None
        self.goley=None
        self.health = health
        self.color=color
        self.posx = posx
        self.posy=posy
        self.name = name
        self.strength = strength
        self.agility = agility
        self.time = 1
        self.size=size
        self.tame = tame
        self.state=state
        self.behav=behav
        
        
        self.speed = speed
        self.litter = litter
        self.birth = birth
        
    
    def update_pos(self):
        r=random.randint(1,2)
        if r == 1:
            x=random.randint(-1,1)
            y=random.randint(-1,1)
        
            self.oldposx=self.posx
            self.oldposy=self.posy
            return [self.posx+x,self.posy+y]
        else:
            return [self.posx,self.posy]
            
    def px(self):
        return self.posx
    def py(self):
        return self.posy
    def age(self):
        self.time += 1
    def goto(self,x,y):
        self.posx=x
        self.posy=y
    
        

    

# Creating instances of creatures

class Dwarf:
    def __init__(self, color, posx, posy, name, strength, agility, birth, possessions):
        
        self.shape='D'
        self.color=color
        self.posx = posx
        self.posy=posy
        self.name = name
        self.strength = strength
        self.agility = agility
        self.time = 0
        self.size=10
        self.possessions =possessions
        
        
        
        self.speed=3
        self.litter = 1
        self.birth = birth
        self.task = 'idle'

        f=open(str(maindir)+'/dwarves/D-'+str(name)+'.dwarf','w')
        f.close()
        
    
    def update_pos(self):
        r=random.randint(1,2)
        if r == 1:
            x=random.randint(-1,1)
            y=random.randint(-1,1)
        
            self.oldposx=self.posx
            self.oldposy=self.posy
            return [self.posx+x,self.posy+y]
        else:
            return [self.posx,self.posy]
    
    def px(self):
        return self.posx
    def py(self):
        return self.posy
    def age(self):
        self.time += 1
    def goto(self,x,y):
        self.posx=x
        self.posy=y
    def path_to(grid_array,x,y):
        self.task ='Pathing'
        dwarf_path(str(maindir)+'/region/pathfind.data', (self.posx,self.posy), (x,y),'D-'+str(name)+'.dwarf')
        
        
        
        

