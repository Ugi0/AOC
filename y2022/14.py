from collections import defaultdict
import itertools
lines = open("input.txt","r").read().split("\n")
def solve(part2 = False):
    blocked = defaultdict(lambda: [])
    for x in lines:
        for i in range(len(x.split("->"))-1):
            a = x.split("->")[i].strip()
            b = x.split("->")[i+1].strip()
            a1,a2 = [int(x) for x in a.split(",")]
            b1,b2 = [int(x) for x in b.split(",")]
            if a1 == b1:
                for j in range(min(a2,b2),max(a2,b2)+1):
                    if j not in blocked[a1]:
                        blocked[a1].append(j)
            else:
                for j in range(min(a1,b1),max(a1,b1)+1):
                    if a2 not in blocked[j]:
                        blocked[j].append(a2)
    lowestPoint = max([x for x in itertools.chain(blocked.values())])[0]
    if part2:
        for j in range(0,1000):
            blocked[j].append(lowestPoint+2)
        lowestPoint += 3
    start = (500,0)
    count = 0
    def moveSnow(x,y):
        nonlocal blocked
        if y >= lowestPoint:
            return 'off'
        if y+1 not in blocked[x]:
            return moveSnow(x,y+1)
        elif y+1 not in blocked[x-1]:
            return moveSnow(x-1,y+1)
        elif y+1 not in blocked[x+1]:
            return moveSnow(x+1,y+1)
        else:
            if (x,y) == start and start[1] in blocked[start[0]]:
                return 'off'
            blocked[x].append(y)
            return True
    def dropSnow():
        nonlocal count
        while True:
            res = moveSnow(start[0],start[1])
            if res == 'off':
                return False
            elif res:
                count += 1
                break
        return True
    while dropSnow():
        pass
    return count
print(f"Part 1: {solve()}")
print(f"Part 2: {solve(True)}")