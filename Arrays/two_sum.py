


class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pairs = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in pairs:
                return [pairs[complement], i]
            pairs[nums[i]] = i
            




if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums = [2,7,11,15], target = 9))
    print(solution.twoSum(nums = [3,2,4], target = 6))