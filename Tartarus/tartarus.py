#!/usr/bin/env python3
X=800
Y=100
import cProfile
import pstats
import io
import gc
import os
import subprocess
import curses
import time
import numpy as np
import worldgen
import random
import biomes
import math
import creatures
import pathfinding
result = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
maindir=result.stdout
maindir = maindir[:-1]
import multiprocessing
gc.enable()
'''
	"	=
░		
░	]	░


;		░
░	[	░
        o	
'''
'''
scene=0 is start
1 is main menu
2 is world creation
'''
task1c=0
task2c=0
relover=0
relovery=0
def region_generating(stdscr):
    #deprecated. here for remaining mentions.
    stdscr.refresh()
def add_item(row, col, item,items):
    items[row, col].append(item)
    
def remove_item(row, col, item,items):
    if item in items[row, col]:
        items[row, col].remove(item)
        
def get_items(row, col,items):
    return items[row, col]

def get_top_item(row, col,items):
    if items[row, col]:
        return items[row, col][-1]
    else:
        return None
#wtasks
def add_wtask(row, col, wtask,wtasks):
    wtasks[row, col].append(wtask)
    
def remove_wtask(row, col, wtask,wtasks):
    if wtask in wtasks[row, col]:
        wtasks[row, col].remove(wtask)
        
def get_wtasks(row, col,wtasks):
    return wtasks[row, col]

def get_top_wtask(row, col,wtasks):
    if wtasks[row, col]:
        return wtasks[row, col][-1]
    else:
        return None
##
def get_stockpile(x,y,stockpil):
    return stockpil[x][y]
class FPSCounter:
    def __init__(self):
        self.start_time = time.time()
        self.frame_count = 0

    def update(self):
        self.frame_count += 1
        if self.frame_count >= 10:  # Update FPS every 10 frames
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            fps = self.frame_count / elapsed_time
            return f"FPS: {fps:.2f}"
            self.start_time = end_time
            self.frame_count = 0
furniture= [ 'slate_pebble_table','basalt_pebble_table','talc_pebble_table','talc_pebble_chair','basalt_pebble_chair','slate_pebble_table','wood_table','wood_chair'
    ]
solids = [
                'tree', 'slate', 'iron-ore', 'copper-ore', 'silver-ore', 'gold-ore', 'mudstone', 'ozone','magnesite-ore','mythril-ore','tin-ore',
                'undiscovered_moss1','fungi-tree','water','undiscovered_rock_bush1','undiscovered_dense_moss1','fracter-ore','wood-wall','river','talc','basalt','great_sea'
        ]
building_items=['basalt_pebble','talc_pebble','slate_pebble','wood']

item_list = [ 'basalt_pebble','talc_pebble','slate_pebble','wood'
              
        ]
'''
for i in furniture:
    item_list.append(furniture[i])
'''
rock_types = [ 'basalt_pebble','talc_pebble','slate_pebble'
    ]
item_color = [ 22 , 23 , 10 , 8
    ]
undiscovered_tiletypes = ['undiscovered_moss1','undiscovered_rock_bush1','undiscovered_dense_moss1'

                          ]


workshops=[ 'carpenter0','carpenter1','carpenter2','carpenter3','carpenter4','carpenter5','carpenter6','carpenter7','carpenter8',
                'mason0','mason1','mason2','mason3','mason4','mason5','mason6','mason7','mason8'

    ]

carpenter_tiles=['carpenter0','carpenter1','carpenter2','carpenter3','carpenter4','carpenter5','carpenter6','carpenter7','carpenter8']
mason_tiles=['mason0','mason1','mason2','mason3','mason4','mason5','mason6','mason7','mason8']


startt=time.time()




tile_types = [
                'grass', 'sapling', 'mud', 'peat', 
                'nettle', 'crabgrass', 'densegrass', 'snow','aerath',
                'dead_shrub','cave_moss','rock_bush','dense_moss','sparse_grass','cavern_floor','slate_bridge',
                'carpenter0','carpenter1','carpenter2','carpenter3','carpenter4','carpenter5','carpenter6','carpenter7','carpenter8',
                'mason0','mason1','mason2','mason3','mason4','mason5','mason6','mason7','mason8','snow_covered_grass','snow_covered_nettle','snow_covered_sapling','snow_covered_densegrass',
                'snow_covered_crabgrass','snow_covered_sparse_grass','frozen_river','frozen_pool'
        ]
scene=0
def inputter(row=0,col=0,msg='hi'):
        curses.noecho()
        stdscr.addstr(row,col,msg)
        user_input=''
        while True:
            
            # Get user input
            key = stdscr.getch()

            # Check if the user wants to quit
            if key == 10:
                break

            # Display the input
            try:
                # Convert the input key to a character and add it to the string
                char = chr(key)
                user_input += char

                # Display the input character
                stdscr.addstr(char)
            except:
                # Handle non-ASCII characters gracefully
                pass
        return user_input

        #potentially a pain in the rear
        curses.echo()

def keypress(key):
    global scene
    if scene == 1:
        if key == ord('1'):
            scene=2
        
def start():
    global scene
    scene=1
    stdscr.addstr("1: New World\n",curses.A_BOLD)
    stdscr.addstr("2: Existing World\n")
    stdscr.addstr("3: Info\n")
    stdscr.addstr(10,0,"Created by Ralphy Reece")
    
    
def scene2():
    global key
    os.system('clear')
    global scene
    stdscr.addstr(10,0,"World Size:\n")

    stdscr.addstr(12,0,"1: Micro\n")
    stdscr.addstr(13,0,"2: Mini\n")
    stdscr.addstr(14,0,"3: Medium\n")
    key='9'
    
    
    
    
    scene=3
def gen_micro():
    
    world=worldgen.perlin_array(shape = (200, 200),
			scale=100, octaves = 6, 
			persistence = .5, 
			lacunarity = 2.0, 
			seed = None)
    for i in range(20):
        for j in range(20):
            print(world[i][j])
def scene_micro():
    global key
    os.system('clear')
    global scene
    stdscr.addstr(10,0,"World Generation Time:\n")

    
    key='9'

