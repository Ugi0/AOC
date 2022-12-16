lines = open("input.txt","r").read().split("\n")
num = 0
for x in lines:
    a1, a2 = [int(z) for z in x.split(",")[0].split("-")]
    b1, b2 = [int(z) for z in x.split(",")[1].split("-")]
#    if a1 >= b1 and a2 <= b2:
 #       num += 1
  #  elif a1 <= b1 and a2 >= b2:
   #     num += 1

    if a1 <= b1 <= a2 or b1 <= a1 <= b2:
        num += 1
print(num)
