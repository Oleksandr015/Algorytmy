"""
PODPOWIEDZI:
*   aby wykonać operacje swap (zamienie elementow w liscie) użyj konstrukcji: a, b = b, a
*   uważaj na przekroczenie indeksu tablicy w zagnieżdzonej pętli!
"""
from AISD.random_number_list import get_random_number_list
from time import  time

def bubble_sort(array):

    for _ in range(len(array)):
        swapped = False
        for index in range(len(array)-1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                swapped = True
        if not swapped:
            return






if __name__ == '__main__':
    array = [11, 32, 74, 79, 89, 90] #get_random_number_list(5, 100)
    print(array)
    a = time()
    bubble_sort(array)
    print(time() - a)
    print(array)
