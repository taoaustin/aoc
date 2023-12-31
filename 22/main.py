from typing import List, Tuple

class Brick:
    def __init__(self, name, line):
        self.name = name
        parts = line.split("~")
        coord1 = [int(i) for i in parts[0].split(",")]
        coord2 = [int(i) for i in parts[1].split(",")]
        self.x = min(coord1[0], coord2[0])
        self.y = min(coord1[1], coord2[1])
        self.z = min(coord1[2], coord2[2])
        self.x_dist = abs(coord1[0] - coord2[0]) + 1
        self.y_dist = abs(coord1[1] - coord2[1]) + 1
        self.z_dist = abs(coord1[2] - coord2[2]) + 1
        self.supported_by = set()
        self.supports = set()

    def grid_coords_2D(self) -> List[Tuple[int, int]]:
        return [(self.x + i, self.y + j) for i in range(self.x_dist) for j in range(self.y_dist)]

def place_bricks(unsorted_bricks):
    grid: List[List[Tuple[int, int]]] = [[(-1, 0) for _ in range(10)] for _ in range(10)]
    bricks = sorted(unsorted_bricks, key=lambda b: b.z)
    for b in bricks:
        coords = b.grid_coords_2D()
        max_z = max(grid[r][c][1] for r, c in b.grid_coords_2D())
        max_z = max(0, max_z)
        for r, c in coords:
            if grid[r][c][1] == max_z and grid[r][c][0] != -1:
                b.supported_by.add(grid[r][c][0])
                unsorted_bricks[grid[r][c][0]].supports.add(b.name)
            grid[r][c] = (b.name, max_z + b.z_dist)

def drop_brick(unsorted_bricks, b_name):
    removed_brick = unsorted_bricks[b_name]
    dropped = set()
    q = [b for b in removed_brick.supports if len(unsorted_bricks[b].supported_by) == 1]
    while(q):
        b = unsorted_bricks[q.pop(0)]
        dropped.add(b.name)
        for supportee in b.supports:
            if unsorted_bricks[supportee].supported_by.issubset(dropped):
                q.append(supportee)
    return len(dropped)

unsorted_bricks = [Brick(i, line) for i, line in enumerate(open("input.txt").read().splitlines())]
place_bricks(unsorted_bricks)
bricks_that_cant_be_removed = set()
for b in unsorted_bricks:
    if len(b.supported_by) == 1:
        bricks_that_cant_be_removed.add(next(iter(b.supported_by)))
silver = len(unsorted_bricks) - len(bricks_that_cant_be_removed)
print(f"Part 1: {silver}")
gold = sum(drop_brick(unsorted_bricks, b_name) for b_name in bricks_that_cant_be_removed)
print(f"Part 2: {gold}")

