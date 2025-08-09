from typing import Iterable


def binary_search(arr: list[int], target: int) -> int:
    arr = sorted(arr)
    start = 0
    end = len(arr) - 1
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
    if start > end:
        return -1
    mid: int = (start + end) // 2
    guess = arr[mid]
    if guess == target:
        return mid
    if guess > target:
        return binary_search_recursive(arr, target, start=start, end=mid - 1)
    return binary_search_recursive(arr, target, start=mid + 1, end=end)


def binary_search_first_occurrence_recursive(
    arr: list[int], target: int, start: int, end: int
) -> int:
    # Wrong solution, some upgrades required
    if start > end:
        return -1
    mid = int((start + end) / 2)
    if arr[mid] < target:
        return binary_search_first_occurrence_recursive(arr, target, mid + 1, end)
    if arr[mid] > target:
        return binary_search_first_occurrence_recursive(arr, target, start, mid - 1)
    return min(
        mid, binary_search_first_occurrence_recursive(arr, target, start, mid - 1)
    )


def binary_search_first_occurrence(arr: list[int], target: int) -> int:
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            result = mid
            end = mid - 1
        if arr[mid] > target:
            end = mid - 1
        if arr[mid] < target:
            start = mid + 1
    return result
