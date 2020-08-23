"""
*   tworzenie listy musi odbywać się poza pomiarem czasu
*   do tworzenia listy należy wykorzystać get_random_number_list, lista powinna byc duza np 10000 elementów
*   wyświetl otrzymane czasy z wszystkich zamplementowanych algorytmów w celu porównania
*   użyc biblioteki timeit
"""
from copy import deepcopy
from datetime import time
from timeit import timeit

from AISD.random_number_list import get_random_number_list
from AISD.sortings.bubble_sort import bubble_sort
from AISD.sortings.selection_sort import selection_sort


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
    N = 50000
    RAMDOM_MAX_RANGE = 100000

    array = get_random_number_list(N, RAMDOM_MAX_RANGE)
    # start = time()
    # insertion_sort(array)
    # end = time() - start
    # print(end)

    time = timeit(stmt=lambda: insertion_sort(deepcopy(array)), number=1)
    print(time)
    time = timeit(stmt=lambda: bubble_sort(deepcopy(array)), number=1)
    print(time)
    time = timeit(stmt=lambda: selection_sort(deepcopy(array)), number=1)
    print(time)
