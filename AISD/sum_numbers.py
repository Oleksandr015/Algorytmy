"""
Napisz funkcje sum_numbers przyjmującą listę liczb całkowitych.
Zwraca sumę elementów listy.
W wywołaniu przekaż listę wygenerowaną przez funkcję get_random_number_list().
"""
from random_number_list import get_random_number_list



def sum_numbers(random_list):
    summ = 0
    count = 0
    for i in random_list:
        summ += i
        count += 1

    return count


if __name__ == '__main__':
    array = get_random_number_list(10, 100)
    print(sum_numbers(array))
