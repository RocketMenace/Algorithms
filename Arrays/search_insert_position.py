

class Solution:

    def searchInsert(self, nums: list[int], target: int) -> int:

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                end = mid - 1
            if guess < target:
                start = mid + 1
        return start

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert(nums = [1,3,5,6], target = 5))
    print(solution.searchInsert(nums = [1,3,5,6], target = 7))
