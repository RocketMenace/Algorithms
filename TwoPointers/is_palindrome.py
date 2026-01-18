


def is_palindrome_two_pointers(x: int) -> bool:
    x = str(x)
    start, end = 0, len(x) - 1
    while start < end:
        if x[start] != x[end]:
            return False
        start += 1
        end -= 1
    return True

def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    temp = x
    r = 0
    while temp > 0:
        last_digit = temp % 10
        r = r * 10 + last_digit
        temp //= 10
    if r == x:
        return True
    return False



if __name__ == "__main__":
    print(is_palindrome(x = 121))
    print(is_palindrome(x = -121))
