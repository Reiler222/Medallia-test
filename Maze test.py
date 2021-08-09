# X izquierda a derecha || Y arriba a abajo

def distance(a, b):
    """Distance between starting point and end point"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def explore(pos):
    """Given your actual position at the maze, return all possible combinations of movements"""
    x = pos[0]
    y = pos[1]  # Dividing coords into X and Y

    combinations = []

    # In order: Up, right, down, left
    if 0 <= (y - 1) <= MAX_SIZE:
        combinations.append([x, y - 1])
    if 0 <= (x + 1) <= MAX_SIZE:
        combinations.append([x + 1, y])
    if 0 <= (y + 1) <= MAX_SIZE:
        combinations.append([x, y + 1])
    if 0 <= (x - 1) <= MAX_SIZE:
        combinations.append([x - 1, y])

    return combinations

def sort_pos_by_dist(destiny, candidates):
    """ Step by step:
    Step 1: Marking all positions with an int showing the distance between that position and the end.
    Step 2: Sorting this the result list by the distances
    Step 3: Returning as a list only the positions"""
    step1 = [(p, distance(p, destiny)) for p in candidates]  
    step2 = sorted(step1, key=lambda x: x[1])
    return [p[0] for p in step2]


def calculate_path(laberinto):
    """Function for calculating the correct path to the end of the maze"""

    start = [0, 0]  # Your actual position
    finish = [MAX_SIZE, MAX_SIZE]  # Finish point
    candidates = [start]  # Possible path candidates
    visited = []  # Visited tiles
    path = []  # Work in progress

    while len(candidates) >= 0:  # Infinite loop. 
        candidates = sort_pos_by_dist(finish, candidates)
        start = candidates.pop(0)  # Extract your last position

        path.append(start)
        visited.append(start)

        possible = explore(start)
        if start == finish or finish in candidates:
            break
        for p in possible:
            x = p[0]
            y = p[1]
            cell = laberinto[y][x]
            if (cell != "1") and (p not in candidates) and (p not in visited):
                candidates.append(p)
                
    return visited

# TEST CASE

MAX_SIZE = 5

laberinto = [
    ["0", "0", "0", "0", "0", "1"],
    ["0", "1", "1", "1", "1", "0"],
    ["0", "0", "0", "0", "0", "1"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
]

print(calculate_path(laberinto))