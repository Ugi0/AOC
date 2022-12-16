lines = open("input.txt","r").read().split("\n")
counter = 1
num = 0
i = 0
def draw(index):
    ind = index%40
    if abs(counter-ind) <= 1:
        print('#', end ="")
    else:
        print('.', end ="")
    if ((index+1)%40) == 0:
        print()
for x in lines:
    line = x.split(" ")
    if line[0] == "noop":
        draw(i)
        i += 1
    if line[0] == "addx":
        draw(i)
        i += 1
        if (i % 40) == 20:
             num += i*counter
        draw(i)
        i += 1
        if (i % 40) == 20:
             num += i*counter
        counter += int(line[1])
    elif (i % 40) == 20:
        num += i*counter
print()
print(num)
