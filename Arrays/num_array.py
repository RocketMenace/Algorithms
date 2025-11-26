

class NumArraY:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left: right + 1])



if __name__ == "__main__":

    arr = NumArraY(nums=[-2, 0, 3, -5, 2, -1])
    print(arr.sum_range(0, 2))
    print(arr.sum_range(2, 5))
    print(arr.sum_range(0, 5))