


def valid_palindrome(s: str) -> bool:
    s = "".join(x for x in s if x.isalnum()).lower()
    if not s:
        return True
    pointer_1 = 0
    pointer_2 = len(s) - 1
    while pointer_1 < pointer_2:
        if s[pointer_1] != s[pointer_2]:
            return False
        pointer_1 += 1
        pointer_2 -= 1
    return True


if __name__ == "__main__":
    print(valid_palindrome(s = "A man, a plan, a canal: Panama"))
    print(valid_palindrome(s = "race a car"))
    print(valid_palindrome(s = " "))
    print(valid_palindrome(s="aa"))