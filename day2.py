# part 1
# with open("input2.txt") as f:
#     lines = f.readlines()
# total = 0
# dict = {"red":12,"green":13,"blue":14}
# for line in lines:
#     check = True
#     id = ((line.split(":"))[0].split(" "))[1]
#     line = (line.replace('\n','')).replace(' ','')
#     line = (line.split(":"))[1].split(";")
#     for round in line:
#         round = round.split(',')
#         for colour in round:    
#             for key,value in dict.items():
#                 if colour.find(key) != -1:
#                     if int(colour[:colour.find(key)]) > value:
#                         check = False
#     if check:
#         total += int(id)
# print(total)
# part 2
with open("input2.txt") as f:
    lines = f.readlines()
total = 0
for line in lines:
    dict = {"red":0,"green":0,"blue":0}
    id = ((line.split(":"))[0].split(" "))[1]
    line = (line.replace('\n','')).replace(' ','')
    line = (line.split(":"))[1].split(";")
    for round in line:
        round = round.split(',')
        for colour in round:    
            for key,value in dict.items():
                if colour.find(key) != -1:
                    if int(colour[:colour.find(key)]) > value:
                        dict[key] = int(colour[:colour.find(key)])
    total += dict["red"]*dict["green"]*dict["blue"]
print(total)