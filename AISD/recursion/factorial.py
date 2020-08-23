def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_non_recursive(n):
    if n <=0:
        return 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i

    return factorial


def fact(x):
    if x == 1:
        return 1
    return x * fact(x-1)

if __name__ == '__main__':
    print(factorial_recursive(3))
    print(factorial_recursive(4))
    print(factorial_recursive(0))
    print(factorial_recursive(1))
    print()
    print(factorial_non_recursive(3))
    print(factorial_non_recursive(4))
    print(factorial_non_recursive(0))
    print(factorial_non_recursive(1))

    print(fact(3))