import numpy as np
lines = open("input.txt","r").read().split("\n")
#tail = [0,0]
#head = [0,0]
directions = {'R': [0,1], 'L': [0,-1], 'U': [-1,0], 'D': [1,0]}
def func(ropes):
    visited = set()
    tails = [[0,0] for x in range(ropes)]
    for x in lines:
        action = x[0]
        num = x.split(" ")[1]
        for i in range(int(num)):
            tails[0][0] += directions[action][0]
            tails[0][1] += directions[action][1]
            for i in range(1,ropes):
                dx = tails[i][0]-tails[i-1][0]
                dy = tails[i][1]-tails[i-1][1]
                if abs(dx) >= 2  or abs(dy) >= 2:
                    tails[i][0] -= np.sign(dx)
                    tails[i][1] -= np.sign(dy)
            visited.add((tails[-1][0], tails[-1][1]))
    return len(visited)
    
print(f"Part 1: {func(2)}")
print(f"Part 2: {func(10)}")