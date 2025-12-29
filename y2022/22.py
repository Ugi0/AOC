lines = open("input.txt","r").read().split("\n")
instructions = lines[-1]
rawMap = lines[:-1]

map = {}
size = 0
for i in range(len(rawMap)-1):
    for j in range(len(rawMap[i])):
        value = rawMap[i][j]
        if value != " ":
            map[i] = map.get(i, {})
            map[i][j] = [1 if value == "." else 0][0]
            size += 1

def parseIntoIntructions(inst):
    li = []
    while len(inst) != 0:
        i = 1
        while inst[:i].isnumeric() and i <= len(inst):
            i += 1
        li.append((inst[:i-1],inst[i-1:i]))
        inst = inst[i:]
    return [x for x in li if x != ""]

def getConnected(x,y,direction): # Assumes map will be in the given shape
    sideLength = int((size // 6) ** (1/2))
    positions = [(0,1), (0,2), (1,1), (2, 0), (2, 1), (3, 0)]
    #               (starting square, direction) : (resulting square, direction)
    connections =   {(0, 3): (5, 0), (0, 2): (3, 0), 
                    (1, 3): (5, 3), (1, 0): (4, 2), (1, 1): (2, 2), 
                    (2, 0): (1, 3), (2, 2): (3, 1),
                    (3, 2): (0, 0), (3, 3): (2, 0),
                    (4, 0): (1, 2), (4, 1): (5, 2),
                    (5, 0): (4, 3), (5, 1): (1, 1), (5, 2): (0, 1)}
    start = positions.index((x//sideLength, y//sideLength))
    getLeftSize = { 0: lambda x,y: x % sideLength, 
                    1: lambda x,y: (sideLength- y-1)%sideLength,
                    2: lambda x,y: (sideLength- x-1)%sideLength,
                    3: lambda x,y: y % sideLength}
    getPosition = { 0: lambda x,y, extra: (x+extra, y),
                    1: lambda x,y, extra: (x, y+(sideLength-extra-1)),
                    2: lambda x,y, extra: (x+(sideLength-extra-1), y+(sideLength-1)),
                    3: lambda x,y, extra: (x+(sideLength-1), y+extra)}
    return getPosition[connections[(start, direction)][1]]((positions[connections[(start, direction)][0]][0]*50), (positions[connections[(start, direction)][0]][1]*50), getLeftSize[direction](x,y)), connections[(start, direction)][1]

def solve(part2 = False):
    curr = (0, min(map[0]))
    facing = 0 # 0 right, 1 down, 2 left, 3 up
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    for step in parseIntoIntructions(instructions):
        for i in range(int(step[0])):
            if facing % 2 == 0:
                keys = [x for x in map[curr[0]]]
                nextSpot = (curr[0], curr[1]+moves[facing][1])
                if part2:
                    if nextSpot[1] > max(keys) or nextSpot[1] < min(keys):
                        resp = getConnected(*curr, facing)
                        if map[resp[0][0]][resp[0][1]]:
                            nextSpot, facing = resp
                            curr = nextSpot
                        continue
                else:
                    if nextSpot[1] > max(keys):
                        nextSpot = (nextSpot[0], nextSpot[1]-len(keys))
                    if nextSpot[1] < min(keys):
                        nextSpot = (nextSpot[0], nextSpot[1]+len(keys))
                if list(map[curr[0]].values())[nextSpot[1] - min(keys)]:
                    curr = nextSpot
            else:
                keys = [x for x in map.keys() if curr[1] in map[x]]
                nextSpot = (curr[0]+moves[facing][0], curr[1])
                if part2:
                    if nextSpot[0] > max(keys) or nextSpot[0] < min(keys):
                        resp = getConnected(*curr, facing)
                        if map[resp[0][0]][resp[0][1]]:
                            nextSpot, facing = resp
                            curr = nextSpot
                        continue
                else:
                    if nextSpot[0] > max(keys):
                        nextSpot = (nextSpot[0]-len(keys), curr[1])
                    if nextSpot[0] < min(keys):
                        nextSpot = (nextSpot[0]+len(keys), curr[1])
                if [map[x][curr[1]] for x in map.keys() if curr[1] in map[x]][nextSpot[0]-min(keys)]:
                    curr = nextSpot
        if step[1] == "R":
            facing = (facing + 1) % 4
        elif step[1] == "L":
            facing = (facing - 1) % 4
    return 1000*(curr[0]+1)+4*(curr[1]+1)+facing

print(f"Part 1: {solve()}")
print(f"Part 2: {solve(True)}")