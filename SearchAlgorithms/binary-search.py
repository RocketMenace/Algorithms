

def binary_search(arr: list[int], target: int) -> int:
    arr = sorted(arr)
    start = 0
    end = len(arr)
    while start <= end:
        mid = (start + end) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            end = mid - 1
        if guess < target:
            start = mid + 1
    return -1

def binary_search_recursive(arr: list[int], target: int, start: int, end: int) -> int:
    mid: int = (start + end) // 2
    guess = arr[mid]
    if guess == target:
        return mid
    if guess > target:
        return binary_search_recursive(arr, target, start=start, end=mid - 1)
    return binary_search_recursive(arr, target, start= mid + 1, end=end)

