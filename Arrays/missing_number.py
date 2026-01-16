

def missing_number(nums: list[int]) -> int | None:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    print(missing_number(nums = [3,0,1]))
