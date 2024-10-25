import threading
import time
lines = open("input.txt","r").read().split("\n")
blueprints = []
for x in lines:
    s = x.split(" ")
    blueprints.append(tuple([int(x) for x in [s[1].replace(":", ""), s[6], s[12], s[18], s[21], s[27], s[30]]]))

def search(maxDays, planNum, oreRobotOreCost, clayRobotOreCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost):
    maxGeode = 0
    checked = {}
    def advanceADay(day , oreRobots, ore, clayRobot, clay, obsidianRobot, obsidian, geodeRobot, geode, path):
        nonlocal maxGeode
        nonlocal checked
        if day == maxDays:
            if geode > maxGeode:
                maxGeode = geode
            return geode
        if geode + (geodeRobot * (maxDays-day)) + (((maxDays-day)+1)*((maxDays-day))//2) <= maxGeode:
            return 0
        hashNum = hash("".join([str(x) for x in [day, oreRobots, ore, clayRobot, clay, obsidianRobot, obsidian, geodeRobot, geode]]))
        if checked.get(hashNum, -1) != -1:
            return 0
        paths = []
        if geodeRobotObsidianCost <= obsidian and geodeRobotOreCost <= ore:
            paths.append(advanceADay(day+1, oreRobots, ore - geodeRobotOreCost + oreRobots, clayRobot, clay + clayRobot, 
            obsidianRobot, obsidian - geodeRobotObsidianCost + obsidianRobot, geodeRobot+1, geode + geodeRobot, path+ ["GeodeRobot"]))
        else:
            if obsidianRobotClayCost <= clay and obsidianRobotOreCost <= ore and obsidianRobot < geodeRobotObsidianCost:
                paths.append(advanceADay(day+1, oreRobots, ore - obsidianRobotOreCost + oreRobots, clayRobot, clay - obsidianRobotClayCost + clayRobot, 
                obsidianRobot+1, obsidian + obsidianRobot, geodeRobot, geode + geodeRobot, path+ ["ObsidianRobot"]))
            if oreRobotOreCost <= ore and oreRobots < max(oreRobotOreCost, clayRobotOreCost, geodeRobotOreCost, obsidianRobotOreCost):
                paths.append(advanceADay(day+1, oreRobots+1, ore - oreRobotOreCost + oreRobots, clayRobot, clay + clayRobot, 
                obsidianRobot, obsidian + obsidianRobot, geodeRobot, geode + geodeRobot, path+ ["OreRobot"]))
            if clayRobotOreCost <= ore and clayRobot < obsidianRobotClayCost:
                paths.append(advanceADay(day+1, oreRobots, ore - clayRobotOreCost + oreRobots, clayRobot+1, clay + clayRobot, 
                obsidianRobot, obsidian + obsidianRobot, geodeRobot, geode + geodeRobot, path+ ["ClayRobot"]))
            paths.append(advanceADay(day+1, oreRobots, ore + oreRobots, clayRobot, clay + clayRobot, 
            obsidianRobot, obsidian + obsidianRobot, geodeRobot, geode + geodeRobot, path+ ["None"]))

        checked[hashNum] = max(paths)
        if day == 0:
            global count
            if maxDays == 24:
                count += planNum*max(paths)
            else:
                count *= max(paths)
        return max(paths)
    return advanceADay(0,1,0,0,0,0,0,0,0,[])

count = 0
threads = []
for i in range(0,len(blueprints)):
    thread = threading.Thread(target=search, args=(24, *blueprints[i]))
    thread.start()
    threads.append(thread)

while any([x.is_alive() for x in threads]):
    time.sleep(2)

print(f"Part 1: {count}")

count = 1
threads = []
for i in range(0,min(3, len(blueprints))):
    thread = threading.Thread(target=search, args=(32, *blueprints[i]))
    thread.start()
    threads.append(thread)

while any([x.is_alive() for x in threads]):
    time.sleep(2)

print(f"Part 2: {count}")

#Both parts completed for me in about 60 seconds, could be further optimized but it's good enough.