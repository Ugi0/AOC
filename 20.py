from LinkedList import DoublyLinkedList, Node

lines = [int(x) for x in open("input.txt","r").read().split("\n")]

list = DoublyLinkedList()
list2 = DoublyLinkedList()
DecryptionKey = 811589153
for x in lines:
    list.add_node(x)
    list2.add_node(x*DecryptionKey)

list.closeLoop()
list2.closeLoop()

for i in range(len(lines)): #Mixing once for part 1
    node, index = list.getOriginalIndex(i)
    list.move(index, node.value)

for x in range(10): #10 times for part2
    for i in range(len(lines)):
        node, index = list2.getOriginalIndex(i)
        list2.move(index, node.value)

num = 0
indexOf0 = list.findIndex(0)
for i in range(1,4):
    num += list.get(indexOf0+i*1000).value

num2 = 0
indexOf0 = list2.findIndex(0)
for i in range(1,4):
    num2 += list2.get(indexOf0+i*1000).value

print(f"Part 1: {num}")
print(f"Part 2: {num2}")