

def single_number(nums: list[int]) -> int | None:
    for i in range(len(nums)):
        if nums[i] not in nums[i + 1:] and nums[i] not in nums[:i]:
            return nums[i]
    return None



if __name__ == "__main__":
    print(single_number(nums = [2,2,1]))
    print(single_number(nums = [4,1,2,1,2]))
