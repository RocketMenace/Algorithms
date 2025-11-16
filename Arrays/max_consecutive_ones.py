

class Solution(object):
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        prev = 0
        for num in nums:
            if num == 1:
                current += 1
            if current > prev:
                prev = current
            if num == 0:
                current = 0
        return prev


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))