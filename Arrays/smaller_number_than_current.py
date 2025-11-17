

class Solution:

    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        nums_sorted = sorted(nums)
        pairs = dict()
        for i in range(len(nums)):
            if nums_sorted[i] not in pairs:
                pairs[nums_sorted[i]] = i
        return [pairs[x] for x in nums]




if __name__ == "__main__":
    solution = Solution()
    print(solution.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
