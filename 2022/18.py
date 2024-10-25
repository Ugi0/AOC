lines = open("input.txt","r").read().split("\n")
cubes = [[int(y) for y in x.split(",")] for x in lines]

near = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1,), (0,0,-1)]

def getOutsideCubes(): #picks a point outside the lava pool and finds surrounding cubes that can be reached.
    minNum = min(min([x[0] for x in cubes]),min([x[1] for x in cubes]),min([x[2] for x in cubes]))-1
    maxNum = max(max([x[0] for x in cubes]),max([x[1] for x in cubes]),max([x[2] for x in cubes]))+1
    start = [minNum, minNum, minNum]
    moreAdded = True
    notInsideCubes = [start]
    while moreAdded:
        moreAdded = False
        for cube in notInsideCubes:
            for move in near:
                movedTo = [cube[0]+move[0], cube[1]+move[1], cube[2]+move[2]]
                if (movedTo not in cubes and movedTo not in notInsideCubes) and (min(movedTo) >= minNum and max(movedTo) <= maxNum):
                    notInsideCubes.append(movedTo)
                    moreAdded = True
    return notInsideCubes

outsideCubes = getOutsideCubes()
count = 0
count2 = 0
for cube in cubes:
    for move in near:
        if [cube[0]+move[0], cube[1]+move[1], cube[2]+move[2]] not in cubes:
            count += 1 
            if [cube[0]+move[0], cube[1]+move[1], cube[2]+move[2]] in outsideCubes:
                count2 += 1
                
print(f"Part 1 {count}")
print(f"Part 2 {count2}")