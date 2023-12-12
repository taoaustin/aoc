seq_lists = [[ [ int(intstr) for intstr in line.split(" ")] ] for line in open("input.txt").readlines()]
for seqs in seq_lists:
    while (len([n for n in seqs[-1] if n != 0]) != 0):
        next_seq_lvl = []
        for i in range(1, len(seqs[-1])):
            next_seq_lvl.append(seqs[-1][i] - seqs[-1][i - 1])
        seqs.append(next_seq_lvl)

silver = 0
gold = 0
for seqs in seq_lists:
    for i in range(len(seqs) - 1, 0, -1):
        seqs[i - 1].append(seqs[i - 1][-1] + seqs[i][-1])
        seqs[i - 1].insert(0, seqs[i - 1][0] - seqs[i][0])
    silver += seqs[0][-1]
    gold += seqs[0][0]
print(f"Part 1: {silver}")
print(f"Part 2: {gold}")
# could have done this recursively