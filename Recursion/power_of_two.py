
def power_of_two(n: int) -> bool:
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return power_of_two(int(n / 2))





