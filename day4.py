with open("input4.txt") as f:
    lines = f.readlines()

# parse
newlines = []
for line in lines:
    newlines.append(line[:-1].split(":")[1:][0].split("|"))
cards = {}
for line in newlines:
    cards[tuple(filter(None, line[0].split(' ')))] = tuple(filter(None, line[1].split(' ')))

# part 1
total = 0
for x, y in cards.items():
    current = 0
    for i in x:
        if i in y:
            if current == 0:
                current += 1
            else:
                current *= 2
    total += current
print(total)

#part 2
import numpy as np
copies = np.ones(len(cards))
for j, (x, y) in enumerate(cards.items()):
    current = 1
    for i in x:
        if i in y:
            if j + current < len(copies):
                copies[j + current] += copies[j]
            current += 1
print(sum(copies))