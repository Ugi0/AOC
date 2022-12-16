lines = open("input.txt","r").read().split("\n")
row = 20
checked = {row: []}
for x in lines:
    a,b = x.split(":")
    c = a.split(" ")[-2:] + b.split(" ")[-2:]
    d= [int(x.split("=")[1]) if "," not in x  else int(x.replace(",","").split("=")[1]) for x in c]
    start = (d[0],d[1])
    beacon = (d[2],d[3])
    distance = abs(start[0]-beacon[0]) + abs(start[1]-beacon[1])
    print(start, beacon, distance)
    if abs(start[1] - row) <= distance:
        amount = distance - abs(start[1]-row)
        checked[row].append((start[0]-amount, start[0]+amount))
checked[row].sort()
num = 0
li = []
for x in checked[row]:
    li.append((x[0], "A"))
    li.append((x[1], "B"))
li.sort()
last = li[0][0]
count = 1
for x in li[1:]:
    if count != 0:
        num += x[0]-last
    else:
        num += 1
    if x[1] == "A":
        count += 1
    else:
        count -= 1
    last = x[0]
print(num)

#4483797 too low
#5278544 too high
#5031813 not correct
#5024154 not correct
#4724228 correct!