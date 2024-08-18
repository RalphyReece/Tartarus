# Tartarus

Based on Dwarffortress. A very simplified approach meant to run inside the terminal.

Important things to note

Micro Worldsize is the only available size. 
Little gameplay available (chairs, tables, 2 workshops, mining, tree cutting, stockpiles (wip)
Many bugs at this state.
Rendering bugs can cause flashing lights. (Especially on Alacritty and Kitty Terminals.)

System Requirements:

Python 3+ 
pip3/pip

Gpu requirement: Ascii-based, any gpu at all can run.
Cpu requirement: 3GHz+ is maximum fps, can run semi well on as low as 1GHz.
Battery: A lot.
Ram: Uses tiny amounts of ram. 500MB will be sufficient for default sized worlds. A beginning world uses 260MB when idle, 360 when running entity simulations.


  
  
  You can also "overclock" the game by removing the time.sleep() at the end of the Tartarus.py file. This will speed the game up to 2x performance, with major risks, 

Underclocking:
  Changing the time.sleep(.02) to a higher number can allow the cpu more rest time. This will cap the framerate slower, but also makes it run reliably. (Recommended on low end devices)
