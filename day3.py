with open("input3.txt") as f:
    lines = f.readlines()

# remove newlines
newlines = []
for line in lines:
    newlines.append(line.strip('\n'))

# build the complete number given a single digit
def build_number(newlines, i, j):
    if not newlines[i][j].isnumeric():
        return 0
    string = newlines[i][j]
    k = j - 1
    while 0 <= k and newlines[i][k].isnumeric():
        string = newlines[i][k] + string
        k -= 1
    k = j + 1
    while k < len(newlines[i]) and newlines[i][k].isnumeric():
        string = string + newlines[i][k]
        k += 1
    return int(string)

# part 1
# check all neighbours of a symbol, sum all the numbers
def check_neighbours(newlines, i, j):
    total = 0
    for k in range(i - 1, i + 2):
        skip = False
        for l in range(j - 1, j + 2):
            if skip:
                if newlines[k][l].isnumeric():
                    continue
                else:
                    skip = False
            if newlines[k][l].isnumeric():
                total += build_number(newlines, k, l)
                skip = True
    return total

# iterate through every character in every line to find symbols
total = 0
for i, line in enumerate(newlines):
    for j, char in enumerate(line):
        if not char.isnumeric() and char != '.':
            total += check_neighbours(newlines, i, j)
print(total)

# part 2
# check all neighbours of a symbol, take the product of all numbers, return only if there are 2
def check_neighbours_part_2(newlines, i, j):
    total = 1
    count = 0
    for k in range(i - 1, i + 2):
        skip = False
        for l in range(j - 1, j + 2):
            if skip:
                if newlines[k][l].isnumeric():
                    continue
                else:
                    skip = False
            if newlines[k][l].isnumeric():
                if build_number(newlines,k,l) != 0:
                    count += 1
                    total *= build_number(newlines, k, l)
                    skip = True
    if count == 2:
        return total
    return 0
total = 0
for i, line in enumerate(newlines):
    for j, char in enumerate(line):
        if not char.isnumeric() and char != '.':
            total += check_neighbours_part_2(newlines, i, j)
print(total)