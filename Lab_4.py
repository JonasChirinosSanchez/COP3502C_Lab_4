def fibonacci(n):
    x = 0
    y = 1

    if n == 1:
        return 0
    elif n == 2:
        return 1
    for i in range(n - 2):
        x, y = y, x + y
    return y


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % 2 == 0:
            return False
    return True


def print_prime_factors(x):
    factor_x = []

    x_initial = x

    if x % 2 == 0:
        while x % 2 == 0:
            factor_x.append("* 2 ")
            y = x // 2

    if x % 3 == 0:
        while x % 3 == 0:
            factor_x.append("* 3 ")
            x = x // 3

    if x % 5 == 0:
        while x % 5 == 0:
            factor_x.append("* 5 ")
            x = x // 5

    if x % 7 == 0:
        while x % 7 == 0:
            factor_x.append("* 7 ")
            x = x // 7

    if x > 2:
        factor_x.append(f"* {x}")

    print(f"{x_initial} =", *factor_x)
