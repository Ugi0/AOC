lines = open("input.txt","r").read().split("\n")
def getCode(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-65+27
def solve(part2 = False):
    num = 0
    count = 0
    if part2:
        while True:
            q = [[],[],[]]
            li = lines[count:count+3]
            for x,y in [[0,1],[1,2],[0,2]]:
                a = li[x]
                b = li[y]
                for char in a:
                    if char in b:
                        q[x+y-1].append(getCode(char))
            common = set(q[0]) & set(q[1]) & set(q[2])
            num += common.pop()
            count += 3
            if count >= len(lines):
                break
        return num
    else:
        for x in lines:
            size = len(x)
            a = x[:size//2]
            b = x[size//2:]
            for char in a:
                if char in b:
                    num += getCode(char)
                    break
        return num
print(f"Part 1: {solve()}")
print(f"Part 2: {solve(True)}")