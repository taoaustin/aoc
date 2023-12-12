def find_S(sketch):
    for i in range(len(sketch)):
        for j in range(len(sketch[i])):
            if (sketch[i][j] == 'S'):
                return (i, j)

def from_S(row, col, sketch):
    if sketch[row - 1][col] in "|F7": return (row - 1, col)
    if sketch[row + 1][col] in "|LJ": return (row + 1, col)
    if sketch[row][col - 1] in "-FL": return (row, col - 1)
    return (row, col + 1)

def get_next(prev, cur, sketch):
    if sketch[cur[0]][cur[1]] == "|":
        if (prev == (cur[0] - 1, cur[1])): return (cur[0] + 1, cur[1])
        return (cur[0] - 1, cur[1])
    if sketch[cur[0]][cur[1]] == "-":
        if (prev == (cur[0], cur[1] - 1)): return (cur[0], cur[1] + 1)
        return (cur[0], cur[1] - 1)
    if sketch[cur[0]][cur[1]] == "F":
        if (prev == (cur[0], cur[1] + 1)): return (cur[0] + 1, cur[1])
        return (cur[0], cur[1] + 1)
    if sketch[cur[0]][cur[1]] == "7":
        if (prev == (cur[0], cur[1] - 1)): return (cur[0] + 1, cur[1])
        return (cur[0], cur[1] - 1)
    if sketch[cur[0]][cur[1]] == "L":
        if (prev == (cur[0], cur[1] + 1)): return (cur[0] - 1, cur[1])
        return (cur[0], cur[1] + 1)
    if sketch[cur[0]][cur[1]] == "J":
        if (prev == (cur[0] - 1, cur[1])): return (cur[0], cur[1] - 1)
        return (cur[0] - 1, cur[1])

def create_2x_path(cur, type, sketch):
    if (type == "|"):
        sketch[2 * cur[0]][2 * cur[1]] = "|"
        sketch[2 * cur[0] + 1][2 * cur[1]] = "|"
    elif (type == "-"):
        sketch[2 * cur[0]][2 * cur[1]] = "-"
        sketch[2 * cur[0]][2 * cur[1] + 1] = "-"
    elif (type == "F"):
        sketch[2 * cur[0]][2 * cur[1]] = "F"
        sketch[2 * cur[0]][2 * cur[1] + 1] = "-"
        sketch[2 * cur[0] + 1][2 * cur[1]] = "|"
    elif (type == "7"):
        sketch[2 * cur[0]][2 * cur[1]] = "7"
        sketch[2 * cur[0] + 1][2 * cur[1]] = "|"
    elif (type == "L"):
        sketch[2 * cur[0]][2 * cur[1]] = "L"
        sketch[2 * cur[0]][2 * cur[1] + 1] = "-"
    elif (type == "S" or type == "J"): # S happens also to be a J in my input
        sketch[2 * cur[0]][2 * cur[1]] = type


def is_valid(sketch, width, height, row, col, prevC, newC):
    return (row >= 0 and row < height\
            and col >= 0 and col < width\
            and sketch[row][col] == prevC\
            and sketch[row][col] != newC)

def flood_fill(sketch, width, height, row, col, prevC, newC):
    queue = []
    queue.append([row, col])
    sketch[row][col] = newC
    while queue:
        cur = queue.pop(0)
        posX = cur[0]
        posY = cur[1]
        if is_valid(sketch, width, height, posX + 1, posY, prevC, newC):
            sketch[posX + 1][posY] = newC
            queue.append([posX + 1, posY])
        if is_valid(sketch, width, height, posX - 1, posY, prevC, newC):
            sketch[posX - 1][posY] = newC
            queue.append([posX - 1, posY])
        if is_valid(sketch, width, height, posX, posY + 1, prevC, newC):
            sketch[posX][posY + 1] = newC
            queue.append([posX, posY + 1])
        if is_valid(sketch, width, height, posX, posY - 1, prevC, newC):
            sketch[posX][posY - 1]= newC
            queue.append([posX, posY - 1])


sketch = [[c for c in line] for line in open("input.txt").read().splitlines()]
_2x_sketch = [["." for i in range(len(sketch[0]) * 2)] for j in range((len(sketch) * 2))]
s_loc = find_S(sketch)
double_silver = 1
cur = s_loc
create_2x_path(cur, sketch[cur[0]][cur[1]], _2x_sketch)
_next = from_S(*s_loc, sketch)
while (sketch[_next[0]][_next[1]] != "S"):
    create_2x_path(_next, sketch[_next[0]][_next[1]], _2x_sketch)
    _tmp = get_next(cur, _next, sketch)
    cur = _next
    _next = _tmp
    double_silver += 1
print(f"Part 1: {double_silver // 2}")

s_loc = find_S(_2x_sketch)
gold = 0
flood_fill(_2x_sketch, len(_2x_sketch[0]), len(_2x_sketch), s_loc[0], s_loc[1] + 1, ".", "I") # guess and print
for i in range(len(sketch)):
    for j in range(len(sketch[i])):
        if (_2x_sketch[2*i][2*j] == "I"):
            _2x_sketch[2*i][2*j] = "*"
            gold += 1
print(f"Part 2: {gold}")

# for line in _2x_sketch:
#     for char in line:
#         print(char, end="")
#     print()