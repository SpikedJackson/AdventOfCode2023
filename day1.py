# part 1
with open("input1.txt") as f:
    lines = f.readlines()
total = 0
for line in lines:
    line=list(line)
    num = []
    for i in line:
        if i.isnumeric():
            num.append(i)
    num2 = int(''.join([num[0],num[-1]]))
    total += num2
print(total)

#part 2
numbers = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
with open("input1.txt") as f:
    lines = f.readlines()
total = 0
for line in lines:
    num = []
    for i in range(0,len(line)):
        if line[i].isnumeric():
            num.append(line[i])
        else:
            for key,value in numbers.items():
                if line[i:].find(key) == 0:
                    num.append(value)
    num2 = int(''.join([str(num[0]),str(num[-1])]))
    total += num2
print(total)