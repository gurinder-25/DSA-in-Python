class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.dummy = Node(0)
        self.length = 0

    def get(self, index):
        cur = self.dummy.next
        while cur and index>0:
            cur = cur.next
            index-=1
        if cur and index==0:
            return cur.val

    def addAtHead(self, val):
        cur = self.dummy.next
        self.dummy.next = Node(val)
        self.dummy.next.next = cur
        self.length+=1

    def addAtTail(self, val):
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        self.length+=1

    def addAtIndex(self, index, val):
        if index>self.length:
            return -1
        cur = self.dummy
        for _ in range(index):
            cur = cur.next
        tmp = cur.next
        cur.next = Node(val)
        cur.next.next = tmp
        self.length+=1




l = LinkedList()
l.addAtTail(1)
l.addAtTail(2)
l.addAtTail(3)
l.addAtIndex(1, 4)
print(l.get(0))
print(l.get(1))
print(l.get(2))
print(l.get(3))