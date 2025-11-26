

def single_number(nums: list[int]) -> int | None:
    from collections import defaultdict
    res = defaultdict(int)
    for i in range(len(nums)):
        res[nums[i]] += 1
    for i in range(len(nums)):
        if res[nums[i]] == 1:
            return nums[i]
    return None



if __name__ == "__main__":
    # print(single_number(nums = [2,2,1]))
    print(single_number(nums = [4,1,2,1,2]))
