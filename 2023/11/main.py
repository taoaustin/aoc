def rotate(mat):
    res = []
    for i in range(len(mat[0])):
        line = []
        for j in range(len(mat)):
            line.append(mat[j][i])
        res.append(line)
    return res

def get_total_distance(coords, doubled_rows, doubled_cols, expansion):
    res = 0
    for i in range(len(coords)):
        for j in range(i, len(coords)):
            coord1 = coords[i]
            coord2 = coords[j]
            row_factor = 0 
            for k in doubled_rows:
                if (min(coord1[0], coord2[0]) < k and max(coord1[0], coord2[0]) > k):
                    row_factor += 1
            row_dist = (abs(galaxy_coords[i][0] - galaxy_coords[j][0]) - row_factor) + (row_factor * expansion)
            col_factor = 0
            for k in doubled_cols:
                if (min(coord1[1], coord2[1]) < k and max(coord1[1], coord2[1]) > k):
                    col_factor += 1
            col_dist = (abs(galaxy_coords[i][1] - galaxy_coords[j][1]) - col_factor) + (col_factor * expansion)
            res += (row_dist + col_dist)
    return res

if __name__ == "__main__":
    input = [list(line) for line in open("input.txt").read().splitlines()]
    doubled_rows = [index for index, line in enumerate(input) if "#" not in line]
    doubled_cols = [index for index, line in enumerate(rotate(input)) if "#" not in line]
    galaxy_coords = [(row, col) for row in range(len(input)) for col in range(len(input[0])) if input[row][col] == "#"]
    silver = get_total_distance(galaxy_coords, doubled_rows, doubled_cols, 2)
    print(f"Part 1: {silver}")
    gold = get_total_distance(galaxy_coords, doubled_rows, doubled_cols, 1000000)
    print(f"Part 2: {gold}")

