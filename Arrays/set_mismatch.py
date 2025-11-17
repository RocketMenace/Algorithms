


class Solution:
    def find_errors_num(self, nums: list[int]) -> list[int]:
        expected_sum = int(len(nums) * (len(nums) + 1) / 2)
        errors = set()
        for i in range(len(nums)):
            if nums[i] in errors:
                missing = expected_sum - (sum(nums) - nums[i])
                return [nums[i], missing]
            errors.add(nums[i])





if __name__ == "__main__":
    solution = Solution()
    print(solution.find_errors_num(nums = [2,2]))