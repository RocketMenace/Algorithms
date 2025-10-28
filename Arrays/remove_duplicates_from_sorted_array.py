

class Solution(object):
    def removeDuplicates(self, nums) -> int | None:
        write_index = 1
        for i in range(1, len(nums)):
            if nums[write_index - 1] != nums[i]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index


"""
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
            w
            i
            w  i
               w  i
               w     i
               w       i
"""