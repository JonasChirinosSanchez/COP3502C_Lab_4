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

    prime_factor = False

    if x == 2:
        print(f"{x_initial} =", 2)
        prime_factor = True
    elif x == 3:
        print(f"{x_initial} =", 3)
        prime_factor = True
    elif x == 5:
        print(f"{x_initial} =", 5)
        prime_factor = True
    elif x == 7:
        print(f"{x_initial} =", 7)
        prime_factor = True

    #Becomes true once on of the prime factors become the initial value
    pass_two = False
    pass_three = False
    pass_five = False
    pass_seven = False

    if prime_factor == False:
        if x % 2 == 0:
            factor_x.append(" 2 ")
            x = x // 2
            pass_two = True
            while x % 2 == 0:
                factor_x.append("* 2 ")
                x = x // 2

        if x % 3 == 0:
            if pass_two == False:
                factor_x.append(" 3 ")
                x = x // 3
                pass_three = True
            while x % 3 == 0:
                factor_x.append("* 3 ")
                x = x // 3

        if x % 5 == 0:
            if pass_two == False:
                if pass_three == False:
                    factor_x.append(" 5 ")
                    x = x // 5
                    pass_five = True
            while x % 5 == 0:
                factor_x.append("* 5 ")
                x = x // 5

        if x % 7 == 0:
            if pass_two == False:
                if pass_three == False:
                    if pass_five == False:
                        factor_x.append("* 7 ")
                        x = x // 7
                        pass_seven = True
            while x % 7 == 0:
                factor_x.append("* 7 ")
                x = x // 7

        if x > 2:
            factor_x.append(f"* {x}")

        print(f"{x_initial} =", *factor_x)
