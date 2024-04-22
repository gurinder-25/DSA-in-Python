class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findDuplicate(nums):
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
             break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


print(findDuplicate([1, 3, 4, 2, 2]))