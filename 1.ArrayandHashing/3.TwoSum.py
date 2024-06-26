def twoSum(nums, target):
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return (prevMap[diff], i)
        prevMap[n] = i


nums = list(map(int, input().split()))
target = int(input())
print(twoSum(nums, target))