
class Solution:

    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = list()
        x_pointer = 0
        y_pointer = n
        while y_pointer < len(nums):
            res.extend([nums[x_pointer], nums[y_pointer]])
            x_pointer += 1
            y_pointer += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.shuffle(nums = [2,5,1,3,4,7], n = 3))

