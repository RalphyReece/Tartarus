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
    def __init__(self, color, posx, posy, name, strength, agility, possessions):
        
        self.shape='☺'
        self.color=color
        self.posx = posx
        self.posy=posy
        self.name = name
        self.strength = strength
        self.agility = agility
        self.time = 0
        self.size=10
        self.possessions =possessions
        self.health=10
        self.pathx=None
        self.pathy=None

        self.overc=0
        self.overyc=0
        
        
        self.speed=3
        self.litter = 1
        self.birth = 3000
        self.task = 'idle'
        self.goal = None

        f=open(str(maindir)+'/fort/dwarves/D-'+str(name)+'.dwarf','w')
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
    def path_to(self,grid_array,x,y):
        self.task ='Pathing'
        q=pathfinding.main(grid_array, (x,y), (12,12))
        
        try:                   
            first_elements = [x[0] for x in q]
            second_elements = [x[1] for x in q]
            self.pathx=first_elements
            self.pathy=second_elements
        except:
            pass
        
        
        
        
        

