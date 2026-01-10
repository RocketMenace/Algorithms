from collections import defaultdict


def intersection(nums_1: list[int], nums_2: list[int]) -> list[int]:
    counter = defaultdict(int)
    res = list()
    for i in nums_1:
        counter[i] += 1
    for i in nums_2:
        if i in counter and counter[i] > 0:
            res.append(i)
            counter[i] -= 1
    return res

if __name__ == "__main__":
    print(intersection(nums_1 = [4,9,5], nums_2 = [9,4,9,8,4]))
    print(intersection([1,2,2,1], [2]))