class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    dummy = Node(0, head)
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print()

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next = Node(4)
l1.next.next.next.next = Node(5)

print("Original linked list1:")
printLinkedList(l1)


result = reverseKGroup(l1, 2)
printLinkedList(result)