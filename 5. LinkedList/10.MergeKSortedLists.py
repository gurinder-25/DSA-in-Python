class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        lists = mergedLists
    return lists[0]

def mergeList(l1, l2):
    dummy = Node()  # Creating a dummy node without a value
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next

l1 = Node(1)
l1.next = Node(4)
l1.next.next = Node(5)

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(4)

l3 = Node(2)
l3.next = Node(6)

merged = mergeKLists([l1, l2, l3])
node = merged

output = []
while node:
    output.append(node.val)
    node = node.next

print(output)
