from collections import defaultdict


def majority_element(nums: list[int]) -> int | None:
    majority = len(nums) / 2
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1
    for k,v in counter.items():
        if v >= majority:
            return k
    return None



if __name__ == "__main__":
    print(majority_element(nums = [2,2,1,1,1,2,2]))