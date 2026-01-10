
def intersection(nums_1: list[int], nums_2: list[int]) -> list[int]:
    seen = set(nums_1)
    res = set()
    for i in nums_2:
        if i in seen and i not in res:
            res.add(i)
    return list(res)

if __name__ == "__main__":
    print(intersection(nums_1 = [4,9,5], nums_2 = [9,4,9,8,4]))

