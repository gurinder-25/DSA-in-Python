class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        i = 1
        while i<len(nums):
            res = res ^ nums[i]
            i+=1
        return res
