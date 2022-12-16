lines = open("input.txt","r").read().split("\n")
path = ['/']
dir = {}
for x in lines[1:]:
    args = x.split(" ")
    if x[0] == "$":
        if args[1] == "cd": 
            if args[2] == "..":
                path = path[:-1]
            else:
                path.append(args[2])
    else:
        dir[tuple(path+[args[1]])] = [args[0]]
#num = 0
upfordelettion = {}
def compare(path1, path2):
    for i,x in enumerate(path1):
        if path2[i] == x:
            pass
        else:
            return False
    return True
def look(path):
    size = 0
    fileshere = [x for x in dir.keys() if len(x) == len(path)+1 and compare(path,x)]
    for file in fileshere:
        if dir[file] == ['dir']:
            size += look(file)
        else:
            size += int(dir[file][0])
    global upfordelettion
    upfordelettion[size] = path
    #if size > 100000:
        #global num
        #num += size
    return size
spaceneeded = 30000000 - (70000000 - look(('/',)))
print(spaceneeded)
for x in sorted(upfordelettion.keys()):
    if x >= spaceneeded:
        print(x, upfordelettion[x])
        break
#print(num)
