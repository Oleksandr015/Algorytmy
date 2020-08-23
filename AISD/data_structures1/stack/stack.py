"""
*   Elementy stosu przechowywane w prywatnej liście _items
*   Parametrem konstruktora rozmiar stosu capacity, przechowywany w atrybucie prywatnym
*   Metoda push dodaje element na stos. Zaimplementuj własny wyjątek StackOverflowException rzucany w momencie
    przepełnienia stosu
*   Metoda pop wyciąga element ze stosu i zwraca go. Jeżeli stos jest pusty rzuca wyjątkiem EmptyStackException
*   Metoda is_empty zwraca True jezeli stos jest pusty, False w innym przypadku

Napisz krótkie testy w tym pliku. Można użyć assert.
np. assert stack.is_empty()
lub
with pytest.raises(EmptyStackException):
    stack.pop()

Zainstaluj pytest jezeli trzeba: pip install pytest
"""
import pytest


class StackOverflowException(Exception):
    pass


class EmptyStackException(Exception):
    pass


class Stack:

    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity

    def push(self, elem):
        pass

    def pop(self):
        pass

    def is_empty(self):
        pass


if __name__ == '__main__':
    stack = Stack(3)

    with pytest.raises(EmptyStackException):
        stack.pop()

    stack.push(1)
    stack.push(2)
    stack.push(3)
