

def reverse_string(s: list[str]) -> None:
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    print(s)



if __name__ == "__main__":
    print(reverse_string(s = ["h","e","l","l","o"]))