# completely stolen from reddit, could not get my recursion to work properly, my ass is filtered
def get_combinations(line, all_runs):
    if (len(line) == 0):
        res = 1 if len(all_runs) == 0 else 0
        dp[(line, all_runs)] = res
        return res

    if (len(all_runs) == 0):
        for c in line:
            if c == "#":
                dp[(line, all_runs)] = 0
                return 0
        return 1
    if (len(line) < sum(all_runs) + len(all_runs) - 1):
        dp[(line, all_runs)] = 0
        return 0

    if ((line, all_runs) in dp):
        return dp[(line, all_runs)]


    if (line[0] == "."):
        res = get_combinations(line[1::], all_runs)
        dp[(line, all_runs)] = res
        return res

    if (line[0] == "#"):
        for i in range(all_runs[0]):
            if line[i] == ".":
                dp[(line, all_runs)] = 0
                return 0

        if ((len(line) > all_runs[0]) and (line[all_runs[0]] == "#")):
            dp[(line, all_runs)] = 0
            return 0
        res = get_combinations(line[all_runs[0] + 1::], all_runs[1::])
        dp[(line, all_runs)] = res
        return res

    res = get_combinations("#" + line[1::], all_runs) + get_combinations("." + line[1::], all_runs)
    dp[(line, all_runs)] = res
    return res
    

if __name__ == "__main__":
    input = [(line.split()[0], tuple(int(s) for s in line.split()[1].split(","))) for line in open("input.txt").read().splitlines()]
    dp = {}
    silver = 0
    for pair in input:
        silver += get_combinations(pair[0], pair[1])
    print(f"Part 1: {silver}")
    gold_input = [((line + (("?" + line) * 4)), run_lens * 5) for (line, run_lens) in input]
    gold = 0
    for pair in gold_input:
        gold += get_combinations(pair[0], pair[1])
    print(f"Part 2: {gold}")
