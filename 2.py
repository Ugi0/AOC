lines = open("input.txt","r").read().split("\n")
resp = {"X": 1, "Y": 2, "Z": 3}
win = {"X": "C", "Y": "A", "Z": "B"}
loss = {"X": "B", "Y": "C", "Z": "A"}
same = {"X": "A", "Y": "B", "Z": "C"}
def findB(a, t):
    if t == "Y":
        return dict((v,k) for k,v in same.items())[a]
    if t == "Z":
        return dict((v,k) for k,v in win.items())[a]
    if t == "X":
        return dict((v,k) for k,v in loss.items())[a]
def solve(part2 = False):
    num = 0
    for x in lines:
        a = x[0]
        if part2:
            b = findB(a, x[2])
        else:
            b = x[2]
        if a == same[b]:
            num += 3
        if a == win[b]:
            num += 6
        num += resp[b]
    return num

print(f"Part 1: {solve()}")
print(f"Part 2: {solve(True)}")