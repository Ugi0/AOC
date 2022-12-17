line = open("input.txt","r").read()
rocks = [
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (-1,1), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (0,2), (1,2), (2,2)],
    [(0,0), (-1,0), (-2,0), (-3,0)],
    [(0,0), (1,0), (0,1), (1,1)]
]
def solve(steps):
    def canMove(x,y,rock):
        for z in rock:
            if y+z[1] in reserved.get(x+z[0], []) or x+z[0] < 0 or y+z[1] < 0 or y+z[1] > 6: # not already reserved && y > 0 && x between 0 and 6
                return False
        return True
    def moveByJet(move, currentPoint,rock):
        if move == "<":
            if canMove(currentPoint[0], currentPoint[1]-1, rock):
                return (currentPoint[0], currentPoint[1]-1)
            else:
                return currentPoint
        else:
            if canMove(currentPoint[0], currentPoint[1]+1, rock):
                return (currentPoint[0], currentPoint[1]+1)
            else:
                return currentPoint
    def becomeSolid(x, y, rock):
        for point in rock:
            line = reserved.get(x+point[0], [])
            reserved[x+point[0]] = line
            reserved[x+point[0]].append(y+point[1])
    rockNum = 0
    jetCount = 0
    reserved = {-1: []}
    while rockNum != steps:
        rock = rocks[rockNum % len(rocks)]
        currentPoint = (max(reserved.keys())+4-min([x[0] for x in rock]), 2)
        currentPoint = moveByJet(line[jetCount % len(line)], currentPoint ,rock)
        jetCount += 1
        while True:
            if canMove(currentPoint[0]-1, currentPoint[1], rock):
                currentPoint = (currentPoint[0]-1, currentPoint[1]) #moveDown()
                currentPoint = moveByJet(line[jetCount % len(line)], currentPoint ,rock)
                jetCount += 1
            else:
                becomeSolid(*currentPoint, rock)
                break
        rockNum += 1
        reserved = { k: reserved[k] for i, k in enumerate(sorted(reserved.keys(), reverse=True)) if i < 100}
    return (max(reserved.keys())+1,jetCount % len(line), reserved[max(reserved.keys())], rockNum % len(rocks)) #max height, jetcount index, surface roughness, current rock index
print(f"Part 1: {solve(2022)[0]}")

hashes = {}
for i in range(1,1000000):
    sol = solve(i)
    jetcount, roughness, rockIndex = [x for x in sol[1:]]
    currentHash = hash(((jetcount,tuple(roughness),rockIndex)))
    if currentHash not in hashes.keys():
        hashes[currentHash] = (sol[0], i)
    else:
        print(f"{i} and {hashes[currentHash][1]} have the same hash value with values {sol[0]} and {hashes[currentHash][0]}")
        solution = ((1000000000000 // (i - hashes[currentHash][1])) * (sol[0] - hashes[currentHash][0])) + solve((1000000000000 % (i - hashes[currentHash][1])))[0]
        print(f"Therefore, the answer for a trillion rocks would be {solution}")
        break