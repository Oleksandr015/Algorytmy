"""
PODPOWIEDZI:
*   zapisz indeks minimalnej wartości do zmiennej. Początka wartość tej zmiennej powinna być równa pierwszemu
    elementowi nieposortowanej tablicy
*   szukaj najmniejszego elementu nieposortowanej tablicy w przedziale (aktualny element + 1, dlugosc tablicy)
"""
from AISD.random_number_list import get_random_number_list


def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
        return array


if __name__ == '__main__':
    array = get_random_number_list(5, 100)
    print(array)
    selection_sort(array)
    print(array)
    print()

    print(selection_sort([1,5,8,9]))
