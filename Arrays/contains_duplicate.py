from collections import defaultdict


class Solution:

    def contains_duplicate(self, nums: list[int]) -> bool:
        arr = set()
        for num in nums:
            if num in arr:
                return True
            arr.add(num)
        return False

    def contains_duplicate(self, nums: list[int]) -> bool:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            if cnt[num] == 2:
                return True
        return False