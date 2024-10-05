#part 1
with open("input5.txt") as f:
    lines = f.readlines()

# parse
seeds = lines[0].strip('\n').split(' ')[1:]
seeds = [int(item) for item in seeds]
maps = []
i = 0
for j, line in enumerate(lines):
    if line == '\n':
        if j > j - i + 1:
            maps.append(lines[j - i + 1:j])
        i = 0
    else:
        i += 1
maps.append(lines[len(lines) - i + 1:len(lines)])
for i, amap in enumerate(maps):
    for j, item in enumerate(amap):
        maps[i][j] = maps[i][j].strip('\n').split(' ')

# compute mappings
locations = []
for seed in seeds:
    for i, item in enumerate(maps):
        for amap in item:
            if int(seed) in range(int(amap[1]), int(amap[1]) + int(amap[2])):
                seed = int(amap[0]) + int(seed) - int(amap[1])
                break
    locations.append(int(seed))
print(min(locations))

#part 2
#gotta do this a lot differently

import re
with open("input5.txt") as g:
    puzzle_input = g.read()
segments = puzzle_input.split('\n\n')   # split for seeds and different mappings
intervals = []                          # this will be our todo list of intervals that need to be mapped

# use regex to find ranges of seeds
for seed in re.findall(r'(\d+) (\d+)', segments[0]):
    start, length = map(int, seed)  # convert to int
    end = start + length
    intervals.append((start,end,1)) # 1 is our segment index, since we start on the first mapping (seed-to-soil)

locations = []
# while there are things todo in our todo list
while intervals:
    start, end, segment = intervals.pop()   # first thing todo
    
    # if we've gone through all the mappings, save the smallest location for this range
    if segment == 8:
        locations.append(start)
        continue

    # use regex to find mappings in current segment
    for mapping in re.findall(r'(\d+) (\d+) (\d+)', segments[segment]):
        destination, mapping_start, mapping_length = map(int, mapping)  # convert to int
        mapping_end = mapping_start + mapping_length                    # end of our range
        mapping_diff = destination - start # used to map
        #no overlap with mapping range
        if start >= mapping_end or end <= mapping_start:
            continue
        # the start of our range does not overlap with mapping range
        if start < mapping_start:
            intervals.append((start,mapping_start,segment)) # create a new item in todo list for the range not converted (lower piece)
            start = mapping_start
        # the end of our range does not overlap with mapping range
        if end > mapping_end:
            intervals.append((mapping_end,end,segment)) # create a new item in todo list for the range not converted (upper piece)
            end = mapping_end
        # convert our range using mapping, it can go to the next segment
        intervals.append((start+mapping_diff,end+mapping_diff,segment+1))
        break
    # no conversion was necessary, move onto next segment
    else:
        intervals.append((start,end,segment+1))
print(min(locations))