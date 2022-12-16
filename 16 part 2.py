lines = open("input.txt","r").read().split("\n")
valves = {}
paths = {0 : [["AA","AA",0,[]]]}
steps = 26
paths.update({x: [] for x in range(1,steps+1)})
for x in lines:
    data = x.split(" ")
    name = data[1]
    rate = data[4].split("=")[1].replace(";","")
    connections = [x.replace(",","") for x in data[9:]]
    valves[name] = (int(rate), connections)

def solve(name, name2, num, opened, i):
    for y in valves[name2][1]:
        for x in valves[name][1]:
            paths[i+1].append([x, y, num+sum([x[1] for x in opened]), opened])
            if valves[name][0] != 0 and name not in [x[0] for x in opened]:
                paths[i+1].append([name, y, num+sum([x[1] for x in opened]), opened+[[name, valves[name][0]]]])
            if valves[name2][0] != 0 and name2 not in [x[0] for x in opened] and name != name2:
                paths[i+1].append([x, name2, num+sum([x[1] for x in opened]), opened+[[name2, valves[name2][0]]]])
            if (valves[name][0] != 0 and name not in [x[0] for x in opened]) and (valves[name2][0] != 0 and name2 not in [x[0] for x in opened]) and name != name2:
                paths[i+1].append([name, name2, num+sum([x[1] for x in opened]), opened+[[name2, valves[name2][0]]]+[[name, valves[name][0]]]])

for i in range(0,steps):
    for current in paths[i]:
        solve(*current, i)
    del paths[i]
    paths[i+1] = sorted(paths[i+1], key=lambda x: x[2], reverse=True)[:50000]
print(max([x[2] for x in paths[i+1]]))