import numpy as np
import matplotlib.pyplot as plt

def create_river(array, width=4, bend_factor=.9):
    # Get dimensions of the array
    rows, cols = array.shape
    
    # Starting point for the river
    current_x, current_y = 0, cols // 2
    
    while current_x < rows:
        # Create the river width
        for i in range(-width//2, width//2):
            if 0 <= current_y + i < cols:
                array[current_x, current_y + i] = 1
        
        # Randomly change direction to create bends with a larger curve
        direction = np.random.choice(['left', 'right', 'straight'], p=[bend_factor/2, bend_factor/2, 1-bend_factor])
        if direction == 'left' and current_y - 1 >= 0:
            current_y -= 1
        elif direction == 'right' and current_y + 1 < cols:
            current_y += 1
        
        # Move the river downward
        current_x += 1
        
    return array






