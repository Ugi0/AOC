lines = open("input.txt","r").read().split("\n")

moves = ("N", "S", "W", "E")
moveDiff = {"N": (-1, 0), "S": (1, 0),
            "W": (0, -1), "E": (0, 1)}
allAdjacent = ((-1, -1), (-1, 0), (-1, 1), (0, -1),  (1, 0), (1, 1), (0, 1), (1, -1))
checks = {  "N": ((-1, -1), (-1, 0), (-1, 1)),
            "S": ((1,-1), (1, 0), (1, 1)),
            "W": ((-1, -1), (0, -1), (1, -1)),
            "E": ((-1, 1), (0, 1), (1, 1))}


def solve(part2 = False):
    if not part2:
        rounds = 10
    else:
        rounds = 1000
    elves = set()
    for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == "#":
                    elves.add((i,j))
    for round in range(rounds):
        considerations = set()
        counts = {}
        for elf in elves:
            if any([(elf[0]+delta[0], elf[1]+delta[1]) in elves for delta in allAdjacent]):
                directions = moves[(round%len(moves)):]+moves[:(round%len(moves))] 
                for direction in directions:
                    if all([(elf[0]+delta[0], elf[1]+delta[1]) not in elves for delta in checks[direction]]):
                        considerations.add((elf, (elf[0]+moveDiff[direction][0], elf[1]+moveDiff[direction][1])))
                        counts[(elf[0]+moveDiff[direction][0], elf[1]+moveDiff[direction][1])] = counts.get((elf[0]+moveDiff[direction][0], elf[1]+moveDiff[direction][1]), 0) +1
                        break
        moved = False
        for x in considerations:
            if counts[x[1]] == 1:
                moved = True
                elves.remove(x[0])
                elves.add(x[1])
        if not moved:
            return round+1
    return (max([x[0] for x in elves])-min([x[0] for x in elves])+1)*(max([x[1] for x in elves])-min([x[1] for x in elves])+1) - len(elves)
print(f"Part 1: {solve()}")
print(f"Part 2: {solve(True)}") 