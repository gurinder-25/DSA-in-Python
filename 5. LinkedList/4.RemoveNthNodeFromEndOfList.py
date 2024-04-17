class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next



def printLinkedList(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print()

# Define the linked list
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

n = 2

# Print the original linked list
print("Original linked list1:")
printLinkedList(l1)

l = removeNthFromEnd(l1, n)


# Print the reordered linked list
print("\nReordered linked list:")
printLinkedList(l)

