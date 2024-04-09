def search(nums, target):
    start = 0
    end = len(nums) - 1
    mid = 0

    while start <= end:

        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid

    return -1


nums = list(map(int, input().split()))
target = int(input())
print(search(nums, target))
