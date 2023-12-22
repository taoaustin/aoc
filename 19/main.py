import operator

def parse_rule(rule_str):
    if ":" not in rule_str:
        return (0, operator.gt, 0, rule_str)
    str_spl = rule_str.split(":")
    if str_spl[0][1] == "<":
        op = operator.lt
    else:
        op = operator.gt
    return (idict[str_spl[0][0]], op, int(str_spl[0][2:]), str_spl[1])

def apply_rules(part, workflow):
    for rule in workflow:
        part_idx, op, val, res = rule
        if op(part[part_idx], val):
            return res

def accept_part(part, workflows):
    res = apply_rules(part, workflows["in"]) 
    while res != "A" and res != "R":
        res = apply_rules(part, workflows[res])
    if res == "A":
        return sum(part)
    return 0

def branch_ranges(my_ranges, w, workflows):
    if w == "A":
        accepted.add(tuple(tuple(r) for r in my_ranges))
        return
    if w == "R":
        return
    for i, rule in enumerate(workflows[w]):
        if i == len(workflows[w]) - 1:
            branch_ranges([r[:] for r in my_ranges], rule[3], workflows)
        else:
            new_ranges = [r[:] for r in my_ranges]
            if rule[1] == operator.lt:
                new_ranges[rule[0]][1] = rule[2] - 1
                my_ranges[rule[0]][0] = rule[2]
            else:
                new_ranges[rule[0]][0] = rule[2] + 1
                my_ranges[rule[0]][1] = rule[2]
            branch_ranges([r[:] for r in new_ranges], rule[3], workflows)

input = open("input.txt").read().split("\n\n")
idict = {"x": 0, "m": 1, "a": 2, "s": 3}
parts = [[int(n[2:]) for n in line[1:-1].split(",")] for line in input[1].splitlines()]
workflows = {
    line.split('{')[0]: [parse_rule(rule) for rule in line[:-1].split('{')[1].split(",")] 
    for line in input[0].splitlines()
} #  }} nvim treesitter not working right lmao
silver = 0
for part in parts:
    silver += accept_part(part, workflows)
print(f"Part 1: {silver}")
accepted = set()
branch_ranges([[1, 4000], [1, 4000], [1, 4000], [1, 4000]], "in", workflows)
gold = 0
for ranges in accepted:
    t1 = ranges[0][1] - ranges[0][0] + 1
    t2 = ranges[1][1] - ranges[1][0] + 1
    t3 = ranges[2][1] - ranges[2][0] + 1
    t4 = ranges[3][1] - ranges[3][0] + 1
    gold += (t1 * t2 * t3 * t4)
print(f"Part 2: {gold}")

