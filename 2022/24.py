import queue
import copy
lines = [list(x) for x in open("input.txt","r").read().split("\n")]
blizzards = []
for i,x in enumerate(lines):
    for j, y in enumerate(x):
        if i == 0 and y != "#":
            start = (i,j)
        if i == len(lines)-1 and y != "#":
            end = (i,j)
        elif y == ">":
            blizzards.append([i,j,0])
        elif y == "v":
            blizzards.append([i,j,1])
        elif y == "<":
            blizzards.append([i,j,2])
        elif y == "^":
            blizzards.append([i,j,3])
height, width = len(lines), len(lines[0])
moves = [(0,1), (1,0), (0,-1), (-1,0)]
def check(x,y):
    if x >= height:
        return False
    if lines[x][y] == "#":
        return False
    else:
        return True
def moveBlizzards():
    for x in copy.copy(blizzards):
        blizzards.remove(x)
        newx, newy = x[0]+moves[x[2]][0], x[1]+moves[x[2]][1]
        if newx == height-1:
            newx = 1
        if newx == 0:
            newx = height-2
        if newy == width-1:
            newy = 1
        if newy == 0:
            newy = width-2
        blizzards.append([newx, newy, x[2]])
    return blizzards
def solve(part2 = False):
    Queue = queue.PriorityQueue()
    if part2:
        Queue.put([0, end])
    else:
        Queue.put([0, start])
    last = -1
    while not Queue.empty():
        spot = Queue.get()
        if spot[0] != last:
            moveBlizzards()
            last = spot[0]
        for x in moves:
            if (not any([[spot[1][0]+x[0], spot[1][1]+x[1], u] in blizzards for u in range(4)])) and check(spot[1][0]+x[0], spot[1][1]+x[1]):
                if not part2:
                    if (spot[1][0]+x[0], spot[1][1]+x[1]) == end:
                        return spot[0]+1
                else:
                    if (spot[1][0]+x[0], spot[1][1]+x[1]) == start:
                        return spot[0]+1
                if [spot[0]+1, (spot[1][0]+x[0], spot[1][1]+x[1])] not in Queue.queue:
                    Queue.put([spot[0]+1, (spot[1][0]+x[0], spot[1][1]+x[1])])
        if [spot[0]+1, (spot[1][0], spot[1][1])] not in Queue.queue and not any([[spot[1][0], spot[1][1], u] in blizzards for u in range(4)]):
            Queue.put([spot[0]+1, (spot[1][0], spot[1][1])])
ans = solve()
print(f"Part 1: {ans}")
ans2 = solve(True)
print(f"Part 2: {ans+ans2+solve()}")
#Quite a slow code, taking ~230s for both parts.
#But it works so gefm