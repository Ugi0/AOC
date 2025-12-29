lines = [list(x) for x in open("input.txt","r").read().split("\n")]
count = 0
value = {"1": 1, "2": 2, "0": 0, "-": -1, "=": -2}
toSnafu = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}

for x in lines:
    pos = 0
    for number in x[::-1]:
        count += value[number]*(5**pos)
        pos += 1

def convertToSNAFU(num):
    ans = ""
    while num > 0:
        remainder = num % 5
        num = num // 5
        ans += toSnafu[remainder]
        if remainder > 2:
            num += 1
    if len(ans) == 0:
        return "0"
    return ans[::-1]

print(f"Part 1: {convertToSNAFU(count)}")
