


class Solution:

    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        arr = set(range(1, len(nums) + 1))
        nums = set(nums)
        return list(arr.difference(nums))



if __name__ == "__main__":

    solution = Solution()
    print(solution.find_disappeared_numbers(nums = [4,3,2,7,8,2,3,1]))