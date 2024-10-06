#part 1
with open("input6.txt") as f:
    lines = f.readlines()
lines = [list(map(int,list(filter(None, line.strip().split(' ')[1:])))) for line in lines]

# find the minimum amount of hold by starting from 0, then find the maximum amount of hold by starting from using all the time
def find_range(time, distance):
    hold_time = 0
    while hold_time * (time - hold_time) < distance:
        hold_time += 1
    min = hold_time
    hold_time = time
    while hold_time * (time - hold_time) < distance:
        hold_time -= 1
    return hold_time - min + 1

total = 1
for i, time in enumerate(lines[0]):
    total *= find_range(time, lines[1][i])
print(total)

#part 2
with open("input6.txt") as f:
    lines = f.readlines()
lines = [line.strip().replace(" ","") for line in lines]
time = int(lines[0].split(":")[1])
distance = int(lines[1].split(":")[1])
print(find_range(time, distance))