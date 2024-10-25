line = open("input.txt","r").read()
def solve(part2 = False):
    if part2:
        size = 14
        for i in range(0, len(line)):
            if len(set(line[i:i+size])) == size:
                return i+size
    else:
        size = 4
        for i in range(0, len(line)):
            if len(set(line[i:i+size])) == size:
                return i+size
print(f"Part 1: {solve()}")
print(f"Part 2: {solve(True)}")