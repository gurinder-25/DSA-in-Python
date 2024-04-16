class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2



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


# Print the original linked list
print("Original linked list1:")
printLinkedList(l1)


reorderList(l1)

# Print the reordered linked list
print("\nReordered linked list:")
printLinkedList(l1)

