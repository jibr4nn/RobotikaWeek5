import heapq
import math

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    queue = [(0, start)]
    g_costs = {start: 0}
    came_from = {start: None}

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if current_node == goal:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current_node[0] + dx, current_node[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and not grid[neighbor[0]][neighbor[1]]:
                new_cost = g_costs[current_node] + 1
                if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                    g_costs[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(queue, (priority, neighbor))
                    came_from[neighbor] = current_node

    path, current = [], goal
    while current:
        path.append(current)
        current = came_from[current]
    return path[::-1]

# Contoh penggunaan
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
start, goal = (0, 0), (4, 4)
print("Jalur A*:", a_star(grid, start, goal))
