import numpy as np
import heapq
import multiprocessing
import threading
import time
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic cost from current node to end node
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def astar_search(grid, start, end):
    def heuristic(a, b):
        # Manhattan distance heuristic
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Initialize start and end nodes
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Initialize open and closed lists
    open_list = []
    closed_list = set()

    # Add the start node
    heapq.heappush(open_list, start_node)

    # Loop until end node is found
    while open_list:
        # Pop node with lowest f value from open list
        current_node = heapq.heappop(open_list)

        # Add current node to closed list
        closed_list.add(current_node.position)

        # Found the goal
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate neighbors
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Ensure within grid bounds
            if node_position[0] < 0 or node_position[0] >= grid.shape[0] or node_position[1] < 0 or node_position[1] >= grid.shape[1]:
                continue

            # Skip obstacles
            if grid[node_position[0], node_position[1]] == 1:
                continue

            # Create neighbor node
            neighbor_node = Node(current_node, node_position)

            # Skip if neighbor node is in the closed list
            if neighbor_node.position in closed_list:
                continue

            # Calculate g, h, and f values
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, end)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # Skip if neighbor node is already in the open list with lower f value
            for open_node in open_list:
                if neighbor_node == open_node and neighbor_node.f > open_node.f:
                    break
            else:
                # Add neighbor node to open list
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example usage
def main(grid_array, start, end):
    # Define a function to run astar_search with a timeout
    def run_astar_search(grid_array, start, end):
        nonlocal path
        path = astar_search(grid_array, start, end)
    
    # Initialize path variable
    path = None
    
    # Create a new thread to run astar_search
    search_thread = threading.Thread(target=run_astar_search, args=(grid_array, start, end))
    search_thread.start()
    
    # Wait for the thread to finish or timeout
    search_thread.join(timeout=0.1)
    
    # If the thread is still alive (timeout occurred), set path to None
    if search_thread.is_alive():
        path = None
        
    
    return path

# Example usage:
# result = main(grid_array, start, end)

