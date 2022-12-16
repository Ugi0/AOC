lines = []
while True:
    a = input()
    if a == "":
        break
    else:
        lines.append(list(a))
def visible(n ,m ):
    size = len(lines)
    if n == 0 or n == size-1:
        return True
    elif m == 0 or m == size-1:
        return True
    value = int(lines[n][m])
    nums = [1,1,1,1]
    # if all([int(lines[n][i]) < value for i in range(0,m)]): #same row before
    #     return True
    # if all([int(lines[n][i]) < value for i in range(m+1,size)]): #same row before
    #     return True
    # if all([int(lines[i][m]) < value for i in range(0,n)]): #same row before
    #     return True
    # if all([int(lines[i][m]) < value for i in range(n+1,size)]): #same row before
    #     return True
    #return False
    for i in range(m-1,0, -1):
        if int(lines[n][i]) < value:
            nums[0] += 1
        else:
            break;
    for i in range(m+1,size-1):
        if int(lines[n][i]) < value:
            nums[1] += 1
        else:
            break;
    for i in range(n-1, 0, -1):
        if int(lines[i][m]) < value:
            nums[2] += 1
        else:
            break;
    for i in range(n+1, size-1):
        if int(lines[i][m]) < value:
            nums[3] += 1
        else:
            break;
    return nums[0]*nums[1]*nums[2]*nums[3]

num = 0
for i in range(len(lines)):
     for j in range(len(lines)):
         #if visible(i,j):
         n = visible(i,j)
         if num < n:
             #num += 1
             num = n

print(num)