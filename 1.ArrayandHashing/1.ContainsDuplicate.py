def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


nums = list(map(int, input().split()))
print(containsDuplicate(nums))
