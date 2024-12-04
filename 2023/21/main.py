from typing import List, Tuple

def find_s(grid, steps):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return (i, j, 0, 0,steps)
    return (0, 0, 0, 0, 0)

def is_valid(row, col, grid):
    return (row >= 0 
            and row < len(grid) 
            and col >= 0
            and col < len(grid[0]) 
            and grid[row][col] != "#")

def bfs_p1(grid, total_steps):
    row, col, _, _, steps = find_s(grid, total_steps)
    q: List[Tuple[int, int, int]] = [(row, col, steps)]
    visited = set()
    while(q):
        row, col, steps = q.pop(0) 
        if ((row, col) in visited): continue
        visited.add((row, col))
        if (steps % 2 == 0):
            if grid[row][col] != "S":
                grid[row][col] = "O"
        if steps == 0: continue
        if is_valid((row + 1), col, grid):
            q.append(((row + 1), col, steps - 1))
        if is_valid((row - 1), col, grid):
            q.append(((row - 1), col, steps - 1))
        if is_valid(row, (col + 1), grid):
            q.append((row, (col + 1), steps - 1))
        if is_valid(row, (col - 1), grid):
            q.append((row, (col - 1), steps - 1))

def bfs(grid, total_steps):
    cond = lambda x: x % 2 == 0
    q: List[Tuple[int, int, int, int, int]] = [find_s(grid, total_steps)]
    visited = set()
    while(q):
        row, col, pu_row, pu_col, steps = q.pop(0) # watch for rolling rocks in 0.5x a presses!
        if ((row, col, pu_row, pu_col) in visited): continue
        visited.add((row, col, pu_row, pu_col))
        if cond(steps):
            if type(grid[row][col]) is str:
                grid[row][col] = 1
            else:
                grid[row][col] += 1
        if steps == 0: continue
        if is_valid((row + 1) % len(grid), col, grid):
            q.append(((row + 1) % len(grid), col, pu_row + ((row + 1) // len(grid)), pu_col, steps - 1))
        if is_valid((row - 1) % len(grid), col, grid):
            q.append(((row - 1) % len(grid), col, pu_row + ((row - 1) // len(grid)), pu_col, steps - 1))
        if is_valid(row, (col + 1) % len(grid[0]), grid):
            q.append((row, (col + 1) % len(grid[0]), pu_row, pu_col + ((col + 1) // len(grid[0])), steps - 1))
        if is_valid(row, (col - 1) % len(grid[0]), grid):
            q.append((row, (col - 1) % len(grid[0]), pu_row, pu_col + ((col - 1) // len(grid[0])), steps - 1))


grid = [list(line) for line in open("input.txt").read().splitlines()]
bfs_p1(grid, 64)
silver = sum(1 for line in grid for c in line if c == "O" or c == "S")
print(f"Part 1: {silver}")
# cheated gold, its apparently extrapolating the first 3 results of steps=65, 196, 327 since the desired-steps % 131 == 65
# and fitting the results to a quadratic eq.
