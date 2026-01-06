

def find_gcd(nums: list[int]) -> int:
    a_min = nums[0]
    b_max = 0
    for i in nums:
        if i >= b_max:
            b_max = i
        if i <= a_min:
            a_min = i
    while a_min != 0:
        b_max, a_min = a_min, b_max % a_min
    return b_max



if __name__ == "__main__":
    print(find_gcd(nums = [2,5,6,9,10]))
    print(find_gcd(nums = [7,5,6,8,3]))
