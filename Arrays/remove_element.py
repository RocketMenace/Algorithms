class Solution(object):
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write_index = 1
        for i in range(len(nums)):
            if nums[write_index - 1] == val:
                nums[write_index] = nums[i]
        return write_index




if __name__ == "__main__":

    solution = Solution()
    print(solution.removeElement(nums = [3,2,2,3], val = 3))