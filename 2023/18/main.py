from typing import Dict, List, Tuple

def read_instructions_shoelace(input: List[Tuple[str, int]]):
    cur = (0, 0)
    cur_coord = (0, 0)
    term1 = 0
    term2 = 0
    for i in range(len(input) - 1):
        dir, mag = input[i]
        next_dir = input[i + 1][0]
        cur_offset = offset[(dir, next_dir)]
        step = ddict[dir]
        prev_coord = cur_coord
        cur = (cur[0] + step[0] * mag, cur[1] + step[1] * mag)
        cur_coord = (cur[0] + cur_offset[0], cur[1] + cur_offset[1])
        term1 += (prev_coord[0] * cur_coord[1])
        term2 += (prev_coord[1] * cur_coord[0])
    return abs(term1 - term2) // 2

ddict = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
offset: Dict[Tuple[str, str], Tuple[int, int]] = {
    ("U", "R"): (0, 0),
    ("U", "L"): (1, 0),
    ("D", "R"): (0, 1),
    ("D", "L"): (1, 1),
    ("R", "U"): (0, 0),
    ("R", "D"): (0, 1),
    ("L", "U"): (1, 0),
    ("L", "D"): (1, 1)
}
silver_input = [(line.split()[0], int(line.split()[1])) for line in open("input.txt").read().splitlines()]
silver = read_instructions_shoelace(silver_input)
print(f"Part 1: {silver}")
hexdir = {"0": "R", "1": "D", "2": "L", "3": "U"}
gold_input = [(hexdir[line.split()[2][-2]], int(line.split()[2][2:-2], 16)) for line in open("input.txt").read().splitlines()]
gold = read_instructions_shoelace(gold_input)
print(f"Part 2: {gold}")



