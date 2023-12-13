import time

def get_first(line):
    for i in range(len(line)):
        if line[i] in "0123456789":
            return line[i]
        else:
            tmp = spelt_number(line, i)
            if tmp:
                return tmp

def get_last(line):
    for i in range(len(line)):
        if line[i] in "0123456789":
            last = line[i]
        else:
            tmp = spelt_number(line, i)
            if tmp:
                last = tmp
    return last

def spelt_number(line, i):
    if (i + 3 <= len(line)):
        if (line[i: i+3] in ["one", "two", "six"]):
            return word_map[line[i: i+3]]
    if (i + 4 <= len(line)):
        if (line[i: i+4] in ["four", "five", "nine"]):
            return word_map[line[i: i+4]]
    if (i + 5 <= len(line)):
        if (line[i: i+5] in ["three", "seven", "eight"]):
            return word_map[line[i: i+5]]
    return False

word_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

t0 = time.time()
f = open("input.txt")
running_sum = 0
for line in f:
    first_num = get_first(line)
    last_num = get_last(line)
    running_sum += int(first_num + last_num)
t1 = time.time()
print(running_sum)
print(t1-t0)