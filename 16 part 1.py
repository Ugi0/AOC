lines = open("input.txt","r").read().split("\n")
valves = {}
paths = {0 : [["AA",0,[]]]}
steps = 26
paths.update({x: [] for x in range(1,steps+1)})
for x in lines:
    data = x.split(" ")
    name = data[1]
    rate = data[4].split("=")[1].replace(";","")
    connections = [x.replace(",","") for x in data[9:]]
    valves[name] = (int(rate), connections)

def solve(name, num, opened, i):
    for x in valves[name][1]:
        paths[i+1].append([x, num+sum([x[1] for x in opened]), opened])
    if valves[name][0] != 0 and name not in [x[0] for x in opened]:
        paths[i+1].append([name, num+sum([x[1] for x in opened]), opened+[[name, valves[name][0]]]])
for i in range(0,steps):
    for current in paths[i]:
        solve(*current, i)
    del paths[i]
    paths[i+1] = sorted(paths[i+1], key=lambda x: x[1], reverse=True)[:2000]
print(max([x[1] for x in paths[i+1]]))