lines = open("input.txt","r").read().split("\n")
most = [0,0,0]
num = 0
for x in lines:
    if x == "":
        if num > most[0]:
            most[2] = most[1]
            most[1] = most[0]
            most[0] = num
        elif num > most[1]:
            most[2] = most[1]
            most[1] = num
        elif num > most[2]:
            most[2] = num
        num = 0
    else:
        num += int(x)
print(f"Part 1: {most[0]}")
print(f"Part 2: {sum(most)}")
