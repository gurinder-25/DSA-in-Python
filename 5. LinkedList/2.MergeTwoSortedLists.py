class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val<list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2
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
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# Print the original linked list
print("Original linked list1:")
printLinkedList(l1)
print("Original linked list2:")
printLinkedList(l2)

# Reverse the linked list
reversed_list = mergeTwoLists(l1, l2)

# Print the reversed linked list
print("\nReversed linked list:")
printLinkedList(reversed_list)

