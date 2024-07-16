import numpy as np
import heapq
from concurrent.futures import ThreadPoolExecutor, as_completed
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
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = set()
    open_dict = {}

    heapq.heappush(open_list, start_node)
    open_dict[start_node.position] = start_node

    while open_list:
        current_node = heapq.heappop(open_list)
        open_dict.pop(current_node.position, None)

        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.position)

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] < 0 or node_position[0] >= grid.shape[0] or node_position[1] < 0 or node_position[1] >= grid.shape[1]:
                continue

            if grid[node_position[0], node_position[1]] == 1:
                continue

            if node_position in closed_list:
                continue

            neighbor_node = Node(current_node, node_position)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, end)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if node_position in open_dict and open_dict[node_position].f <= neighbor_node.f:
                continue

            heapq.heappush(open_list, neighbor_node)
            open_dict[node_position] = neighbor_node

    return None

def main(grid_array, start, end):
    def run_astar_search():
        return astar_search(grid_array, start, end)
    
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(run_astar_search)
        try:
            path = future.result(timeout=.3)
        except Exception:
            path = None
    
    return path

def dwarf_path(start, end,file):
    grid_array=np.loadtxt('region/pathfind.data')
    
    def run_astar_search():
        return astar_search(grid_array, start, end)
    
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(run_astar_search)
        try:
            path = future.result(timeout=1000)
        except Exception:
            path = None
    f=open(str(file),'w')
    if path != None:
        f.write(str(path))
    f.close()
    

# Example usage:
'''
grid_array = np.loadtxt('region/pathfind.data')
start = (0, 0)
end = (12,12)
result = main(grid_array, start, end)
print(result)

'''
