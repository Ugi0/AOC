lines = open("input.txt","r").read().split("\n")

monkeys = {}

for x in lines:
    monkey = x.split(" ")[0][:-1]
    operation = x.split(" ")[1:]
    monkeys[monkey] = operation

def rec(monkey, part2 = False):
    if monkeys[monkey][0].isnumeric() or monkeys[monkey][0][1:].isnumeric():
        return int(monkeys[monkey][0])
    else:
        if monkey == "root" and part2:
            return rec(monkeys[monkey][0]), rec(monkeys[monkey][2])
            return eval(f"{rec(monkeys[monkey][0])} == {rec(monkeys[monkey][2])}")
        return eval(f"{rec(monkeys[monkey][0])} {monkeys[monkey][1]} {rec(monkeys[monkey][2])}")
        
print(f"Part 1: {int(rec('root'))}")

minNum = 0
maxNum = 10**15

while minNum < maxNum: #Find part 2 by testing different values of humn and closing in on the right answer using binary search
    middle = (minNum+maxNum) // 2
    monkeys["humn"] = [str(middle)]
    result = rec("root", True)
    if result[0] > result[1]:
        minNum = middle+1
    else:
        maxNum = middle
print(f"Part 2: {minNum}")