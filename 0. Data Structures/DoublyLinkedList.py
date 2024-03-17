class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        cur = self.left.next
        while cur and index>0:
            cur = cur.next
            index-=1
        if cur and cur!=self.right and index==0:
            return cur.val
        return -1

    def addAtHead(self, val):
        node = Node(val)
        prev = self.left
        next = self.left.next
        node.next, node.prev = next, prev
        next.prev = prev.next = node

    def addAtTail(self, val):
        node = Node(val)
        next = self.right
        prev = self.right.prev
        node.next, node.prev = next, prev
        next.prev = prev.next = node

    def addAtIndex(self, index, val):
        cur = self.left
        while cur and index>0:
            cur= cur.next
            index-=1
        if cur and index==0:
            node = Node(val)
            prev = cur
            next = cur.next
            node.next, node.prev = next, prev
            next.prev = prev.next = node


d = DoublyLinkedList()
d.addAtTail(1)
d.addAtTail(2)
d.addAtTail(3)
d.addAtIndex(1, 4)
print(d.get(0))
print(d.get(1))
print(d.get(2))
print(d.get(3))