def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)

    return longest

nums = list(map(int, input().split()))
print(longestConsecutive(nums))