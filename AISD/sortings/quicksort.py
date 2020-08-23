from solutions.random_number_list import get_random_number_list


def partition(array, begin, end):
    # np. 2 9 1 5 3 3 8 10 [6]
    i = begin - 1
    pivot = array[end]  # zawsze zakladamy ze pivot jest ostatnim elementem
    for j in range(begin, end):
        # sprawdzamy czy aktualny element jest mniejszy niz pivot,
        # jezeli tak, to inkrementujemy i - indeks mniejszego elementu. Pozwoli to zamienić znaleziony mniejszy element
        # z wiekszym elementem aktualnie znajdujacym sie w indeksie i (dzieki inkrementacji)
        # ...
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # np. 2 3 1 5 (3) 9 8 10 [6]
    # zamieniamy następny element wiekszy od pivota z pivotem.
    # np. 2 3 1 5 (3) [6] 9 8 10 9
    # Teraz pivot juz jest posortowany (na swoim miejscu)
    # zwracamy nowy indeks pivota
    # ...
    array[i+1], array[end] = array[end], array[i+1]
    return i + 1


def quicksort(array, begin, end):
    # warunek stopu (warunek: return)
    # ...
    if begin >= end:
        return
    pivot_index = partition(array, begin, end)
    quicksort(array, begin, pivot_index - 1)
    quicksort(array, pivot_index + 1, end)

    pivot_index = partition(array, begin, end)
    # odpowiednie wywolania rekurencyjne dla lewej i prawej strony
    # np. 2 3 1 5 3 [6] 9 8 10 9
    # lewa: 2 3 1 5 3
    # prawa: 9 8 10 9
    # ...


if __name__ == '__main__':
    array = get_random_number_list(10, 100)
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)


'''from random_number_list import get_random_number_list


def partition(array, begin, end):
    # np. 2 9 1 5 3 3 8 10 [6]
    i = begin - 1
    pivot = array[end]  # zawsze zakladamy ze pivot jest ostatnim elementem
    for j in range(begin, end):

        # sprawdzamy czy aktualny element jest mniejszy niz pivot,
        # jezeli tak, to inkrementujemy i - indeks mniejszego elementu. Pozwoli to zamienić znaleziony mniejszy element
        # z wiekszym elementem aktualnie znajdujacym sie w indeksie i (dzieki inkrementacji)

        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # np. 2 3 1 5 (3) 9 8 10 [6]
    # zamieniamy następny element wiekszy od pivota z pivotem.
    # np. 2 3 1 5 (3) [6] 9 8 10 9
    # Teraz pivot juz jest posortowany (na swoim miejscu)
    # zwracamy nowy indeks pivota
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def quicksort(array, begin, end):
    # warunek stopu
    if begin >= end:
        return
    pivot_index = partition(array, begin, end)
    # odpowiednie wywolania rekurencyjne dla lewej i prawej strony
    quicksort(array, begin, pivot_index - 1)
    quicksort(array, pivot_index + 1, end)


if __name__ == '__main__':
    array = get_random_number_list(10, 100)
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)
'''