def create_popup(stdscr, message):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    popup_height = 5
    popup_width = len(message) + 4
    popup_y = (height // 2) - (popup_height // 2)
    popup_x = (width // 2) - (popup_width // 2)

    popup_win = curses.newwin(popup_height, popup_width, popup_y, popup_x)
    popup_win.border(0)
    popup_win.addstr(2, 2, message)
    stdscr.refresh()
    popup_win.refresh()
    time.sleep(2)
    popup_win.getch()


stdscr = curses.initscr()
stdscr.keypad(True)
curses.curs_set(0)  # Hide the cursor
curses.start_color()
stdscr.nodelay(1)  # Make getch non-blocking
###Another Overclocking Option
stdscr.timeout(10)
###
##Colors
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

#tree brown
brown_approximation = 600 # Value between 0-1000 for approximating brown
curses.init_color(8, brown_approximation, brown_approximation // 2, 0)  # RGB values for brown
curses.init_pair(8, 8, curses.COLOR_BLACK)

#dark brown
brown_approximation = 160 # Value between 0-1000 for approximating brown
curses.init_color(9, brown_approximation, brown_approximation // 2, 0)  # RGB values for brown
curses.init_pair(9, 9, curses.COLOR_BLACK)

#gray
brown_approximation = 160 # Value between 0-1000 for approximating brown
curses.init_color(10, 500, 500, 500)  # RGB values for brown
curses.init_pair(10, 10, curses.COLOR_BLACK)

#dark green
curses.init_color(11, 0, 250, 0)  # RGB values for brown
curses.init_pair(11, 11, curses.COLOR_BLACK)

#mud
curses.init_color(12, 800, 600, 0)  # RGB values for brown
curses.init_pair(12, 12, curses.COLOR_BLACK)

#peat
brown_approximation = 800 
curses.init_color(13, brown_approximation, brown_approximation // 2, 0)  
curses.init_pair(13, 13, curses.COLOR_BLACK)

#nettle
curses.init_color(14, 0, 220, 0)  
curses.init_pair(14, 14, curses.COLOR_BLACK)

#marsh soil
curses.init_color(15, 0, 200, 0) 
curses.init_pair(15, 15, curses.COLOR_BLACK)

#crabgrass
curses.init_color(16, 0, 120, 0)  
curses.init_pair(16, 16, curses.COLOR_BLACK)

#dense grass
curses.init_color(17, 0, 800, 0)  
curses.init_pair(17, 17, curses.COLOR_BLACK)

#snow
curses.init_color(18, 900, 900, 1000)  
curses.init_pair(18, 18, curses.COLOR_BLACK)

#fungi tree

curses.init_color(19, 0, 400, 200)  
curses.init_pair(19, 19, curses.COLOR_BLACK)

#dark cyan

curses.init_color(20, 0, 170, 200)  
curses.init_pair(20, 20, curses.COLOR_BLACK)

#sparse grass
curses.init_color(21, 0, 340, 0)  
curses.init_pair(21, 21, curses.COLOR_BLACK)

#dark gray
curses.init_color(22, 300, 300, 300)  
curses.init_pair(22, 22, curses.COLOR_BLACK)

#talc
curses.init_color(23, 950, 950, 900)  
curses.init_pair(23, 23, curses.COLOR_BLACK)

#frosty ice blue
curses.init_color(24, 750, 900, 1000) 
curses.init_pair(24, 24, curses.COLOR_BLACK)

#sea
curses.init_color(25, 50, 300, 600)  # RGB values range from 0-1000
curses.init_pair(25, 25, curses.COLOR_BLACK)

talc_color = (950, 950, 900)
fps_counter = FPSCounter()

def main_menu_print(stdscr):
    stdscr.addstr(5,62,"a - announcement window")
    stdscr.addstr(6,62,"d - designation menu")
    stdscr.addstr(7,62,"Space - pause (or leave menu)")
    stdscr.addstr(8,62,"k - toggle cursor")
    stdscr.addstr(9,62,"b - build menu")
    stdscr.addstr(10,62,"q - query")
    stdscr.addstr(11,62,"p - stockpiles")
def designation_menu_print(stdscr):
    stdscr.addstr(5,62,"d - mine")
    stdscr.addstr(6,62,"t - chop trees")
    stdscr.addstr(7,62,"x - undo designation")
    stdscr.addstr(8,62,"Space - leave menu")
def building_menu_print(stdscr):
    stdscr.addstr(5,62,"w - workshop")
    stdscr.addstr(8,62,"Space - leave menu")
def workshop_menu_print(stdscr):
    stdscr.addstr(5,62,"c - carpenter workshop")
    stdscr.addstr(6,62,"m - mason workshop")
    
    stdscr.addstr(8,62,"Space - leave menu")
    
def query_menu_print(stdscr):
    stdscr.addstr(5,62,"a - add new task")
    stdscr.addstr(6,62,"r - remove task")
    
    stdscr.addstr(8,62,"Space - leave menu")
def carpenter_crafting_menu_print(stdscr):
    stdscr.addstr(5,62,"t - table")
    stdscr.addstr(6,62,"c - chair")
    #stdscr.addstr(6,62,"b - wood_blocks")
    
    
    stdscr.addstr(8,62,"Space - leave menu")
def mason_crafting_menu_print(stdscr):
    stdscr.addstr(5,62,"t - table")
    stdscr.addstr(6,62,"c - chair")
    
    
    stdscr.addstr(8,62,"Space - leave menu")
def write_announcement(string):
    f=open(str(maindir)+'/fort/announcements.data','a')
    f.write(string)
    f.close()
def stockpile_menu_print(stdscr):
    stdscr.addstr(5,62,"1 - furniture stockpile")
    stdscr.addstr(6,62,"2 - common building items")
    stdscr.addstr(10,62,"x - remove stockpile tiles")
    
    
    stdscr.addstr(8,62,"Space - leave menu")
def announcement_window(stdscr):
    stdscr.clear()
    
    file = open(str(maindir)+'/fort/announcements.data','r') 
  
    
    content = file.readlines() 
  
    x=len(content)

    for i in range(x):
        try:
            stdscr.addstr(int(30-i),0,content[(x-1-i)])
        except:
            pass
    stdscr.refresh()
    while True:

        key = stdscr.getch()

        if key != -1:
        
            
            break
            

    
    
def draw_rect(stdscr, char, color_pair, y, x):
    

    key_height = 3
    key_width = 5


    box_y = y - 1
    box_x = x - 1


    # Draw box
    for i in range(key_height):
        for j in range(key_width):
            if i == 0 or i == key_height - 1 or j == 0 or j == key_width - 1:
                stdscr.addch(box_y + i, box_x + j, curses.ACS_BLOCK, curses.color_pair(1))
            else:
                stdscr.addch(box_y + i, box_x + j, ' ', curses.color_pair(2))

    # Print character in center of box
    char_y = y
    char_x = x
    stdscr.addch(char_y, char_x, char, curses.color_pair(color_pair))
  
def set_carpenter_crafting_task(dwarves, cursor_x, cursor_y, rock, item_type):
    for Q in dwarves:
        if 'carpenter' in Q.professions:
            if Q.get_goal() is None:
                Q.set_craft(cursor_x, cursor_y)
                Q.get_item = rock
                Q.make_item = item_type  
     
def set_mason_crafting_task(dwarves, cursor_x, cursor_y, rock, item_type):
    for Q in dwarves:
        if 'mason' in Q.professions:
            if Q.get_goal() is None:
                Q.set_craft(cursor_x, cursor_y)
                Q.get_item = rock
                Q.make_item = item_type  
# Main loop
while True:
    key='sdsdsd'
    
    
    # Get the next character typed (or -1 if no input)
    key = stdscr.getch()
    keypress(key)
    
    
    if key != -1:
        
        #stdscr.addstr(f"Key pressed: {key}\n")
        
        
        if key == ord('`'):
            break



    if scene==0:
        start()
    if scene==1:
        if key == ord('1'):
            scene=2
    if scene==2:
        scene2()
    if scene==3:
        if key == ord('1'):
            scene='gen_micro'
        if key == ord('2'):
            scene='gen_mini'
        if key == ord('3'):
            scene='gen_medium'
    if scene=='gen_micro':
        scene='micro'
    if scene=='micro':
        scene_micro()
        x=inputter(row=11,col=0,msg='Years: (press Enter to exit, double is ok)')
        scene='micro2'      
    if scene=='micro2':
        os.system('clear')
        stdscr.addstr(15,0,"Generating World, grab a sandwich")
        stdscr.refresh()
        
        worldgen.perlin_array(years=int(x), shape = (20, 60),
			scale=100, octaves = 6, 
			persistence = .5, 
			lacunarity = 2.0, 
			seed = random.randint(0,100))
        scene='start_game'
        key='q'
        os.system('clear')
        embarkx =0
        embarky =0
    if scene=='start_game':
        
        f=open(str(maindir)+'/world/world_size.data','r')
        size=f.read()
        
        f.close()
        os.system('clear')
        filename = str(maindir)+'/world/graphic.data'  
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                try:
                    stdscr.refresh()
                    time.sleep(.05)
                    stdscr.addstr(i, 0, line)
                except:
                    pass
        scene='choose_emb'
        
    if scene=='choose_emb':
            number_after_x = size.split('x')[1]
        
            
        
            stdscr.addstr(0,int(number_after_x)+5,"Where to embark?(world size:) "+str(size))
            stdscr.addstr(3,int(number_after_x)+5,".,:; are water tiles")
            stdscr.addstr(4,int(number_after_x)+5,"+ * % # @ are land, altitude highest at @")
            #
            

            
        
            stdscr.addstr(embarky,embarkx,"X",curses.color_pair(1))
            elev=np.loadtxt(str(maindir)+'/world/world_elev.data')
            stdscr.addstr(25,0,"Elevation: "+str(elev[embarky][embarkx]))
            temp=np.loadtxt(str(maindir)+'/world/world_temp.data')

            rain=np.loadtxt(str(maindir)+'/world/world_rain.data')

            stdscr.addstr(29,0,"Rain: "+str(rain[embarky][embarkx]))

            
            stdscr.addstr(28,0,"Temp: "+str(temp[embarky][embarkx]))
            stdscr.refresh()
            if elev[embarky][embarkx] < 40:
                stdscr.addstr(26,0,"Sea, Can not embark",curses.color_pair(3))
            else:
                stdscr.addstr(26,0,"                       ",curses.color_pair(1))
                
            
            #
            biome='                      '
            t=temp[embarky][embarkx]
            temperature=t
            a=elev[embarky][embarkx]
            r=rain[embarky][embarkx]
            if t > biomes.desert[0] and t < biomes.desert[1]:
                if a > biomes.desert[2] and a < biomes.desert[3]:
                    if r > biomes.desert[4] and r < biomes.desert[5]:
                        biome='desert'
            if t > biomes.glacier[0] and t < biomes.glacier[1]:
                if a > biomes.glacier[2] and a < biomes.glacier[3]:
                    if r > biomes.glacier[4] and r < biomes.glacier[5]:
                        biome = 'glacier'
            if t > biomes.savannah[0] and t < biomes.savannah[1]:
                if a > biomes.savannah[2] and a < biomes.savannah[3]:
                    if r > biomes.savannah[4] and r < biomes.savannah[5]:
                        biome = 'savannah'
            if t > biomes.alpine[0] and t < biomes.alpine[1]:
                if a > biomes.alpine[2] and a < biomes.alpine[3]:
                    if r > biomes.alpine[4] and r < biomes.alpine[5]:
                        biome = 'alpine'
            if t > biomes.forest[0] and t < biomes.forest[1]:
                if a > biomes.forest[2] and a < biomes.forest[3]:
                    if r > biomes.forest[4] and r < biomes.forest[5]:
                        biome = 'forest'
            if t > biomes.plain[0] and t < biomes.plain[1]:
                if a > biomes.plain[2] and a < biomes.plain[3]:
                    if r > biomes.plain[4] and r < biomes.plain[5]:
                        biome = 'plain'
            if t > biomes.marsh[0] and t < biomes.marsh[1]:
                if a > biomes.marsh[2] and a < biomes.marsh[3]:
                    if r > biomes.marsh[4] and r < biomes.marsh[5]:
                        biome = 'marsh'
            if t > biomes.rainforest[0] and t < biomes.rainforest[1]:
                if a > biomes.rainforest[2] and a < biomes.rainforest[3]:
                    if r > biomes.rainforest[4] and r < biomes.rainforest[5]:
                        biome = 'rainforest'
            if t > biomes.slop[0] and t < biomes.slop[1]:
                if a > biomes.slop[2] and a < biomes.slop[3]:
                    if r > biomes.slop[4] and r < biomes.slop[5]:
                        biome = 'slop'
            if t > biomes.shallows[0] and t < biomes.shallows[1]:
                if a > biomes.shallows[2] and a < biomes.shallows[3]:
                    if r > biomes.shallows[4] and r < biomes.shallows[5]:
                        biome = 'shallows'
            if t > biomes.sea[0] and t < biomes.sea[1]:
                if a > biomes.sea[2] and a < biomes.sea[3]:
                    if r > biomes.sea[4] and r < biomes.sea[5]:
                        biome = 'sea'
            if t > biomes.depths[0] and t < biomes.depths[1]:
                if a > biomes.depths[2] and a < biomes.depths[3]:
                    if r > biomes.depths[4] and r < biomes.depths[5]:
                        biome = 'depths'

            stdscr.addstr(30,0,"                 ",curses.color_pair(2))
            stdscr.addstr(30,0,biome,curses.color_pair(2))

            
                
            
            
            
            

            if key == curses.KEY_UP:
              
            

                if embarky > 0:
                    embarky-=1
                    
            if key == curses.KEY_DOWN:
                
           
                
                if embarky < 19:
                    embarky+=1
                    

            
            if key == curses.KEY_LEFT:
            
                if embarkx > 0:
                    embarkx-=1
                    
            
            if key == curses.KEY_RIGHT:
                
                stdscr.refresh()
                if embarkx < 59:
                    embarkx +=1
            if key == 10:
                if elev[embarky][embarkx] > 40:
                    x=inputter(8,int(number_after_x)+5,"Do you want to embark? (y/n):")
                    if x == 'y':
                        scene='micro_region'
                        
                        os.system('clear')
    if scene == 'micro_region':
        os.system('clear')
        region_generating(stdscr)
        
        worldgen.micro_region(biome,elev[embarky,embarkx],stdscr)
        x=np.loadtxt(str(maindir)+'/region/region.data',dtype=object)
        
                
        np.savetxt(str(maindir)+'/fort/fort.data',x,fmt='%s')
                
        scene='preplay'
                    
                    
                
                    
                
                    
                   
            
            
        stdscr.refresh()
            
            
        
        




        
        

        #
        t=0
        t2=0
        cursorx,cursory=30,15
        x=np.loadtxt(str(maindir)+'/fort/fort.data',dtype=object)
        dc1=[0,0]
        dc2=[0,0]
    if scene == 'preplay':
        items=np.empty((X,Y),dtype=object)
        for i in range(X):
            for j in range(Y):
                items[i, j] = []
        wtasks=np.empty((X,Y),dtype=object)
        stockpile=np.zeros((X,Y))
        for i in range(X):
            for j in range(Y):
                wtasks[i, j] = []
        tasks=np.zeros((X,Y))
        workshop_color=np.zeros((X,Y))
        
        menu='main'
        t=0
        t2=0
        cursorx,cursory=1,1
        x=np.loadtxt(str(maindir)+'/fort/fort.data',dtype=object)
        #text animal
        entities=[]
        dwarves=[]
        playing = 1
        
        rat= creatures.Creature('Y', 7, 15, 30, 'yak', 1, 1, 1, 10, 1,400,0,3,0,0)
        entities.append(rat)
        
        for i in range(10):
                rat= creatures.Creature('Y', 7, 15, 95, 'yak', 1, 1, 1, 10, 1,10000,0,1,0,0)
                #rat= creatures.Creature('r', 7, 30, 150, 'rat', 1, 1, 1, 2, 3,30000,1,5,0,0)
                entities.append(rat)
        
        #rat= creatures.Creature('d', 7, 15, 35, 'dog', 10, 1, 1, 2, 3,10000,0,50,0,1)
        #entities.append(rat)
        #rat= creatures.Creature('d', 7, 15, 42, 'dog', 10, 1, 1, 2, 3,10000,0,50,0,1)
        
        #entities.append(rat)
        #Dwarves

        
        dorf=creatures.Dwarf(1, 14, 90, 'Gimli', 5, 5, ['pickaxe'],['miner'])
        dwarves.append(dorf)
        
        
        dorf=creatures.Dwarf(3, 15, 91, 'Nil', 5, 5, ['axe'],['woodcutter'])
        #self, color, posx, posy, name, strength, agility, possessions, professions
        dwarves.append(dorf)

        dorf=creatures.Dwarf(1, 14, 90, 'Gimlii', 5, 5, ['pickaxe'],['miner'])
        dwarves.append(dorf)

        dorf=creatures.Dwarf(1, 14, 90, 'Gimlii', 5, 5, [],['carpenter','architecture'])
        dwarves.append(dorf)

        dorf=creatures.Dwarf(2, 14, 93, 'Dinglii', 5, 5, [],['mason'])
        dwarves.append(dorf)
        
        for i in range(5):
            add_item(i+90,20,'wood',items)
        scene='play'
        over=5
        overy=0
        tim=time.time()
        kshown=0
        dclicks=0

        ##Testing Area
        '''
        for i in range(X):
            for j in range(Y):
                if x[i][j] == 'slate':
                    x[i][j]='cavern_floor'
        
        
        
        '''
        
        ##
        dc=0
        dc1=[None,None]
        dc2=[None,None]

        
        discover1=False
    if scene == 'play':
        
        #snow/other
        #add temp later
        try:
            if season=='winter':
                if t % 6001 == 0:
                    for j in range(Y):
                        for i in range(X):
                            if x[i][j] == 'grass':
                                x[i][j] = 'snow_covered_grass'
                            if x[i][j] == 'nettle':
                                x[i][j] = 'snow_covered_nettle'
                            if x[i][j] == 'densegrass':
                                x[i][j] = 'snow_covered_densegrass'
                            if x[i][j] == 'sparse_grass':
                                x[i][j] = 'snow_covered_sparse_grass'
                            if x[i][j] == 'sapling':
                                x[i][j] = 'snow_covered_sapling'
                            if x[i][j] == 'crabgrass':
                                x[i][j] = 'snow_covered_crabgrass'
                            if x[i][j] == 'river':
                                x[i][j] = 'frozen_river'
                    
                            if x[i][j] == 'water':
                                x[i][j] = 'frozen_pool'
        except:
            pass
                        
                    
            
            
        
        if t % 8000 < 2000:
            season='spring'
        elif t % 8000 < 4000:
            season='summer'
        elif t % 8000 < 6000:
            season='fall'
        elif t % 8000 < 8000:
            season='winter'
        if t == 0:
            x_2=np.zeros((X,Y))
            for j in range(X):
                for i in range(Y):
                    if x[j][i] in solids:
                        x_2[j][i] = 1
                    
            np.savetxt(str(maindir)+'/region/pathfind.data',x_2)
            
        if t % 10 == 0:
            for j in range(Y):
                
                
            
                for i in range(X):
                    if x[i][j] in undiscovered_tiletypes:
                        try:
                            
                                
                             if x[i-1][j] in tile_types or \
                                x[i+1][j] in tile_types or \
                                x[i][j-1] in tile_types or \
                                x[i][j+1] in tile_types:
                                discover1=True
                        except:
                            pass
                        

        #discover cave
        if discover1 == True:
            create_popup(stdscr,'You have discovered a cavern deep inside the mountain')
            write_announcement('You have discovered a cavern deep inside the mountain \n')
            discover1 = False
            for j in range(Y):
                for i in range(X):
                    if x[i][j] == 'undiscovered_moss1':
                        x[i][j] = 'cave_moss'
                    if x[i][j] == 'undiscovered_rock_bush1':
                        x[i][j] = 'rock_bush'
                    if x[i][j] == 'undiscovered_dense_moss1':
                        x[i][j] = 'dense_moss'
                    
                        

            
        
        

        if t == 2:
            over=0
            playing=0

        if t == 800:
                beg1=time.time()
        
        if t % 2 == 0:
                stdscr.clear()

        if playing % 2 ==0:
            stdscr.addstr(0,18,"PAUSED",curses.color_pair(6))
        
        
        t+=1
        offset=62
        if key == curses.KEY_F1:
                for i in entities:
                        i.goto(i.posx+overy,i.posy+over)
                for i in dwarves:
                        i.goto(i.posx+overy,i.posy+over)
                over=0
                overy=0
        if menu == 'main':
            if key == ord('a'):
                announcement_window(stdscr)
        
        if key == ord(' '):
            if menu =='main':
                playing+=1
            elif menu != 'main':
                menu='main'
                kshown=0
        
            
            
        if key == ord('k'):
            if menu == 'main':
                kshown += 1
                menu = 'k'
            elif menu == 'k':
                kshown += 1
                menu = 'main'

                
            
        '''
        if key == ord('>'):
            stdscr.clear()
            over+=10
            for i in entities:
                i.goto(i.posx,i.posy-10)
            
        if key == ord('<'):
            stdscr.clear()
            if over >= 10:
                over-=10
                for i in entities:
                    i.goto(i.posx,i.posy+10)
        '''
        if key == 27:
            menu='main'
            kshown=0
            dclicks=0
        
        
         
        
        
        for j in range(30):
                try:
                    stdscr.addstr(j+1,60,'|')
                except:
                    pass
                
                
            
                for i in range(60):
                        try:
                            




                            
                            
                            if x[i+over][j+overy] == 'grass':
                                stdscr.addstr(j+1,i,'`',curses.color_pair(2))
                            
                            if x[i+over][j+overy] == 'dead shrub':
                                stdscr.addstr(j+1,i,'&',curses.color_pair(9))
                    
                            if x[i+over][j+overy] == 'sapling':
                                stdscr.addstr(j+1,i,'γ',curses.color_pair(11))

                            if x[i+over][j+overy] == 'mud':
                                stdscr.addstr(j+1,i,';',curses.color_pair(12))
                            if x[i+over][j+overy] == 'snow':
                                stdscr.addstr(j+1,i,'"',curses.color_pair(7))

                            if x[i+over][j+overy] == 'dirt':
                                stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                            
                            if x[i+over][j+overy]== 'wood-wall':
                                stdscr.addstr(j+1,i,'#',curses.color_pair(8))
                            if x[i+over][j+overy]== 'peat':
                                stdscr.addstr(j+1,i,'&',curses.color_pair(15))
                            if x[i+over][j+overy] == 'nettle':
                                stdscr.addstr(j+1,i,'\'',curses.color_pair(14))
                            if x[i+over][j+overy] == 'crabgrass':
                                stdscr.addstr(j+1,i,'√',curses.color_pair(16))
                            if x[i+over][j+overy] == 'densegrass':
                                stdscr.addstr(j+1,i,'\"',curses.color_pair(17))
                            if x[i+over][j+overy] == 'snow':
                                stdscr.addstr(j+1,i,'~',curses.color_pair(18))
                            if x[i+over][j+overy] == 'aerath':
                                stdscr.addstr(j+1,i,'º',curses.color_pair(5))
                            if x[i+over][j+overy] == 'cave_moss':
                                stdscr.addstr(j+1,i,',',curses.color_pair(6))
                            if x[i+over][j+overy] == 'rock_bush':
                                stdscr.addstr(j+1,i,'ı',curses.color_pair(10))
                            if x[i+over][j+overy] == 'dense_moss':
                                stdscr.addstr(j+1,i,'‰',curses.color_pair(20))
                            if x[i+over][j+overy] == 'sparse_grass':
                                stdscr.addstr(j+1,i,'.',curses.color_pair(21))
                            if x[i+over][j+overy] == 'cavern_floor':
                                stdscr.addstr(j+1,i,'¬',curses.color_pair(22))
                            if x[i+over][j+overy] == 'slate_bridge':
                                stdscr.addstr(j+1,i,'═',curses.color_pair(22))
                            if x[i+over][j+overy] == 'snow_covered_grass':
                                stdscr.addstr(j+1,i,'~',curses.color_pair(18))
                            if x[i+over][j+overy] == 'snow_covered_nettle':
                                stdscr.addstr(j+1,i,'\'',curses.color_pair(18))
                            if x[i+over][j+overy] == 'snow_covered_crabgrass':
                                stdscr.addstr(j+1,i,'~',curses.color_pair(23))
                            if x[i+over][j+overy] == 'snow_covered_densegrass':
                                stdscr.addstr(j+1,i,'-',curses.color_pair(18))
                            if x[i+over][j+overy] == 'snow_covered_sapling':
                                stdscr.addstr(j+1,i,'/',curses.color_pair(23))
                            if x[i+over][j+overy] == 'snow_covered_sparse_grass':
                                stdscr.addstr(j+1,i,'≈',curses.color_pair(23))
                            if x[i+over][j+overy] == 'frozen_river':
                                stdscr.addstr(j+1,i,'#',curses.color_pair(24))
                            if x[i+over][j+overy] == 'frozen_pool':
                                stdscr.addstr(j+1,i,'#',curses.color_pair(24))
                            if stockpile[i+over,j+overy]!=0:
                                stdscr.addstr(j+1,i,'=',curses.color_pair(23))


                            #items
                            if get_top_item(i+over,j+overy,items) == 'wood':
                                stdscr.addstr(j+1,i,'≠',curses.color_pair(8))
                            if get_top_item(i+over,j+overy,items) == 'slate_pebble':
                                stdscr.addstr(j+1,i,'•',curses.color_pair(10))
                            if get_top_item(i+over,j+overy,items) == 'basalt_pebble':
                                stdscr.addstr(j+1,i,'•',curses.color_pair(22))
                            if get_top_item(i+over,j+overy,items) == 'talc_pebble':
                                stdscr.addstr(j+1,i,'•',curses.color_pair(23))
                            if get_top_item(i+over,j+overy,items) == 'wood_table':
                                stdscr.addstr(j+1,i,'╦',curses.color_pair(8))
                                
                            


                            #workshop
                            if x[i+over][j+overy] == 'carpenter0':
                                stdscr.addstr(j+1,i,' ',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'carpenter1':
                                stdscr.addstr(j+1,i,'░',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'carpenter2':
                                stdscr.addstr(j+1,i,'░',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'carpenter3':
                                stdscr.addstr(j+1,i,'\"',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'carpenter4':
                                stdscr.addstr(j+1,i,' ',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'carpenter5':
                                stdscr.addstr(j+1,i,']',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'carpenter6':
                                stdscr.addstr(j+1,i,'═',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'carpenter7':
                                stdscr.addstr(j+1,i,' ',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'carpenter8':
                                stdscr.addstr(j+1,i,'░',curses.color_pair(int(workshop_color[i+over][j+overy])))

                            if x[i+over][j+overy] == 'mason0':
                                stdscr.addstr(j+1,i,';',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'mason1':
                                stdscr.addstr(j+1,i,'░',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'mason2':
                                stdscr.addstr(j+1,i,' ',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'mason3':
                                stdscr.addstr(j+1,i,' ',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'mason4':
                                stdscr.addstr(j+1,i,'[',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'mason5':
                                stdscr.addstr(j+1,i,'o',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'mason6':
                                stdscr.addstr(j+1,i,'░',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'mason7':
                                stdscr.addstr(j+1,i,'░',curses.color_pair(int(workshop_color[i+over][j+overy])))
                            if x[i+over][j+overy] == 'mason8':
                                stdscr.addstr(j+1,i,' ',curses.color_pair(int(workshop_color[i+over][j+overy])))

                        except:
                            break
                        
                        
                        
                
                        try:
                    
                            if x[i+over][j+overy] in solids:
                            
                                symbol = '\u2588'

                                color = curses.color_pair(10)
                                if x[i+over][j+overy] == 'iron-ore':
                                    symbol = '%'
                                    color = curses.color_pair(1)
                                elif x[i+over][j+overy] == 'copper-ore':
                                    symbol = '%'
                                    color = curses.color_pair(9)
                                elif x[i+over][j+overy] == 'silver-ore':
                                    symbol = '%'
                                    color = curses.color_pair(10)
                                elif x[i+over][j+overy] == 'gold-ore':
                                    symbol = '%'
                                    color = curses.color_pair(4)
                                elif x[i+over][j+overy] == 'mudstone':
                                    symbol = '#'
                                    color = curses.color_pair(9)
                                elif x[i+over][j+overy] == 'ozone':
                                    symbol = '‰'
                                    color = curses.color_pair(6)
                                elif x[i+over][j+overy] == 'magnesite-ore':
                                    symbol = '%'
                                    color = curses.color_pair(1)
                                elif x[i+over][j+overy] == 'tin-ore':
                                    symbol = '%'
                                    color = curses.color_pair(13)
                                elif x[i+over][j+overy] == 'tree':
                                    symbol = 'O'
                                    color = curses.color_pair(8)
                                elif x[i+over][j+overy] == 'fungi-tree':
                                    symbol = 'Ø'
                                    color = curses.color_pair(19)
                                elif x[i+over][j+overy] == 'fracter-ore':
                                    symbol = '%'
                                    color = curses.color_pair(5)
                                elif x[i+over][j+overy] == 'talc':
                                    symbol = '\u2588'
                                    color = curses.color_pair(23)
                                elif x[i+over][j+overy] == 'basalt':
                                    symbol = '\u2588'
                                    color = curses.color_pair(22)
        
                                if x[i-1+over][j+overy] in tile_types or \
                                   x[i+1+over][j+overy] in tile_types or \
                                   x[i+over][j-1+overy] in tile_types or \
                                   x[i+over][j+1+overy] in tile_types:
                                    
                                    stdscr.addstr(j+1, i, symbol, color)
                        except:
                            break

                        #solid but seeable
                        try:
                            if x[i+over][j+overy] == 'water':
                                    stdscr.addstr(j+1,i,'≈',curses.color_pair(3))
                            if x[i+over][j+overy] == 'river':
                                r=random.randint(1,10)
                                if r <= 5:
                                    stdscr.addstr(j+1,i,'≈',curses.color_pair(3))
                                elif r <= 8:
                                    stdscr.addstr(j+1,i,'~',curses.color_pair(3))
                                else:
                                    stdscr.addstr(j+1,i,'≈')
                            if x[i+over][j+overy] == 'great_sea':
                                r=random.randint(1,10000)
                                if r <= 9999:
                                    stdscr.addstr(j+1,i,'≈',curses.color_pair(25))
                                else:
                                    stdscr.addstr(j+1,i,'~',curses.color_pair(3))
                                
                        except:
                            pass
                        if t % 20 <= 10:
                            if tasks[i+over,j+overy]!=0:
                                stdscr.addstr(j+1,i,'\u2588',curses.color_pair(4))
                        
                        
        

        if t == 800:
                beg2=time.time()
        
        if menu != 'designation':
            relover,relovery=0,0
        if t % 1000 == 0:       
                np.savetxt(str(maindir)+'/fort/fort.data',x,fmt='%s')
        if cursorx >=55 and over < X-10:
            relover+=10
            cursorx -=10
            over+=10
            for i in entities:
                    i.goto(i.posx,i.posy-10)
            for i in dwarves:
                        i.goto(i.posx,i.posy-10)
                        i.overyc-=10
        if cursorx <=5 and over > 10:
            cursorx +=10
            
            over-=10
            for i in entities:
                i.goto(i.posx,i.posy+10)
            for i in dwarves:
                i.goto(i.posx,i.posy+10)
                i.overyc+=10
            
        if kshown % 2 == 1:
            stdscr.addstr(cursory,cursorx,"X")

        #t test
        stdscr.addstr(30,62,'       ')
        stdscr.addstr(30,62,str(t))

        if key == curses.KEY_UP:
            if menu !='main':
              
            

                if cursory > 1:
                    cursory-=1
            if menu == 'main':
                if overy >= 10:
                
                    overy-=10
                    for i in entities:
                        i.goto(i.posx+10,i.posy)
                    for i in dwarves:
                        i.goto(i.posx+10,i.posy)
                        i.overc+=10
                    
        if key == curses.KEY_DOWN:
            if menu !='main':
                
           
                
                if cursory < 59:
                    cursory+=1
            
            if menu == 'main':
                if overy <= Y-10:

                
                    overy+=10
                    for i in entities:
                        i.goto(i.posx-10,i.posy)
                    for i in dwarves:
                        i.goto(i.posx-10,i.posy)
                        i.overc-=10
                    

            
        if key == curses.KEY_LEFT:
            if menu !='main':
            
                if cursorx > 1:
                    cursorx-=1
            if menu =='main':
    
                if over >= 10:
                    over-=10
                    for i in entities:
                        i.goto(i.posx,i.posy+10)
                    for i in dwarves:
                        i.goto(i.posx,i.posy+10)
                        i.overyc+=10
                    
            
        if key == curses.KEY_RIGHT:
            if menu !='main':
                
                stdscr.refresh()
                if cursorx < 179:
                    cursorx +=1
            if menu == 'main':
                
                over+=10
                for i in entities:
                    i.goto(i.posx,i.posy-10)
                for i in dwarves:
                        i.goto(i.posx,i.posy-10)
                        i.overyc-=10
        
        if menu == 'main':
            if key == ord('p'):
                playing=0
                kshown+=1
                menu='stockpile'
                action='stockpile1'
            if key == ord('q'):
                playing=0
                kshown+=1
                menu='query'
            if key == ord('d'):
                playing=0
                menu='designation'
                action='dig'
                kshown+=1
            if key == ord('b'):
                playing=0
                menu='building'
                #kshown+=1
                action='carpenter'
        
        if menu == 'building':
            if key == ord('w'):
                menu = 'workshop'
        if menu == 'workshop':
            if key == ord('c'):
                menu = 'build_carpenter'
            if key == ord('m'):
                menu = 'build_mason'
        if menu == 'build_carpenter':
            can_build=1
            
            for i in range(3):
                for j in range(3):
                    if x[cursorx+over+j][cursory+overy-1+i] not in solids:
                        stdscr.addstr(cursory+i,cursorx+j,'X',curses.color_pair(5))
                    else:
                        can_build=0
                        stdscr.addstr(cursory+i,cursorx+j,'X',curses.color_pair(6))
            
            if can_build==1:
                stdscr.addstr(4,61,'Placement')
            else:
                stdscr.addstr(4,61,'Workshop Blocked')
            if key == 10 and can_build == 1:
                ccursorx=cursorx
                ccursory=cursory
                rocks=[]
                rx=[]
                ry=[]
                for j in range(X-1):
                    for i in range(Y-1):
                            temmm=get_items(j,i,items)
                            if 'slate_pebble' in temmm:
                                rx.append(j)
                                ry.append(i)
                                rocks.append('slate_pebble')
                            elif 'talc_pebble' in temmm:
                                rx.append(j)
                                ry.append(i)
                                rocks.append('talc_pebble')
                            elif 'basalt_pebble' in temmm:
                                rx.append(j)
                                ry.append(i)
                                rocks.append('basalt_pebble')
                            elif 'wood' in temmm:
                                rx.append(j)
                                ry.append(i)
                                rocks.append('wood')
                menu='carpenter_material'
                boldened=0
                key='something to not be 10'
                
        if menu == 'build_mason':
            can_build=1
            
            for i in range(3):
                for j in range(3):
                    if x[cursorx+over+j][cursory+overy-1+i] not in solids:
                        stdscr.addstr(cursory+i,cursorx+j,'X',curses.color_pair(5))
                    else:
                        can_build=0
                        stdscr.addstr(cursory+i,cursorx+j,'X',curses.color_pair(6))
            
            if can_build==1:
                stdscr.addstr(4,61,'Placement')
            else:
                stdscr.addstr(4,61,'Workshop Blocked')
            if key == 10 and can_build == 1:
                ccursorx=cursorx
                ccursory=cursory
                rocks=[]
                rx=[]
                ry=[]
                for j in range(X-1):
                    for i in range(Y-1):
                            temmm=get_items(j,i,items)
                            if 'slate_pebble' in temmm:
                                rx.append(j)
                                ry.append(i)
                                rocks.append('slate_pebble')
                            elif 'talc_pebble' in temmm:
                                rx.append(j)
                                ry.append(i)
                                rocks.append('talc_pebble')
                            elif 'basalt_pebble' in temmm:
                                rx.append(j)
                                ry.append(i)
                                rocks.append('basalt_pebble')
                            elif 'wood' in temmm:
                                rx.append(j)
                                ry.append(i)
                                rocks.append('wood')
                menu='mason_material'
                boldened=0
                key='something to not be 10'
                
              
        if menu == 'carpenter_material':
            for i in range(30):
                if boldened != i:
                    try:
                        stdscr.addstr(i,65,rocks[i])
                    except:
                        pass
                else:
                    try:
                        
                        stdscr.addstr(i, 65,rocks[i],curses.color_pair(6))
                        
                    except:
                        boldened=0
            if key == ord('='):
                if boldened > 0:
                    boldened-=1
            elif key == ord('-'):
                if boldened <30:
                    boldened+=1
            if key == 10:
                #this is kinda a scam, but whatever. Makes choosing a material mostly useless.
                for i in dwarves:
                    if 'carpenter' in i.professions:
                        if i.get_goal() == None:
                            i.get_item=rocks[boldened]
                            i.set_build(ccursorx+over,ccursory+overy-1)
                            

                menu='main'
                
                for i in range(3):
                    for j in range(3):
                        x[ccursorx+over+j][ccursory+overy-1+i]='unbuilt_carpenter_workshop'
                
        if menu == 'mason_material':
            for i in range(30):
                if boldened != i:
                    try:
                        stdscr.addstr(i,65,rocks[i])
                    except:
                        pass
                else:
                    try:
                        
                        stdscr.addstr(i, 65,rocks[i],curses.color_pair(6))
                        
                    except:
                        boldened=0
            if key == ord('='):
                if boldened > 0:
                    boldened-=1
            elif key == ord('-'):
                if boldened <30:
                    boldened+=1
            if key == 10:
                #this is kinda a scam, but whatever. Makes choosing a material mostly useless.
                for i in dwarves:
                    if 'mason' in i.professions:
                        if i.get_goal() == None:
                            i.get_item=rocks[boldened]
                            i.set_build(ccursorx+over,ccursory+overy-1)
                            

                menu='main'
                
                for i in range(3):
                    for j in range(3):
                        x[ccursorx+over+j][ccursory+overy-1+i]='unbuilt_mason_workshop'
                
            
                        
                    
        if menu == 'query':
            if key == ord('a'):
                if x[cursorx+over][cursory+overy-1] in carpenter_tiles:
                    menu = 'carpenter_crafting'
                if x[cursorx+over][cursory+overy-1] in mason_tiles:
                    menu = 'mason_crafting'
                key = 'qqqqqqqq'
                ccursorx=cursorx+over
                ccursory=cursory+overy-1
        if menu == 'carpenter_crafting':
            if key == ord('t'):
                menu = 'query'
                rock = None
                for j in range(X-1):
                    for i in range(Y-1):
                        temmm = get_items(j, i, items)
                        if 'wood' in temmm:
                            rock = 'wood'
                            item_type = 'wood_table'
                            set_carpenter_crafting_task(dwarves, ccursorx, ccursory, rock, item_type)
                            break
            if key == ord('c'):
                menu = 'query'
                rock = None
                for j in range(X-1):
                    for i in range(Y-1):
                        temmm = get_items(j, i, items)
                        if 'wood' in temmm:
                            rock = 'wood'
                            item_type = 'wood_chair'
                            set_carpenter_crafting_task(dwarves, ccursorx, ccursory, rock, item_type)
                            break
        if menu == 'mason_crafting':
            if key == ord('t'):
                menu = 'query'
                rock = None
                for j in range(X-1):
                    for i in range(Y-1):
                        temmm = get_items(j, i, items)
                        for k in rock_types:
                            if k in temmm:
                                rock = k
                                item_type = str(k)+'_table'
                                set_mason_crafting_task(dwarves, ccursorx, ccursory, rock, item_type)
                                break
            if key == ord('c'):
                menu = 'query'
                rock = None
                for j in range(X-1):
                    for i in range(Y-1):
                        temmm = get_items(j, i, items)
                        for k in rock_types:
                            if 'wood' in temmm:
                                rock = k
                                item_type = str(k)+'_chair'
                                set_mason_crafting_task(dwarves, ccursorx, ccursory, rock, item_type)
                                break
                                
                                
                                
                            
                
            
                    
        if menu == 'stockpile':
            

            if key == ord("1"):
                action='stockpile1'
            if key == ord("2"):
                action='stockpile2'
            if key == ord('x'):
                action='stockpile0'
            if key == 10:
                if dclicks==0:
                    dc1=[cursorx,cursory]
                    dclicks=1
                elif dclicks ==1:
                    dc2=[cursorx,cursory]
                    dclicks=0
                    if action=='stockpile1':
                        
                        try:
                            for i in range(dc2[0]-dc1[0]+1+relover):
                                for j in range(dc2[1]-dc1[1]+1):
                                    if x[dc1[0]+i+over,dc1[1]+j-1+overy] in tile_types:
                                        stockpile[dc1[0]+i+over-relover,dc1[1]+j-1+overy]=1
                        except TypeError:
                            pass
                        relover,relovery=0,0
                    if action=='stockpile2':
                        
                        try:
                            for i in range(dc2[0]-dc1[0]+1+relover):
                                for j in range(dc2[1]-dc1[1]+1):
                                    if x[dc1[0]+i+over,dc1[1]+j-1+overy] in tile_types:
                                        stockpile[dc1[0]+i+over-relover,dc1[1]+j-1+overy]=2
                        except TypeError:
                            pass
                        relover,relovery=0,0
                    #rm stockpile
                    if action=='stockpile0':
                        
                        try:
                            for i in range(dc2[0]-dc1[0]+1+relover):
                                for j in range(dc2[1]-dc1[1]+1):
                                    stockpile[dc1[0]+i+over-relover,dc1[1]+j-1+overy]=0
                        except TypeError:
                            pass
                        relover,relovery=0,0
            

           
        
        if menu =='designation':
            
            if key == ord('d'):
                action='dig'
            if key == ord('x'):
                action='rmdig'
            if key == ord('t'):
                action='tree'
                
        
            if key == 10:
                if dclicks==0:
                    dc1=[cursorx,cursory]
                    dclicks=1
                elif dclicks ==1:
                    dc2=[cursorx,cursory]
                    dclicks=0
                    if action=='dig':
                        
                        try:
                            for i in range(dc2[0]-dc1[0]+1+relover):
                                for j in range(dc2[1]-dc1[1]+1):
                                    if x[dc1[0]+i+over,dc1[1]+j-1+overy] in solids:
                                        tasks[dc1[0]+i+over-relover,dc1[1]+j-1+overy]=1
                        except TypeError:
                            pass
                        relover,relovery=0,0
                    if action=='tree':
                        
                        try:
                            for i in range(dc2[0]-dc1[0]+1+relover):
                                for j in range(dc2[1]-dc1[1]+1):
                                    if x[dc1[0]+i+over,dc1[1]+j-1+overy]=='tree':
                                        tasks[dc1[0]+i+over-relover,dc1[1]+j-1+overy]=2
                        except TypeError:
                            pass
                        relover,relovery=0,0
                    if action=='rmdig':
                        
                        try:
                            for i in range(dc2[0]-dc1[0]+1+relover):
                                for j in range(dc2[1]-dc1[1]+1):
                                    tasks[dc1[0]+i+over-relover,dc1[1]+j-1+overy]=0
                        except TypeError:
                            pass
                        relover,relovery=0,0
            
           
                
                
            
            
        
            
                
        
        try:
        
            stdscr.addstr(10,offset,"                     ")
            for tile_type in tile_types:
                    if (
                        x[cursorx-1+over][cursory+overy] == tile_type or 
                        x[cursorx+1+over][cursory+overy] == tile_type or 
                        x[cursorx+over][cursory-1+overy] == tile_type or 
                        x[cursorx+over][cursory+1+overy] == tile_type
                    ):
                        stdscr.addstr(0, offset, f"Tile: {x[cursorx+over][cursory+overy-1]}")
                        
                        break
            if stockpile[cursorx+over][cursory+1+overy] != 0:
                stdscr.addstr(3,offset,'stockpile: '+str(stockpile[cursorx+over][cursory+overy]))
            
                
            if x[cursorx+over][cursory+overy-1] not in solids:
                stdscr.addstr(1, offset, f"Items: {get_items(cursorx+over,cursory+overy-1,items)}")
        except:
            pass
        
        #test animal
        if t == 800:
                beg3=time.time()
        

        for i in dwarves:    
            if i.task == 'idle' or i.task == 'Idle':
                if t % 31 == 0:
                
                
                    i.task='Pathing'
             





            
        
        for i in entities:
            if i.health <=0:
                i.goto(10000,10000)
                entities.remove(i)
        
            '''    
            try:
                if x[i.posx+over][i.posy] != 'stone' and x[i.posx+over][i.posy] != 'water' and x[i.posx+over][i.posy] != 'tree' and x[i.posx+over][i.posy] != 'iron_ore' and x[i.posx+over][i.posy] != 'silver_ore' and x[i.posx+over][i.posy] != 'gold_ore':
                    qqqq=1
                else:
                    i.goto(i.oldposx,i.oldposy)
                    
            except:
                pass
            
            '''
            if playing % 2 == 1:
                    if i.golex == None:
                            if (t+i.movetime) % i.speed == 0:
                                i.age()
                                qq=i.update_pos()
                                try:
                                        if x[qq[1]+over, qq[0]+overy] not in solids:
                                                i.goto(qq[0],qq[1])
                                except:
                                        pass
                                
                                        
                                
            for i in entities:
                if i.behav==1:
                    r=random.randint(0,5)
                    xs=[]
                    ys=[]
                        
                    for j in entities:
                        if j.tame == 0:
                            xs.append(j.posx)
                            ys.append(j.posy)
                    dis=[]
                    for j in range(len(xs)):
                                
                        if entities[j].tame == 0:
                            dist=math.sqrt((xs[j]-i.posx)**2 + (ys[j]-i.posy)**2)
                            if dist == 0:
                                dis.append(10000)
                            else:
                                dis.append(dist)
                    if min(dis) <= 40:
                        if r == 2:
                            i.golex = 'SHunt'
                            i.goley = 'SHunt'
                        
            
            
            if t % 4 <= 3:
                if i.golex == 'SHunt' and i.goley == 'SHunt':
                        if i.behav==1:
                            i.golex="Hunt"
                            i.goley="Hunt"
                            
                        
                        
                            r=random.random()
                            if r > -1:
                                i.state=1
                            xs=[]
                            ys=[]
                        
                            for j in entities:
                                if j.tame == 0:
                                    xs.append(j.posx)
                                    ys.append(j.posy)
                            dis=[]
                            for j in range(len(xs)):
                                
                                if entities[j].tame == 0:
                                    dist=math.sqrt((xs[j]-i.posx)**2 + (ys[j]-i.posy)**2)
                                    if dist != 0:
                                        dis.append(dist)
                            counter=0
                            for j in dis:
                                if j == min(dis):
                                    break
                                else:
                                    counter+=1
                            try:
                                q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posx, i.posy),(xs[counter], ys[counter]) )

                        
                                if q == None:
                                    i.state=0
                                    
                            
                            
                                if q != None:
                                    first_elements = [x[0] for x in q]
                                    second_elements = [x[1] for x in q]
                            except:
                                pass
                                    
                                
                                
                            
                            try:
                                if playing % 2 == 1:
                                    i.goto(first_elements[1],second_elements[1])
                                for k in entities:
                                    if k.posx == i.posx:
                                        if k.posy == i.posy:
                                            if k != i:
                                                write_announcement(str(i.name)+' has engaged '+str(k.name)+' in conflict'+'\n')
                                                for v in range(5):
                                                    r=random.randint(0,10)
                                                    if r > k.agility:
                                                        k.health -= i.strength
                                                        if k.health <= 0:
                                                            i.golex=None
                                                            i.goley=None
                                                            state=0
                                                        r=random.randint(0,10)
                                                        if r > i.agility:
                                                            i.health -= k.strength
                            except:
                                
                                                        
                                                
                                        
                                
                                i.golex=None
                                i.goley=None
                                pass

                
                
                
               
                        
            
            
                        
        #check if stockpile open
        if t % 213 == 0:
        
            for j in range(X):
                for k in range(Y):
                    if stockpile[j][k] == 1:
                        if get_items(j,k,items) == []:
                            #openstock=1
                            for J in range(X):
                                for K in range(Y):
                                    for I in furniture:
                                        if I in get_items(J,K,items):
                                            if stockpile[J][K] != 1:
                                                
                                            
                                            
                                                for B in dwarves:
                                                    if B.get_goal()==None:
                                                    
                                                            B.drop_item=[j,k,I,1]
                                                            B.get_item=I
                                                            break
                                                        
                            break
                    if stockpile[j][k] == 2:
                        if get_items(j,k,items) == []:
                            #openstock=2
                            for J in range(X):
                                for K in range(Y):
                                    
                                    
                                    for I in building_items:
                                        if I in get_items(J,K,items):
                                            if stockpile[J][K] != 2:
                                                #stdscr.addstr(23,62,str(stockpile[J][K]))
                                                
                                            
                                            
                                                for B in dwarves:
                                                    if B.get_goal()==None:
                                                    
                                                            B.drop_item=[j,k,I,2]
                                                            B.get_item=I
                                                            break
                                                        
                            break
                        
                         
                            
                            
                       
        if t == 800:
                beg5=time.time()
        
        
      
        new_entities = []
        for i in entities:
            if i.time % i.birth == 0:
                for j in range(i.litter):
                    
                    new_entity = creatures.Creature(str(i.shape), int(i.color), i.posx, i.posy, str(i.name), i.strength, i.agility, i.size, i.speed, i.litter, i.birth,0,i.health,0,i.behav)
                    new_entities.append(new_entity)
                

        #add the new entities to the main list
        entities.extend(new_entities)

        
        #save pathfinding
        if t % 30 == 0:
            x_2=np.zeros((X,Y))
            for j in range(X):
                for i in range(Y):
                    if x[j][i] in solids:
                        x_2[j][i] = 1
                    
            np.savetxt(str(maindir)+'/region/pathfind.data',x_2)
        
        
        #to update tasks
        if t % 5 == 0:
            task1c=0
            task2c=0
            
            for j in range(X):
                for k in range(Y):
                    if tasks[j][k]==1:
                        task1c=1
                        break
                    elif tasks[j][k]==2:
                        task2c=1
                        break
        
        for i in entities:
                if i.posy < 60:
                    try:
                                
                        stdscr.addstr(i.posx+1,i.posy,i.shape)
                    except curses.error:
                        pass
        for i in dwarves:
                if i.health <=0:
                    i.goto(10000,10000)
                    dwarves.remove(i)
                
                

                if playing % 2 == 1:
                    ##stockpile haul
                    
                    #
                    
                    if 'axe' in i.possessions and 'woodcutter' in i.professions:
                        if task2c==1:
                                    i.set_goal('chop chop')
                        else:
                            i.task='idle'
                                    
                    if 'pickaxe' in i.possessions and 'miner' in i.professions:
                        if task1c==1:
                                    i.set_goal('mine')
                        else:
                            i.task='idle'
                                    
                    
                    if i.get_item!=None:
                        i.set_goal('item_fetch')
                    if i.drop_item!=None:
                        if i.drop_item[2] in i.possessions:
                            
                        
                            i.set_goal('item_drop')
                        
                    if i.get_build() != None:
                        cc=0
                        for ccc in i.possessions:
                            if ccc in item_list:
                                cc=1
                        if cc==1:
                            
                            i.set_goal('build')
                    if i.get_craft() != None:
                        cc=0
                        for ccc in i.possessions:
                            if ccc in item_list:
                                cc=1
                        if cc==1:
                            i.set_goal('craft')
                            
                    if i.task == 'idle':
                            if t % i.speed == 0:
                                i.age()
                                qq=i.update_pos()
                                try:
                                        if x[qq[1]+over, qq[0]+overy] not in solids:
                                                i.goto(qq[0],qq[1])
                                except:
                                        pass
                    if i.task=='Pathing':
                        i.q=None
                        if t > 5:
                            qqq=i.get_goal()
                            if qqq=='craft':
                                            
                                            c=0
                                

                                     
                                            i.task='Path'
                                              
                                            if c != 1:    
                                                
                                                qq=i.get_craft()
                                                try:
                                                    i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(qq[0], qq[1]) )
                                                    i.first_elements = [x[0] for x in i.q]
                                                    i.second_elements = [x[1] for x in i.q]
                                                    c=1
                                                except:
                                                    i.q=None
                                                    i.none_craft()
                                                    i.task='idle'
                            if qqq=='build':
                                            
                                            
                                            c=0
                                

                                     
                                            i.task='Path'
                                              
                                            if c != 1:    
                                                
                                                qq=i.get_build()
                                                try:
                                                    i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(qq[0], qq[1]) )
                                                    i.first_elements = [x[0] for x in i.q]
                                                    i.second_elements = [x[1] for x in i.q]
                                                    c=1
                                                except:
                                                    i.q=None
                                                    i.none_build()
                                                    i.task='idle'
                            if qqq=='item_fetch':
                                c=0
                                for j in range(X):
                                    for k in range(Y):
                                        
                                        if i.get_item in get_items(j,k,items):

                                     
                                            i.task='Path'
                                              
                                            if c != 1:    
                                                
                                                
                                                try:
                                                    i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(j, k) )
                                                    i.first_elements = [x[0] for x in i.q]
                                                    i.second_elements = [x[1] for x in i.q]
                                                    c=1
                                                except:
                                                    i.task='idle'
                                                    i.q=None
                            if qqq=='item_drop':
                                            c=0
                                            
                                

                                     
                                            i.task='Path'
                                              
                                            if c != 1:    
                                                
                                                
                                                try:
                                                    i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(i.drop_item[0], i.drop_item[1]) )
                                                    i.first_elements = [x[0] for x in i.q]
                                                    i.second_elements = [x[1] for x in i.q]
                                                
                                                
                                                except:
                                                    
                                                    i.task='idle'
                                                    i.q=None
                                                  
                                        
                                                   
                                                
                            
                            if qqq=='mine':
                                c=0
                                for j in range(X):
                                    for k in range(Y):
                                        
                                        if tasks[j][k]== 1:

                                     
                                                i.task='Path'
                                                #if x[j-1][k] in tile_types or x[j+1][k] in tile_types or x[j][k+1] in tile_types or x[j][k-1] in tile_types or x[j][k] in tile_types:
                                              
                                                if c != 1:    
                                                
                                                
                                                    try:
                                                        if x[j-1][k] in tile_types:
                                                            i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(j-1, k) )
                                                            i.first_elements = [x[0] for x in i.q]
                                                            i.second_elements = [x[1] for x in i.q]
                                                            c=1
                                                    except:
                                                        pass
                                                if c != 1:
                                                    try:
                                                        if x[j+1][k] in tile_types:
                                                            i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(j+1, k) )
                                                            i.first_elements = [x[0] for x in i.q]
                                                            i.second_elements = [x[1] for x in i.q]
                                                            c=1
                                                    except:
                                                        pass
                                                if c != 1:
                                                    try:
                                                        if x[j][k+1] in tile_types:
                                                            
                                                            i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(j, k+1) )
                                                            i.first_elements = [x[0] for x in i.q]
                                                            i.second_elements = [x[1] for x in i.q]
                                                            c=1
                                                    except:
                                                        
                                                        pass
                                                if c != 1:
                                                    try:
                                                        if x[j][k-1] in tile_types:
                                                            i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(j, k-1) )
                                                            i.first_elements = [x[0] for x in i.q]
                                                            i.second_elements = [x[1] for x in i.q]
                                                            c=1
                                                    except:
                                                        pass
                                                if c == 0:
                                                    i.q=None
                                                
                                                
                                                    
                                                   
                                                    i.task='idle'
                            if qqq=='chop chop':
                                c=0
                                for j in range(X):
                                    for k in range(Y):
                                        
                                        if tasks[j][k]== 2:

                                     
                                            i.task='Path'
                                              
                                            if c != 1:    
                                                
                                                
                                                try:
                                                    i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(j-1, k) )
                                                    i.first_elements = [x[0] for x in i.q]
                                                    i.second_elements = [x[1] for x in i.q]
                                                    c=1
                                                except:
                                                    pass
                                            if c != 1:
                                                try:
                                                    i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(j+1, k) )
                                                    i.first_elements = [x[0] for x in i.q]
                                                    i.second_elements = [x[1] for x in i.q]
                                                    c=1
                                                except:
                                                    pass
                                            if c != 1:
                                                try:
                                                    i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(j, k+1) )
                                                    i.first_elements = [x[0] for x in i.q]
                                                    i.second_elements = [x[1] for x in i.q]
                                                    c=1
                                                except:
                                                    pass
                                            if c != 1:
                                                try:
                                                    i.q=pathfinding.main(np.loadtxt(str(maindir)+'/region/pathfind.data'),(i.posy+over, i.posx+overy),(j, k-1) )
                                                    i.first_elements = [x[0] for x in i.q]
                                                    i.second_elements = [x[1] for x in i.q]
                                                    c=1
                                                except:
                                                    pass
                                            if c == 0:
                                                    i.q=None
                                                    
                                                    i.task='idle'
                                                    
                                            
                                            
                                                
                           
                        
                    if i.task=='Path':
                        
                            
                            
                        
                        
                                    
                            #issue. they all follow 
                            
                            if i.q != None:
                                
                                i.pathx=i.first_elements
                                i.pathy=i.second_elements
                            else:
                                i.pathx=[]
                                i.pathy=[]
                            if i.get_goal() == 'item_drop':
                                    
                                    
                                    yy=i.posx+overy
                                    xx=i.posy+over
                                    

                                    
    
                                    
                                            
                                    if xx==i.drop_item[0] and yy == i.drop_item[1]:
                                        i.possessions.remove(i.drop_item[2])
                                        add_item(xx,yy,i.drop_item[2],items)
                                        stockpile[xx,yy]=i.drop_item[3]
                                        
                                        i.task='idle'
                                        i.drop_item=None
                                        i.set_goal(None)
                                        i.drop_item=None
                            
                                    
                                
                                
                            
                            try:
                                if i.get_goal() == 'item_fetch':
                                    
                                    yy=i.posx+overy
                                    xx=i.posy+over
                                    

                                    
    
                                    if i.get_item in get_items(xx,yy,items):
                                            
        
                                        i.possessions.append(i.get_item)
                                        remove_item(xx,yy,i.get_item,items)
                                        i.task='idle'
                                        i.set_goal(None)
                                        i.get_item=None
                                    elif len(i.pathx) == 1:
                                        i.task='idle'
                                ##copied from
                                    
                                if i.get_goal() == 'build':
                                    
                                    
                                    yy=i.posx+overy
                                    xx=i.posy+over
                                    

                                    
    
                                    if x[i.posy+over,i.posx+overy] == 'unbuilt_carpenter_workshop':
                                    
                                        for cccc in i.possessions:
                                            if cccc in item_list:
                                                qqqq=cccc
                                                i.possessions.remove(cccc)
                                                for WW in range(len(item_list)):
                                                        if cccc == item_list[WW]:
                                                            for J in range(3):
                                                                for K in range(3):
                                                                    workshop_color[i.posy+over+J,i.posx+overy+K]=item_color[WW]
                                                break
                                        i.counter+=1
                                        if i.counter == 200:
                                            cc=0
                                            for J in range(3):
                                                for K in range(3):
                                                    x[i.posy+over+J,i.posx+overy+K]='carpenter'+str(cc)   
                                                    cc+=1
                                        
                                            i.task='idle'
                                            i.counter=0
                                            i.set_goal(None)
                                            i.get_item=None
                                            i.none_build()
                                    if x[i.posy+over,i.posx+overy] == 'unbuilt_mason_workshop':
  
                                        for cccc in i.possessions:
                                            if cccc in item_list:
                                                qqqq=cccc
                                                i.possessions.remove(cccc)
                                                for WW in range(len(item_list)):
                                                        if cccc == item_list[WW]:
                                                            for J in range(3):
                                                                for K in range(3):
                                                                    workshop_color[i.posy+over+J,i.posx+overy+K]=item_color[WW]
                                                break
                                        i.counter+=1
                                        if i.counter == 200:
                                            cc=0
                                            for J in range(3):
                                                for K in range(3):
                                                    x[i.posy+over+J,i.posx+overy+K]='mason'+str(cc)
                                                    
                                                        
                                                        
                                                    cc+=1
                                        
                                            i.task='idle'
                                            i.counter=0
                                            i.set_goal(None)
                                            i.get_item=None
                                            i.none_build()


                                ########
                                if i.get_goal() == 'craft':
                                    
                                    yy=i.posx+overy
                                    xx=i.posy+over
                                    

                                    
    
                                    if x[i.posy+over,i.posx+overy] in workshops:
                                        
                                    
                                        for cccc in i.possessions:
                                            if cccc in item_list:
                                                qqqq=cccc
                                                i.possessions.remove(cccc)
                                                
                                                break
                                        i.counter+=1
                                        if i.counter == 70:
                                            
                                            
                                            add_item(i.posy+over,i.posx+overy,i.make_item,items)
                                            i.make_item=None
                                            
                                        
                                            i.task='idle'
                                            i.counter=0
                                            i.set_goal(None)
                                            i.get_item=None
                                            i.none_craft()
                                    


                                            
                                if playing % 2 == 1:
                                    if (t+i.step) % 4 == 0:
                                    
                                        #if abs(i.pathy[1]-i.posx)<=2:
                                        i.goto(i.pathy[1]-overy,i.pathx[1]-over)
                                      
                                        del i.pathx[0]
                                        del i.pathy[0]
                                    
                            except:
                                
                                        
                                        
                                                        
            
                                             
                                    
                                
                                if i.get_goal() == 'mine':
                                    yy=i.posx+overy
                                    xx=i.posy+over
                                    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # Up, Down, Right, Left

                                    for dx, dy in directions:
                                        nx, ny = xx + dx, yy + dy
    
                                        if 0 <= nx < len(tasks) and 0 <= ny < len(tasks[1]) and tasks[nx][ny] == 1:
                                            tasks[nx][ny] = 0
                                            
        
                                            if x[nx][ny] in solids:
                                                mined=x[nx][ny]
                                                x[nx][ny] = 'cavern_floor'
                                                r=random.randint(1,4)
                                                if r == 2:
                                                    if mined == 'slate':
                                                        add_item(nx,ny,'slate_pebble',items)
                                                    elif mined == 'talc':
                                                        add_item(nx,ny,'talc_pebble',items)
                                                    elif mined == 'basalt':
                                                        add_item(nx,ny,'basalt_pebble',items)
                                                        
            
                                            break 
                                    i.task='idle'
                                    i.set_goal(None)
                                if i.get_goal() == 'chop chop':
                                    yy=i.posx+overy
                                    xx=i.posy+over
                                    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # Up, Down, Right, Left

                                    for dx, dy in directions:
                                        nx, ny = xx + dx, yy + dy
    
                                        if 0 <= nx < len(tasks) and 0 <= ny < len(tasks[0]) and tasks[nx][ny] == 2:
                                            
                                            r=random.randint(1,6)
                                            if x[nx][ny] == 'tree':
                                                if r==1:
                                                    tasks[nx][ny] = 0
                                                    x[nx][ny] = 'grass'
                                                
                                                    add_item(nx,ny,'wood',items)
            
                                            break 
                                    i.task='idle'
                                    i.set_goal(None)
                                        
                                    
        for i in dwarves:        
            if i.posy < 60:
                    try:
                        if i.professions[0] == 'miner':  
                            stdscr.addstr(i.posx+1,i.posy,i.shape,curses.color_pair(10))
                        if i.professions[0] == 'woodcutter':  
                            stdscr.addstr(i.posx+1,i.posy,i.shape,curses.color_pair(8))
                        if i.professions[0] == 'mason':  
                            stdscr.addstr(i.posx+1,i.posy,i.shape)
                        if i.professions[0] == 'carpenter':  
                            stdscr.addstr(i.posx+1,i.posy,i.shape,curses.color_pair(8))
                    except curses.error:
                        pass
            
        ##
        '''
            if 'carpenter' in i.professions:
                    stdscr.addstr(21,62,str(i.goal)+'@'+str(i.task))
                    stdscr.addstr(32,62,str(i.q))

        ##
        '''
                
                
        if t % 2 == 0:
            qqqq=fps_counter.update()
        try:
            stdscr.addstr(0,0,qqqq,curses.color_pair(6))
        except:
            pass
        
        if menu == 'main':
            main_menu_print(stdscr)
        elif menu == 'designation':
            designation_menu_print(stdscr)
        elif menu == 'building':
            building_menu_print(stdscr)
        elif menu == 'workshop':
            workshop_menu_print(stdscr)
        elif menu == 'query':
            query_menu_print(stdscr)
        elif menu == 'carpenter_crafting':
            carpenter_crafting_menu_print(stdscr)
        elif menu == 'mason_crafting':
            mason_crafting_menu_print(stdscr)
        elif menu == 'stockpile':
            stockpile_menu_print(stdscr)
        ####Waves
            
        ####Tree Growth/Sapling
        if playing % 2 == 1:
            if t % 2001 == 0:
                for i in range(X):
                    for j in range(Y):
                        if x[i][j]=='sapling':
                        
                            r=random.randint(0,40000)
                            if r == 1:
                                x[i][j]='tree'
            if (t+456) % 2001 == 0:
                for i in range(X):
                    for j in range(Y):
                        if x[i][j]=='grass':
                        
                            r=random.randint(0,80000)
                            if r == 1:
                                x[i][j]='sapling'
            
        '''   
        for i in dwarves:
            if 'carpenter' in i.professions:
                stdscr.addstr(28,62,x[i.posy+over,i.posx+overy])
                stdscr.addstr(29,62,str(i.posx+overy)+'-'+str(i.posy+over))
                stdscr.addstr(30,62,str(i.get_goal()))
        '''
        
        stdscr.refresh()
        stdscr.addstr(19,62,str(get_items(0,0,items)))
        if t == 500:
                f=open('milestone','a')
                f.write('\n'+str(time.time()-tim))
                f.close()

        stdscr.addstr(0,30,str(menu))
        #Overclocking
        time.sleep(.02)
        '''
        #Item saving
        if t % 200 == 0:
            np.savetxt(str(maindir)+'/fort/items.data',items)
        
        '''
     
        
        
    #stdscr.refresh()








curses.endwin()
