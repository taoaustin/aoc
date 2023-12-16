def HASH(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val



if __name__ == "__main__":
    input = [word for word in open("input.txt").read().strip().split(",")]
    hashes = [HASH(word) for word in input]
    lbl_hashes = [HASH(word.strip("-=0123456789")) for word in input]

    silver = sum(hashes)
    print(f"Part 1: {silver}")
    hashmap = [[] for _ in range(256)]
    for command, hash in zip(input, lbl_hashes):
        if (command[-1] == "-"):
            cur = hashmap[hash]
            for i, lbl in enumerate(cur):
                if lbl[0] == command[:-1]:
                    cur.pop(i)
        else:
            cur = hashmap[hash]
            flag = True
            for i, lbl in enumerate(cur):
                if lbl[0] == command[:-2]:
                    cur[i] = (command[:-2], int(command[-1]))
                    flag = False
            if flag:
                cur.append((command[:-2], int(command[-1])))
    gold = 0
    for i, lens_list in enumerate(hashmap):
        for j, len in enumerate(lens_list):
            gold += (i + 1) * (j + 1) * len[1]
    print(f"Part 2: {gold}")
