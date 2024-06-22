# Tartarus
###CURRENTLY IN ALPHA, AND NO GAMEPLAY IS YET ADDED###
Based on Dwarffortress. A very simplified approach meant to run inside the terminal.

Important things to note

Micro Worldsize is the only available size. Not all biomes have been completed.
Go for Alpine and Forest to see the most support
Currently no gameplay, just animals roaming and fighting.
Many bugs at this state.
Rendering bugs can cause flashing lights.

System Requirements:

Python 3+ 
pip3/pip

Gpu requirement: Ascii-based, any gpu at all can run.
Cpu requirement: Uses little at first, but will increase exponentially as the game progresses.
Battery: Uses a lot of battery, especially with high entity counts. Expect a couple hours charge on Intel processors. ARM lasts noticably longer.
Ram: Uses tiny amounts of ram. 500MB will be sufficient for default sized worlds. A beginning world uses 260MB when idle, 360 when running entity simulations.

Overclocking:
  Overclocking CPU can drastically increase performance on low end hardware (such as Raspberry pi models 3 and lower). 
  
  You can also "overclock" the game by removing the time.sleep() at the end of the Tartarus.py file. This will speed the game up to 2x performance, with major risks, as discussed below.

  time.sleep() removal can speed the game loop time from 2 milliseconds to 1. The removed wait time will cause the cpu to run continuously, instead of allowing breaks between loops. This will run faster until the cpu gets maxed out, and then drop the game speed to a crawl. This is not recommended, and should be used infrequently or phased in and out using loops, to allow the cpu to cool off/ rest.

Underclocking:
  Changing the time.sleep(.01) to a higher number can allow the cpu more rest time. This will cap the framerate slower, but also makes it run reliably.
