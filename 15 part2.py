lines = open("input.txt","r").read().split("\n")
maxNum = 4000000
lastRow = 1
found = False
for row in range(0,maxNum+1):
    if found:
        break
    checked = []
    for x in lines:
        a,b = x.split(":")
        c = a.split(" ")[-2:] + b.split(" ")[-2:]
        d= [int(x.split("=")[1]) if "," not in x  else int(x.replace(",","").split("=")[1]) for x in c]
        start = (d[0],d[1])
        beacon = (d[2],d[3])
        distance = abs(start[0]-beacon[0]) + abs(start[1]-beacon[1])
        if abs(start[1] - row) <= distance:
            amount = distance - abs(start[1]-row)
            checked.append((min(maxNum,max(start[0]-amount,0)), min(maxNum,max(start[0]+amount,0))))
    checked.sort()
    num = 0
    li = []
    for x in checked:
        li.append((x[0], "A"))
        li.append((x[1], "B"))
    li.sort()
    last = li[0][0]
    count = 1
    for x in li[1:]:
        if count != 0:
            num += x[0]-last
        else:
            if x[0]-1 != last:
                print("found", (x[0]-1, row), (x[0]-1)*4000000+row)
                found = True
            num += 1
        if x[1] == "A":
            count += 1
        else:
            count -= 1
        last = x[0]