f = open("input.txt")
running_sum = 0
for line in f:
    for c in line:
        if c in "0123456789":
            first_digit = c
            break
    for c in reversed(line):
        if c in "0123456789":
            last_digit = c
            break
    running_sum += int(first_digit + last_digit)
print(running_sum)