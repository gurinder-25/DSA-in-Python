def sortedTwoSum(nums, target):
    l, r = 0, len(nums) - 1
    while l<=r:
        sum = nums[l] + nums[r]

        if sum>target:
            r-=1
        elif sum<target:
            l+=1
        else:
            return (nums[l],nums[r])




nums = list(map(int, input().split()))
target = int(input())
print(sortedTwoSum(nums, target))