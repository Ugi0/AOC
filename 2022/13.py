import functools
lines = open("input.txt","r").read().split("\n")

def compare(a,b):
    global count
    if isinstance(a,list) and len(a) == 0:
        return 1
    if isinstance(b,list) and len(b) == 0:
        return -1
    if isinstance(a,int) and isinstance(b,int):
        if a < b:
            return 1
        elif a == b:
            return
        else:
            return -1
    if isinstance(a,list) and isinstance(b,int):
        b = [b]
    if isinstance(a,int) and isinstance(b,list):
        a = [a]
    if isinstance(a,list) and isinstance(b,list):
        for i in range(max(len(a), len(b))):
            if i == len(a):
                return 1
            elif i == len(b):
                return -1
            res = compare(a[i],b[i])
            if res != None:
                if res == 1:
                    return 1
                else:
                    return -1

count = 0
for j,i in enumerate(range(0,len(lines),3)):
    first = eval(lines[i])
    second = eval(lines[i+1])
    if compare(first, second) == 1:
        count += j+1
print(f"Part 1: {count}")
count = 0
lines = [eval(x) for x in lines if x != '']
lines.append([[2]])
lines.append([[6]])
lines.sort(key=functools.cmp_to_key(compare), reverse=True)
print(f"Part 2: {(lines.index([[2]])+1) * (lines.index([[6]])+1)}")