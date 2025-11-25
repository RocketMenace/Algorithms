

def missing_number(nums: list[int]) -> int | None:

    for i in range(len(nums) + 1):
        if i not in nums:
            return i
    return None


if __name__ == "__main__":
    print(missing_number(nums = [3,0,1]))
