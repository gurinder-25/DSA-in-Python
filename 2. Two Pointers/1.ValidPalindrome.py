def isPalindrome(nums):
    res = "".join([i for i in nums if i.isalnum()]).lower()
    l, r =0, len(res) - 1
    while l<=r:
        if res[l]!=res[r]:
            return False
        l+=1
        r-=1

    return True




nums = input()
print(isPalindrome(nums))