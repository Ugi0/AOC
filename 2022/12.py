import queue
def solve(part2 = False):
    grid = []
    Queue = queue.PriorityQueue()
    visited = []
    ans = 0
    for i,x in enumerate(open("input.txt","r").read().split("\n")):
        for j,s in enumerate(x):
            if s == 'E':
                end = (i,j)
            if s == 'S':
                start = (i,j)
            if part2:
                if s == 'a':
                    Queue.put((0,(i,j)))
        grid.append(list(x))

    if not part2:
        Queue.put((0,(start[0],start[1])))

    def inGrid(x,y):
        if x == -1 or x == len(grid):
            return False
        if y == -1 or y == len(grid[0]):
            return False
        return True

    def search(x,y, count):
        nonlocal Queue
        if (x,y) == start:
            current = 'a'
        else:
            current = grid[x][y]
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        for step in steps:
            nx,ny = x+step[0],y+step[1]
            if inGrid(nx,ny):
                if ord(grid[nx][ny])-ord(current) <= 1 and (nx,ny) not in visited:
                    if (nx,ny) == end and current != 'z':
                        pass
                    else:
                        Queue.put((count+1,(nx,ny)))
                        visited.append((nx,ny))
                        if grid[nx][ny] == 'E':
                            nonlocal ans
                            ans = count+1

    while not Queue.empty():
        values = Queue.get()
        search(values[1][0],values[1][1],values[0])
    return ans

print(f"Part 1: {solve()}")
print(f"Part 2: {solve(True)}")