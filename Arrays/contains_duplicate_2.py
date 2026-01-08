"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j]
and abs(i - j) <= k.

"""

def contains_duplicate(nums: list[int], k: int) -> bool:
    cnt = dict()
    for i in range(len(nums)):
        if nums[i] in cnt.keys() and abs(cnt.get(nums[i]) - i) <= k:
            return True
        cnt[nums[i]] = i
    return False



if __name__ == "__main__":
    print(contains_duplicate(nums = [1,2,3,1], k = 3))
    print(contains_duplicate(nums = [1,2,3,1,2,3], k = 2))
    print(contains_duplicate(nums = [1,0,1,1], k = 1))
