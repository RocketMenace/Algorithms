


def move_zeroes(nums: list[int]) -> None:
    pointer = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[pointer] = nums[pointer], nums[i]
            pointer += 1

if __name__ == "__main__":
    print(move_zeroes(nums = [0,1,0,3,12]))
    print(move_zeroes(nums=[1,0,1]))
    print(move_zeroes(nums=[0,0,1,0,-1]))

