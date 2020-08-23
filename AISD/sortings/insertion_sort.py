"""
PODPOWIEDZI:
*   zapisz aktualny element do zmiennej
*   aktualną POZYCJĘ porównywanego poprzednika przechowuj w innej zmiennej
*   wykorzystaj zagnieżdżoną while aby iterować po poprzednikach
*   w pętli while nie zapomnij sprawdzić czy nie jesteś poza indeksem tablicy np. array[-1], array[-2]
"""
from time import  time

from random import randint
def get_random_number_list(n, random_max_range):
    return [randint(0, random_max_range) for _ in range(n)]


def insertion_sort(array):
    for index in range(1, len(array)):
        current_element = array[index]
        current_position = index
        while current_position > 0 and current_element < array[current_position - 1]:
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        array[current_position] = current_element
    return array


if __name__ == '__main__':
    array = get_random_number_list(100, 100)
    print(array)
    a = time()

    insertion_sort(array)
    print(time() - a)
    print(array)
