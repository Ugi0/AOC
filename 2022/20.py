import copy
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node
        self.originalIndex = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.size = 0
        self.closed = False
        if values is not None:
            self.add_multiple_nodes(values)

    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        count = 0
        while count < self.size:
            yield current
            current = current.next
            count += 1
    @property
    def values(self):
        return [node.value for node in self]
    
    def findIndex(self, value):
        node = self.head
        count = 0
        while count < self.size:
            if node.value == value:
                return count
            count += 1
            node = node.next
        return None

    def get(self, index):
        node = self.head
        count = 0
        index = index % len(self)
        while count < self.size:
            if count == index:
                return node
            count += 1
            node = node.next
        return None

    def getOriginalIndex(self, index):
        node = self.head
        count = 0
        while count <= self.size:
            if node.originalIndex == index:
                return node, count
            node = node.next
            count += 1
        return None, -1

class DoublyLinkedList(LinkedList):
    def add_node(self, value):
        node = Node(value, None, self.tail)
        node.originalIndex = len(self)
        if self.head is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1
        return self

    def move(self, fro, to):
        current = self.get(fro)
        current2 = copy.copy(current)
        newNode = Node(current.value)
        newNode.originalIndex = current.originalIndex
        prev = current.prev
        next = current.next
        if to == 0:
            return
        if to > 0:
            for i in range(to % (len(self)-1)):
                current2 = current2.next
            newPrev = current2
            newNext = newPrev.next
            prev.next = next
            next.prev = prev
            newPrev.next = newNode
            newNext.prev = newNode
            newNode.next = newNext
            newNode.prev = newPrev
        else:
            for i in range(-to % (len(self)-1)):
                current2 = current2.prev
            newNext = current2
            newPrev = newNext.prev
            prev.next = next
            next.prev = prev
            newPrev.next = newNode
            newNext.prev = newNode
            newNode.next = newNext
            newNode.prev = newPrev
        if current == self.head:
            self.head = current.next
            self.tail = self.head.prev
        if current == self.tail:
            self.tail = current.prev
            self.head = self.tail.next

    def closeLoop(self):
        self.head.prev = self.tail
        self.tail.next = self.head
        self.closed = True

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
print(f"Part 2: {num2}") #Takes ~25s