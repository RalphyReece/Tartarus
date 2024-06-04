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

'''
scene=0 is start
1 is main menu
2 is world creation




'''


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

    
    
    
    




stdscr = curses.initscr()
stdscr.keypad(True)
curses.curs_set(0)  # Hide the cursor
curses.start_color()
stdscr.nodelay(True)  # Make getch non-blocking
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
brown_approximation = 800 # Value between 0-1000 for approximating brown
curses.init_color(13, brown_approximation, brown_approximation // 2, 0)  # RGB values for brown
curses.init_pair(13, 13, curses.COLOR_BLACK)

#nettle
curses.init_color(14, 0, 220, 0)  # RGB values for brown
curses.init_pair(14, 14, curses.COLOR_BLACK)

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
        filename = str(maindir)+'/world/graphic.data'  # Replace with your file name
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
        worldgen.micro_region(biome,elev[embarky,embarkx])
        x=np.loadtxt(str(maindir)+'/region/region.data',dtype=object)
        for j in range(60):
            stdscr.refresh()
            for i in range(180):
                if x[i][j] == 'grass':
                    stdscr.addstr(j+1,i,'`',curses.color_pair(2))
                if x[i][j] == 'tree':
                    stdscr.addstr(j+1,i,'O',curses.color_pair(8))
                if x[i][j] == 'dead shrub':
                    stdscr.addstr(j+1,i,'&',curses.color_pair(9))
                
                if x[i][j] == 'sapling':
                    stdscr.addstr(j+1,i,'∂',curses.color_pair(11))

                if x[i][j] == 'mud':
                    stdscr.addstr(j+1,i,';',curses.color_pair(12))
                if x[i][j] == 'snow':
                    stdscr.addstr(j+1,i,'"',curses.color_pair(7))

                if x[i][j] == 'dirt':
                    stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                if x[i][j] == 'water':
                    stdscr.addstr(j+1,i,'≈',curses.color_pair(3))
                if x[i][j]== 'wood-wall':
                    stdscr.addstr(j+1,i,'#',curses.color_pair(8))
                if x[i][j]== 'wood-wall':
                    stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                '''
                if x[i][j] == 'iron-ore':
                    stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                if x[i][j] == 'copper-ore':
                    stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                if x[i][j] == 'silver-ore':
                    stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                if x[i][j] == 'gold-ore':
                    stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                '''
                    
                if x [i][j] == 'stone':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        

                    except:
                        pass
                
                        

              
                if x [i][j] == 'iron-ore':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                    except:
                        pass
                
                if x [i][j] == 'copper-ore':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                    except:
                        pass
                if x [i][j] == 'silver-ore':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                    except:
                        pass
                if x [i][j] == 'gold-ore':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                    except:
                        pass
        np.savetxt(str(maindir)+'/fort/fort.data',x,fmt='%s')
                
        scene='preplay'
                    
                    
                
                    
                
                    
                   
            
            
        stdscr.refresh()
            
            
        
            
        
        

        #
        t=0
        t2=0
        cursorx,cursory=1,1
        x=np.loadtxt(str(maindir)+'/fort/fort.data',dtype=object)
    if scene == 'preplay':
        t=0
        t2=0
        cursorx,cursory=1,1
        x=np.loadtxt(str(maindir)+'/fort/fort.data',dtype=object)
        #text animal
        entities=[]
        playing = 0
        
        rat= creatures.Creature('Y', 7, 30, 30, 'yak', 1, 1, 1, 1, 1,10000,0,1,0,0)
        entities.append(rat)
        
        rat= creatures.Creature('r', 7, 30, 30, 'rat', 1, 1, 1, 2, 3,10000,1,20,0,0)
        entities.append(rat)
        rat= creatures.Creature('d', 7, 30, 35, 'dog', 10, 1, 1, 2, 3,10000,0,50,0,1)
        
        entities.append(rat)
        scene='play'
    if scene == 'play':
        t+=1
        offset=181
        if key == ord(' '):
            playing+=1
        
        for j in range(60):
            stdscr.addstr(cursory,cursorx,"X")
            stdscr.addstr(cursory,cursorx,"X")
            for i in range(180):
                stdscr.addstr(j+1,i,' ')
                if x[i][j] == 'grass':
                    stdscr.addstr(j+1,i,'`',curses.color_pair(2))
                if x[i][j] == 'tree':
                    stdscr.addstr(j+1,i,'O',curses.color_pair(8))
                if x[i][j] == 'dead shrub':
                    stdscr.addstr(j+1,i,'&',curses.color_pair(9))
                
                if x[i][j] == 'sapling':
                    stdscr.addstr(j+1,i,'∂',curses.color_pair(11))

                if x[i][j] == 'mud':
                    stdscr.addstr(j+1,i,';',curses.color_pair(12))
                if x[i][j] == 'snow':
                    stdscr.addstr(j+1,i,'"',curses.color_pair(7))

                if x[i][j] == 'dirt':
                    stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                if x[i][j] == 'water':
                    stdscr.addstr(j+1,i,'≈',curses.color_pair(3))
                if x[i][j]== 'wood-wall':
                    stdscr.addstr(j+1,i,'#',curses.color_pair(8))
                if x[i][j]== 'peat':
                    stdscr.addstr(j+1,i,'&',curses.color_pair(13))
                if x[i][j] == 'nettle':
                    stdscr.addstr(j+1,i,'*',curses.color_pair(14))
                '''
                if x[i][j] == 'iron-ore':
                    stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                if x[i][j] == 'copper-ore':
                    stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                if x[i][j] == 'silver-ore':
                    stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                if x[i][j] == 'gold-ore':
                    stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                '''
                    
                if x [i][j] == 'stone':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='water' or x[i+1][j]=='water' or x[i][j-1]=='water' or x[i][j+1]=='water':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        if x[i-1][j]=='peat' or x[i+1][j]=='peat' or x[i][j-1]=='peat' or x[i][j+1]=='peat':
                            stdscr.addstr(j+1,i,'&',curses.color_pair(10))
                        

                    except:
                        pass
                
                        

                
                
                if x [i][j] == 'iron-ore':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='water' or x[i+1][j]=='water' or x[i][j-1]=='water' or x[i][j+1]=='water':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                        if x[i-1][j]=='peat' or x[i+1][j]=='peat' or x[i][j-1]=='peat' or x[i][j+1]=='peat':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(1))
                            
                    except:
                        pass
                
                if x [i][j] == 'copper-ore':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='water' or x[i+1][j]=='water' or x[i][j-1]=='water' or x[i][j+1]=='water':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                        if x[i-1][j]=='peat' or x[i+1][j]=='peat' or x[i][j-1]=='peat' or x[i][j+1]=='peat':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(9))
                    except:
                        pass
                if x [i][j] == 'silver-ore':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='water' or x[i+1][j]=='water' or x[i][j-1]=='water' or x[i][j+1]=='water':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                        if x[i-1][j]=='peat' or x[i+1][j]=='peat' or x[i][j-1]=='peat' or x[i][j+1]=='peat':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(10))
                    except:
                        pass
                if x [i][j] == 'gold-ore':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='water' or x[i+1][j]=='water' or x[i][j-1]=='water' or x[i][j+1]=='water':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                        if x[i-1][j]=='peat' or x[i+1][j]=='peat' or x[i][j-1]=='peat' or x[i][j+1]=='peat':
                            stdscr.addstr(j+1,i,'%',curses.color_pair(4))
                    except:
                        pass



                if x [i][j] == 'mudstone':
                    try:
                        if x[i-1][j]=='grass' or x[i+1][j]=='grass' or x[i][j-1]=='grass' or x[i][j+1]=='grass':
                            stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                        if x[i-1][j]=='sapling' or x[i+1][j]=='sapling' or x[i][j-1]=='sapling' or x[i][j+1]=='sapling':
                            stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                        if x[i-1][j]=='mud' or x[i+1][j]=='mud' or x[i][j-1]=='mud' or x[i][j+1]=='mud':
                            stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                        if x[i-1][j]=='tree' or x[i+1][j]=='tree' or x[i][j-1]=='tree' or x[i][j+1]=='tree':
                            stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                        if x[i-1][j]=='water' or x[i+1][j]=='water' or x[i][j-1]=='water' or x[i][j+1]=='water':
                            stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                        if x[i-1][j]=='peat' or x[i+1][j]=='peat' or x[i][j-1]=='peat' or x[i][j+1]=='peat':
                            stdscr.addstr(j+1,i,'#',curses.color_pair(9))
                        
                        

                    except:
                        pass
        np.savetxt(str(maindir)+'/fort/fort.data',x,fmt='%s')
        stdscr.addstr(cursory,cursorx,"X")

        if key == curses.KEY_UP:
              
            

                if cursory > 1:
                    cursory-=1
                    
        if key == curses.KEY_DOWN:
                
           
                
                if cursory < 59:
                    cursory+=1
                    

            
        if key == curses.KEY_LEFT:
            
                if cursorx > 1:
                    cursorx-=1
                    
            
        if key == curses.KEY_RIGHT:
                
                stdscr.refresh()
                if cursorx < 179:
                    cursorx +=1
        if key == ord('d'):
            x[cursorx][cursory-1] = 'grass'
            stdscr.refresh()
        try:
            stdscr.addstr(10,offset,"                     ")
            if x[cursorx-1][cursory]=='grass' or x[cursorx+1][cursory]=='grass' or x[cursorx][cursory-1]=='grass' or x[cursorx][cursory+1]=='grass':
                stdscr.addstr(10, offset, "Tile: " + str(x[cursorx][cursory-1]))
            if x[cursorx-1][cursory]=='sapling' or x[cursorx+1][cursory]=='sapling' or x[cursorx][cursory-1]=='sapling' or x[cursorx][cursory+1]=='sapling':
                stdscr.addstr(10, offset, "Tile: " + str(x[cursorx][cursory-1]))
            if x[cursorx-1][cursory]=='tree' or x[cursorx+1][cursory]=='tree' or x[cursorx][cursory-1]=='tree' or x[cursorx][cursory+1]=='tree':
                stdscr.addstr(10, offset, "Tile: " + str(x[cursorx][cursory-1]))
            if x[cursorx-1][cursory]=='mud' or x[cursorx+1][cursory]=='mud' or x[cursorx][cursory-1]=='mud' or x[cursorx][cursory+1]=='mud':
                stdscr.addstr(10, offset, "Tile: " + str(x[cursorx][cursory-1]))
            if x[cursorx-1][cursory]=='tree' or x[cursorx+1][cursory]=='tree' or x[cursorx][cursory-1]=='tree' or x[cursorx][cursory+1]=='tree':
                stdscr.addstr(10, offset, "Tile: " + str(x[cursorx][cursory-1]))
            if x[cursorx-1][cursory]=='tree' or x[cursorx+1][cursory]=='tree' or x[cursorx][cursory-1]=='tree' or x[cursorx][cursory+1]=='tree':
                stdscr.addstr(10, offset, "Tile: " + str(x[cursorx][cursory-1]))
            if x[cursorx-1][cursory]=='water' or x[cursorx+1][cursory]=='water' or x[cursorx][cursory-1]=='water' or x[cursorx][cursory+1]=='water':
                stdscr.addstr(10, offset, "Tile: " + str(x[cursorx][cursory-1]))
            if x[cursorx-1][cursory]=='peat' or x[cursorx+1][cursory]=='peat' or x[cursorx][cursory-1]=='peat' or x[cursorx][cursory+1]=='peat':
                stdscr.addstr(10, offset, "Tile: " + str(x[cursorx][cursory-1]))
            
        except:
            pass
        
        #test animal
        
        
        
        for i in entities:
            if i.health <=0:
                i.goto(10000,10000)
                entities.remove(i)
                
            try:
                if x[i.posx][i.posy] != 'stone' and x[i.posx][i.posy] != 'water' and x[i.posx][i.posy] != 'tree' and x[i.posx][i.posy] != 'iron_ore' and x[i.posx][i.posy] != 'silver_ore' and x[i.posx][i.posy] != 'gold_ore':
                    stdscr.addstr(i.posx, i.posy, str(i.shape))
                else:
                    i.goto(i.oldposx,i.oldposy)
            except:
                pass
            
            if t % 3 == 0:
                if playing % 2 == 1:
                    if i.golex == None:
                        i.update_pos()
                    i.age()
            
            
            
            if t % 3 == 0:
                if i.golex =='Hunt' and i.goley=='Hunt':
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
                                    dis.append(dis)
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
                                if playing == 1:
                                    i.goto(first_elements[1],second_elements[1])
                            except:
                                for k in entities:
                                    if k.posx == i.posx:
                                        if k.posy == i.posy:
                                            if k != i:
                                                for v in range(5):
                                                    r=random.randint(0,10)
                                                    if r > k.agility:
                                                        k.health -= i.strength
                                                        r=random.randint(0,10)
                                                        if r > i.agility:
                                                            i.health -= k.strength
                                                        
                                                
                                        
                                
                                i.golex=None
                                i.goley=None
                                pass

                
                
                
                    
                if i.golex==None and i.goley==None:
                    r=random.randint(0,30)
                    if r == 3:
                        
                    
                        
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
                                    dis.append(dis)
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
                                if playing == 1:
                                    i.goto(first_elements[1],second_elements[1])
                            except:
                                i.golex=None
                                i.goley=None
                                pass
                            

                            
                            
                        
                        
                        
            
            
                        
                            
                            
                            
                        
                

        # Next, spawn new entities
        new_entities = []
        for i in entities:
            if i.time % i.birth == 0:
                for j in range(i.litter):
                    # Spawn new entity at (10, 10) with the same species/stats
                    new_entity = creatures.Creature(str(i.shape), int(i.color), i.posx, i.posy, str(i.name), i.strength, i.agility, i.size, i.speed, i.litter, i.birth,0,i.health,0,i.behav)
                    new_entities.append(new_entity)
                

        # After iterating over all entities, add the new entities to the main list
        entities.extend(new_entities)


        #save pathfinding
        if t % 100 == 0:
            x_2=np.zeros((180,60))
            for j in range(180):
                for i in range(60):
                    if x[j][i] == 'stone' or x[j][i] == 'water' or x[j][i] == 'tree' or x[j][i] == 'copper-ore' or x[j][i] == 'silver-ore':
                        x_2[j][i] = 1
                    
            np.savetxt(str(maindir)+'/region/pathfind.data',x_2)
        
                
            
        
            
        stdscr.refresh()
        
        
        
        
            
            
        
        
        
        
        
        
        
        
        
    
            




    
    stdscr.refresh()








curses.endwin()
