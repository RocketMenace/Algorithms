

def fibonacci_recursive(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b



if __name__ == "__main__":
    print(fibonacci_recursive(8))
    print(fibonacci_iterative(8))
