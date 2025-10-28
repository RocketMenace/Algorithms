from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index

    def remove_element(self, nums: List[int], val: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer <= right_pointer:
            if nums[left_pointer] == val:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                right_pointer -= 1
            else:
                left_pointer += 1
        return left_pointer

if __name__ == "__main__":
    solution = Solution()
    print(solution.remove_element(nums = [0,1,2,2,3,0,4,2], val = 2))