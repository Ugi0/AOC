lines = open("input.txt","r").read().split("\n")
def solve(part2 = False):
    if part2:
        rounds = 10000
    else:
        rounds = 20
    monkeyItems = {}
    inspections = {}
    moduloOp = 1
    for i in range(0,len(lines),7):
        monkey = int(lines[i].split(" ")[1][:-1])
        monkeyItems[monkey] = [int(x.strip()) for x in lines[i+1].split(":")[1].split(",")]
        moduloOp *= int(lines[i+3].split(" ")[-1])
    for _ in range(rounds):
        for i in range(0,len(lines),7):
            monkey = int(lines[i].split(" ")[1][:-1])
            operation = lines[i+2].split(":")[1].strip()
            test = int(lines[i+3].split(" ")[-1])
            true = int(lines[i+4].split(" ")[-1])
            false = int(lines[i+5].split(" ")[-1])
            while len(monkeyItems[monkey]) != 0:
                old = monkeyItems[monkey][0]
                inspections[monkey] = inspections.get(monkey,0) + 1
                new = eval(operation.split("=")[1])
                if not part2:
                    new = new // 3
                    value = new
                else:
                    value = new % moduloOp
                if new % test == 0:
                    monkeyItems[true].append(value)
                else:
                    monkeyItems[false].append(value)
                monkeyItems[monkey].remove(old)
    values = sorted(inspections.values())
    return values[-1]*values[-2]

print(f"Part 1: {solve()}")
print(f"Part 2: {solve(True)}")