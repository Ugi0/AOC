lines = open("input.txt","r").read().split("\n")
monkeyItems = {}
rounds = 20
inspections = {}
moduloOp = 1
for i in range(0,len(lines),7):
    monkey = int(lines[i].split(" ")[1][:-1])
    monkeyItems[monkey] = [int(x.strip()) for x in lines[i+1].split(":")[1].split(",")]
    moduloOp *= int(lines[i+3].split(" ")[-1])

for time in range(0,rounds):
    for i in range(0,len(lines),7):
        monkey = int(lines[i].split(" ")[1][:-1])
        operation = lines[i+2].split(":")[1].strip()
        test = int(lines[i+3].split(" ")[-1])
        true = int(lines[i+4].split(" ")[-1])
        false = int(lines[i+5].split(" ")[-1])
        while len(monkeyItems[monkey]) != 0:
            old = monkeyItems[monkey][0]
            new = 0
            inspections[monkey] = inspections.get(monkey,0) + 1
            exec(operation)
            new = new // 3
            if new % test == 0:
                monkeyItems[true].append(new % moduloOp)
            else:
                monkeyItems[false].append(new % moduloOp)
            monkeyItems[monkey].remove(old)

save = inspections[max(inspections, key=inspections.get)]
inspections[max(inspections, key=inspections.get)] = 0
print(save*inspections[max(inspections, key=inspections.get)])