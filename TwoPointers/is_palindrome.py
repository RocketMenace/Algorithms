


def is_palindrome_two_pointers(x: int) -> bool:
    x = str(x)
    start, end = 0, len(x) - 1
    while start < end:
        if x[start] != x[end]:
            return False
        start += 1
        end -= 1
    return True



if __name__ == "__main__":
    print(is_palindrome_two_pointers(x = 121))
    print(is_palindrome_two_pointers(x = -121))
