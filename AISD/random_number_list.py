"""
Napisz ciało funkcji get_random_number_list, która zwraca listę n losowych liczb z przedziału od 0 do random_max_number.
*   Użyć list comprehension
*   Użyć randint z biblioteki random (from random import randint) przyjmującej dolny oraz górny zakres generowanych
    liczb. Np. randint(0, 5) wygeneruje liczbe całkowitą losową z przedziału od 0 do 5.

"""
from random import randint


def get_random_number_list(n, random_max_range):
    return [randint(0, random_max_range) for _ in range(n)]



if __name__ == '__main__':
    print(get_random_number_list(10, 100))
