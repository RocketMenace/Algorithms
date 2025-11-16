

class Solution:

    def get_concatenation(self, nums: list[int]) -> list[int]:
        ans = [x  for x in nums]
        ans.extend(nums)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.get_concatenation([1,2,1]))
    print(solution.get_concatenation(nums = [1,3,2,1]))

