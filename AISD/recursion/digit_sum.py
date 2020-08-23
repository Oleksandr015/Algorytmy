"""
PODPOWIEDZI:
*   użyj operatora // do dzielenia całkowitego
*   użyj operatora %
*   sprawdz czy liczba nie jest równa 0 aby uniknac dzielenia przez zero
"""


def digit_sum(number):
    if number == 0:
        return 0
    result = number % 10 + digit_sum(number // 10)
    return result


if __name__ == '__main__':
    assert digit_sum(27) == 9
    assert digit_sum(123) == 6
    assert digit_sum(0) == 0
    assert digit_sum(1) == 1


# Напишите рекурсивную функцию для подсчета элементов в списке.

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

#Найдите наибольшее число в списке.

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max