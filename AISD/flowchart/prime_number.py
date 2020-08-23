def prime_number(n):
    if n <= 1:
        return False
    else:
        i = 2
        while True:
            if i == n:
                return True
            elif n % i == 0:
                return False
            else:
                i += 1
def prime_number_next(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    assert prime_number(1) is False
    assert prime_number(2) is True
    assert prime_number(3) is True
    assert prime_number(21) is False
    assert prime_number(17) is True

    assert prime_number_next(1) is False
    assert prime_number_next(2) is True
