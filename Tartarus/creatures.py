import random
import subprocess
import pathfinding
import numpy as np
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
    def __init__(self, color, posx, posy, name, strength, agility, possessions, professions):
        
        self.professions=professions
        self.iposx=posx
        self.iposy=posy
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
        self.q=None
        self.first_elements=None
        self.second_elements=None
        
        

        self.overc=0
        self.overyc=0
        
        
        self.speed=10
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
             
             
            self.pathx=first_elements
            self.pathy=second_elements
        except:
            pass
    def get_goal(self):
        return self.goal
    def set_goal(self,x):
        self.goal=x
    def add_possession(self,x):
        self.possessions.append(x)
    def task_detect(self,tasks,x,t,X,Y):
        
                    if 'axe' in self.possessions and 'woodcutter' in self.professions:
                        for j in range(X):
                            for k in range(Y):
                                if tasks[j][k]==2:
                                    self.set_goal('chop chop')
                                    
                    if 'pickaxe' in self.possessions and 'miner' in self.professions:
                        for j in range(X):
                            for k in range(Y):
                                if tasks[j][k]==1:
                                    self.set_goal('mine')
                
                            
                
                    if self.task == 'idle':
                            if t % self.speed == 0:
                                self.age()
                                qq=self.update_pos()
                                try:
                                        if x[qq[1]+over, qq[0]+overy] not in solids:
                                                self.goto(qq[0],qq[1])
                                except:



                                        pass


    def get_the_path(self,X,Y,tasks,over,overy,maindir):
                            qqq= self.get_goal()
                            
                            if qqq=='mine':
                                c=0
                                for j in range(X):
                                    for k in range(Y):
                                        
                                        if tasks[j][k]== 1:

                                     
                                            self.task='Path'
                                              
                                            if c != 1:    
                                                
                                                
                                                try:
                                                    q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),( self.posy+over,  self.posx+overy),(j-1, k) )
                                                     
                                                     
                                                    c=1
                                                except:
                                                    pass
                                            if c != 1:
                                                try:
                                                    q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),( self.posy+over,  self.posx+overy),(j+1, k) )
                                                     
                                                     
                                                    c=1
                                                except:
                                                    pass
                                            if c != 1:
                                                try:
                                                    q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),( self.posy+over,  self.posx+overy),(j, k+1) )
                                                     
                                                     
                                                    c=1
                                                except:
                                                    pass
                                            if c != 1:
                                                try:
                                                    q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),( self.posy+over,  self.posx+overy),(j, k-1) )
                                                     
                                                     
                                                    c=1
                                                except:
                                                    pass
                                            if c == 0:
                                                
                                                    
                                                   
                                                 self.task='idle'
                                            if c != 0:
                                                return q
                            if qqq=='chop chop':
                                c=0
                                for j in range(X):
                                    for k in range(Y):
                                        
                                        if tasks[j][k]== 2:

                                     
                                            self.task='Path'
                                              
                                            if c != 1:    
                                                
                                                
                                                try:
                                                    q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),( self.posy+over,  self.posx+overy),(j-1, k) )
                                                     
                                                     
                                                    c=1
                                                except:
                                                    pass
                                            if c != 1:
                                                try:
                                                    q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),( self.posy+over,  self.posx+overy),(j+1, k) )
                                                     
                                                     
                                                    c=1
                                                except:
                                                    pass
                                            if c != 1:
                                                try:
                                                    q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),( self.posy+over,  self.posx+overy),(j, k+1) )
                                                     
                                                     
                                                    c=1
                                                except:
                                                    pass
                                            if c != 1:
                                                try:
                                                    q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),( self.posy+over,  self.posx+overy),(j, k-1) )
                                                     
                                                     
                                                    c=1
                                                except:
                                                    pass
                                            if c == 0:
                                                    q=None
                                                    first_elements = None
                                                    second_elements = None
                                                    
                                                    self.task='idle'
                                            if c != 0:
                                                return q
    
    def path(self,over,overy,playing,t):
        
                            
                            if self.q != None:
                                first_elements = [x[0] for x in self.q]
                                second_elements = [x[1] for x in self.q]
                                
                                self.pathx=first_elements
                                self.pathy=second_elements
                            else:
                                pass
                            
                                    
                                
                                
                            
                            try:
                                if playing % 2 == 1:
                                    if t % 5 == 0:
                                    
                                        #if abs( self.pathy[1]- self.posx)<=2:
                                        self.goto(self.pathy[1]-overy,self.pathx[1]-over)
                                      
                                        del self.pathx[0]
                                        del self.pathy[0]
                                    
                            except:
                                return 'success'
                                '''
                                if qqq == 'get-wood':
                                
                                     self.add_possession('wood')
                                    items[ self.posx][ self.posy]=0
                                     self.task='idle'
                                     self.posx+=1
                                     self.set_goal(None)
                    
                                     self.posx+=1
                                     self.set_goal(None)
                                if  self.get_goal() == 'mine':
                                    yy= self.posx+overy
                                    xx= self.posy+over
                                    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # Up, Down, Right, Left

                                    for dx, dy in directions:
                                        nx, ny = xx + dx, yy + dy
    
                                        if 0 <= nx < len(tasks) and 0 <= ny < len(tasks[1]) and tasks[nx][ny] == 1:
                                            tasks[nx][ny] = 0
        
                                            if x[nx][ny] == 'stone':
                                                x[nx][ny] = 'grass'
                                                r=random.randint(1,4)
                                                if r == 2:
                                                    items[nx][ny]=2
            
                                            break 
                                     self.task='idle'
                                     self.set_goal(None)
                                if  self.get_goal() == 'chop chop':
                                    yy= self.posx+overy
                                    xx= self.posy+over
                                    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # Up, Down, Right, Left

                                    for dx, dy in directions:
                                        nx, ny = xx + dx, yy + dy
    
                                        if 0 <= nx < len(tasks) and 0 <= ny < len(tasks[0]) and tasks[nx][ny] == 2:
                                            
                                            r=random.randint(1,2)
                                            if x[nx][ny] == 'tree':
                                                if r==1:
                                                    tasks[nx][ny] = 0
                                                    x[nx][ny] = 'grass'
                                                
                                                    items[nx][ny]=1
            
                                            break 
                                     self.task='idle'
                                     self.set_goal(None)
        
        
                                '''
        
        

