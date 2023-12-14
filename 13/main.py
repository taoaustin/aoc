def rotate(mat):
    res = []
    for i in range(len(mat[0])):
        line = ""
        for j in range(len(mat)):
            line += (mat[j][i])
        res.append(line)
    return res

def letter_diff(line1, line2):
    return sum(1 for char1, char2 in zip(line1, line2) if char1 != char2)

def find_mirror(mat):
    for i in range(1, len(mat)):
        mirror_at = i
        above = mirror_at - 1
        below = mirror_at
        flag = True
        while (above >= 0 and below < len(mat)):
            if (mat[above] != mat[below]):
                flag = False
                break
            above -= 1
            below += 1
        if flag:
            return i
    return 0 

def find_mirror_with_smudge(mat):
    for i in range(1, len(mat)):
        mirror_at = i
        above = mirror_at - 1
        below = mirror_at
        diff_chars = 0
        while (above >= 0 and below < len(mat)):
            diff_chars += letter_diff(mat[above], mat[below])
            above -= 1
            below += 1
        if (diff_chars == 1):
            return i
    return 0 

if __name__ == "__main__":
    input = [[line for line in pattern.splitlines()] for pattern in open("input.txt").read().split("\n\n")]
    silver = 0
    gold = 0
    for pattern in input:
        silver += find_mirror(pattern) * 100 + find_mirror(rotate(pattern))
        gold += find_mirror_with_smudge(pattern) * 100 + find_mirror_with_smudge(rotate(pattern))

    print(f"Part 1: {silver}")
    print(f"Part 2: {gold}")
     
