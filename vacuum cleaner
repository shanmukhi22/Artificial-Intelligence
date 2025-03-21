  
import random

def vacuum(grid):
    x, y = 0, 0
    while any(1 in row for row in grid):
        if grid[x][y]: print(f"Cleaning ({x}, {y})"); grid[x][y] = 0
        x, y = random.choice([(x + dx, y + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])])

vacuum([[1, 0, 1], [0, 1, 0], [1, 0, 0]])

              
        
