lines = open("input.txt","r").read().split("\n")
def solve(part2 = False):
    li = [['L', 'N', 'W', 'T', 'D'], ['C', 'P', 'H'],
      ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J'],
      ['C', 'W', 'S', 'N', 'T', 'Q', 'L'], ['P', 'H', 'C', 'N'],
      ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B'],
      ['M', 'B', 'R', 'J', 'G', 'S', 'L'],
      ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T'],
      ['W', 'G', 'D', 'N', 'P', 'L']]
    for x in lines:
        amount = int(x.split(" ")[1])
        start = int(x.split(" ")[3])-1
        end = int(x.split(" ")[5])-1
        movedcrates = []
        for r in range(amount):
            if part2:
                movedcrates.append(li[start].pop())
            else:
                li[end].append(li[start].pop())
        for q in movedcrates[::-1]:
            li[end].append(q)
    return li

print(f"Part 1: {''.join([x[-1] for x in solve()])}")
print(f"Part 2: {''.join([x[-1] for x in solve(True)])}")