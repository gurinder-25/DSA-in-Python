class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.left = self.right = None

    def enqueue(self, val):
        newNode = Node(val)
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        else:
            self.left = self.right = newNode

    def dequeue(self):
        if not self.left:
            return None
        val = self.left.val
        self.left = self.left.next
        return val




q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())