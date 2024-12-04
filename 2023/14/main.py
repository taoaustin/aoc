def rotate(mat):
    res = []
    for i in range(len(mat[0])):
        line = ""
        for j in range(len(mat)):
            line = (mat[j][i]) + line
        res.append(line)
    return res

def tilt_line(line):
    return "#".join([move_rocks(substr) for substr in line.split("#")])

def move_rocks(rocks):
    return ("." * rocks.count(".")) + ("O" * rocks.count("O"))

def cycle(mat):
    for _ in range(4):
        mat = [tilt_line(line) for line in rotate(mat)]
    return mat

if __name__ == "__main__":
    input = [line for line in open("input.txt").read().splitlines()]
    tilted = rotate(rotate(rotate(([tilt_line(line) for line in rotate(input)]))))
    silver = sum([(len(line) - i) * line.count("O") for i, line in enumerate(tilted)])
    print(f"Part 1: {silver}")
    map = {}
    i = 1
    cycled = input
    cycle_cycle_len = -1
    cycle_cycle_start = -1
    while (True):
        cycled = cycle(cycled)
        load = sum([(len(line) - i) * line.count("O") for i, line in enumerate(cycled)])
        hash = "".join(cycled)
        if hash in map:
            cycle_cycle_start = map[hash][1]
            cycle_cycle_len = i - cycle_cycle_start
            break
        else:
            map[hash] = [load, i]
        i += 1  

    first_occurrence = ((1000000000 - cycle_cycle_start) % cycle_cycle_len) + cycle_cycle_start
    for v in map.values():
        if first_occurrence in v[1::]:
            print(f"Part 2: {v[0]}")

