class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    cur = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry
        carry = val//10
        val = val%10
        cur.next = ListNode(val)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

def printLinkedList(head):
    if head is None:
        return
    printLinkedList(head.next)
    print(head.val, end="")


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print("First List")
printLinkedList(l1)
print()

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print("Second List")
printLinkedList(l2)
print()

res = addTwoNumbers(l1, l2)
print("After Addition")
printLinkedList(res)