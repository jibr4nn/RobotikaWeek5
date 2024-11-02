class Cell:
    def __init__(self, x, y, walkable=True):
        self.x = x
        self.y = y
        self.walkable = walkable
        self.parent = None

def cell_decomposition(grid, start, goal):
    open_cells = [start]
    closed_cells = set()
    path = []

    while open_cells:
        current = open_cells.pop(0)
        if current == goal:
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]

        closed_cells.add((current.x, current.y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny].walkable and (nx, ny) not in closed_cells:
                neighbor = grid[nx][ny]
                neighbor.parent = current
                open_cells.append(neighbor)
    return None

# Contoh penggunaan
grid = [[Cell(x, y, True) for y in range(5)] for x in range(5)]
grid[2][2].walkable = False
start, goal = grid[0][0], grid[4][4]
print("Jalur Cell Decomposition:", cell_decomposition(grid, start, goal))
