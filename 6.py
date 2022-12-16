line = input()
size = 14
for i in range(0, len(line)):
    if len(set(line[i:i+size])) == size:
        print(i+size)
        break
