

def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    if len(nums) == 2 and nums[1] < nums[0]:
        nums[0], nums[1] = nums[1], nums[0]
        return nums
    pivot = nums[0]
    less = [i for i in nums[1:] if i <= pivot]
    greater = [i for i in nums[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def quick_sort_with_partition(nums: list[int], low: int, high: int) -> None:
    if low < high:
        pivot = partition(nums, low, high)
        quick_sort_with_partition(nums, low, pivot - 1)
        quick_sort_with_partition(nums, pivot + 1, high)

def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i + 1





if __name__ == "__main__":
    nums = [33, 10, 15, 7, 22, 19, 17]
    print(quick_sort_with_partition(nums=nums, low=0, high=len(nums) - 1))
    print(nums)