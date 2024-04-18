class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]

# Test Case
if __name__ == "__main__":
    # Creating nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # Assigning random pointers
    node1.random = node3
    node2.random = node1
    node3.random = node2

    # Assigning next pointers
    node1.next = node2
    node2.next = node3

    # Copying the linked list
    solution = Solution()
    copied_list = solution.copyRandomList(node1)

    # Checking if random pointers are correctly copied
    assert copied_list.random.val == node3.val
    assert copied_list.next.random.val == node1.val
    assert copied_list.next.next.random.val == node2.val

    print("Test passed.")
