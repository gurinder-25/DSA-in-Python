class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print()

# Define the linked list
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)

# Print the original linked list
print("Original linked list:")
printLinkedList(l)

# Reverse the linked list
reversed_list = reverseList(l)

# Print the reversed linked list
print("\nReversed linked list:")
printLinkedList(reversed_list)

