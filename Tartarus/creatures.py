import random
class Creature:
    def __init__(self, shape, color, posx, posy, name, strength, agility, size, speed, litter, birth,stalking,health,state,behav):
        
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
        self.stalking = stalking
        self.state=state
        self.behav=behav
        
        
        self.speed = speed
        self.litter = litter
        self.birth = birth
        
    
    def update_pos(self):
        r=random.randint(1,3)
        if r == 1:
            x=random.randint(-1*self.speed,self.speed)
            y=random.randint(-1*self.speed,self.speed)
        
            self.oldposx=self.posx
            self.posx += x
            self.oldposy=self.posy
            self.posy += y
    def px(self):
        return self.posx
    def py(self):
        return self.posy
    def age(self):
        self.time += 1
    def goto(x,y):
        self.posx=x
        self.posy=y
    
        

    

# Creating instances of creatures

class Dwarf:
    def __init__(self, shape, color, posx, posy, name, strength, agility, size, speed, litter, birth, possessions):
        
        self.shape=shape
        self.color=color
        self.posx = posx
        self.posy=posy
        self.name = name
        self.strength = strength
        self.agility = agility
        self.time = 0
        self.size=size
        self.possessions =possessions
        
        
        self.speed = speed
        self.litter = litter
        self.birth = birth
        
    
    def update_pos(self):
        r=random.randint(1,3)
        if r == 1:
            x=random.randint(-1*self.speed,self.speed)
            y=random.randint(-1*self.speed,self.speed)
        
            self.oldposx=self.posx
            self.posx += x
            self.oldposy=self.posy
            self.posy += y
    def px(self):
        return self.posx
    def py(self):
        return self.posy
    def age(self):
        self.time += 1
    def goto(x,y):
        self.posx=x
        self.posy=y

