lines = open("input.txt","r").read().split("\n")
def solve(part2 = False):
    if part2:
        maxNum = 4000000
        found = False
        for row in range(0,maxNum+1):
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
                        return (x[0]-1)*4000000+row
                    num += 1
                if x[1] == "A":
                    count += 1
                else:
                    count -= 1
                last = x[0]
    else:
        row = 2000000
        checked = {row: []}
        for x in lines:
            a,b = x.split(":")
            c = a.split(" ")[-2:] + b.split(" ")[-2:]
            d= [int(x.split("=")[1]) if "," not in x  else int(x.replace(",","").split("=")[1]) for x in c]
            start = (d[0],d[1])
            beacon = (d[2],d[3])
            distance = abs(start[0]-beacon[0]) + abs(start[1]-beacon[1])
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
        return num

print(f"Part 1: {solve()}")
print(f"Part 2: {solve(True)}") #Brute for solution took me ~3 minutes