def walk_dir(mat, dir, row, col):
    height = len(mat)
    length = len(mat[0])
    mat[row][col][1] = True
    if dir == "up":
        row -= 1
        while ((row >= 0) and (mat[row][col][0] not in "/\\-|")):
            mat[row][col][1] = True
            row -= 1
    elif dir == "down":
        row += 1
        while ((row < height) and (mat[row][col][0] not in "/\\-|")):
            mat[row][col][1] = True
            row += 1
    elif dir == "left":
        col -= 1
        while ((col >= 0) and (mat[row][col][0] not in "/\\-|")):
            mat[row][col][1] = True
            col -= 1
    elif dir == "right":
        col += 1
        while ((col < length) and (mat[row][col][0] not in "/\\-|")):
            mat[row][col][1] = True
            col += 1

    if row < 0 or row >= height or col < 0 or col >= length:
        return (None, None)
    mat[row][col][1] = True
    return (row, col)

def reflect_beams(mat, dir, row, col):
    if row == None and col == None: return

    if dir in mat[row][col][2]: return
    else: mat[row][col][2].append(dir)

    mirror_type = mat[row][col][0]
    match mirror_type, dir:
        case ("/", "up") | ("\\", "down"):
            reflect_beams(mat, "right", *walk_dir(mat, "right", row, col))
        case ("/", "down") | ("\\", "up"):
            reflect_beams(mat, "left", *walk_dir(mat, "left", row, col))
        case ("/", "left") | ("\\", "right"):
            reflect_beams(mat, "down", *walk_dir(mat, "down", row, col))
        case ("/", "right") | ("\\", "left"):
            reflect_beams(mat, "up", *walk_dir(mat, "up", row, col))
        case ("-", "left") | ("-", "right") | ("|", "up") | ("|", "down") | (".", _):
            reflect_beams(mat, dir, *walk_dir(mat, dir, row, col))
        case ("-", "up") | ("-", "down"):
            reflect_beams(mat, "right", *walk_dir(mat, "right", row, col))
            reflect_beams(mat, "left", *walk_dir(mat, "left", row, col))
        case ("|", "left") | ("|", "right"):
            reflect_beams(mat, "up", *walk_dir(mat, "up", row, col))
            reflect_beams(mat, "down", *walk_dir(mat, "down", row, col))

def read_input():
    return [[[c, False, []] for c in line] for line in open("input.txt").read().splitlines()]

def get_energy(mat):
    return sum([1 if mat[i][j][1] else 0 for i in range(len(mat)) for j in range(len(mat[0]))])


if __name__ == "__main__":
    input = read_input()
    reflect_beams(input, "right", 0, 0)
    silver = get_energy(input)
    print(f"Part 1: {silver}")
    gold = silver
    for i in range(len(input)):
        input = read_input()
        reflect_beams(input, "right", i, 0)
        gold = max(gold, get_energy(input))
        input = read_input()
        reflect_beams(input, "left", i , len(input[0]) - 1)
        gold = max(gold, get_energy(input)) 
    for i in range(len(input[0])):
        input = read_input()
        reflect_beams(input, "down", 0, i)
        gold = max(gold, get_energy(input))
        input = read_input()
        reflect_beams(input, "up", len(input) - 1, i)
        gold = max(gold, get_energy(input)) 
    print(f"Part 2: {gold}")

