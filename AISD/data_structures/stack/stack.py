"""
*   Elementy stosu przechowywane w prywatnej liście _items
*   Parametrem konstruktora rozmiar stosu capacity, przechowywany w atrybucie prywatnym
*   Metoda push dodaje element na stos. Zaimplementuj własny wyjątem StackOverflowException rzucany w momencie
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
from collections import deque

import pytest



class StackOverflowException(Exception):
    pass


class EmptyStackException(Exception):
    pass


class Stack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._items = deque()

    def push(self, element: str):
        if len(self._items) == self.capacity:
            raise StackOverflowException(f"Full stack!")
        self._items.append(element)



    def pop(self):
        if self.is_empty():
            raise EmptyStackException(f"Empty stack!")
        return self._items.pop()


    def is_empty(self):
        return not self._items


    def __repr__(self):
        return f'{self._items}'

if __name__ == '__main__':
    stack = Stack(3)
    stack.push('first')
    stack.push('second')
    stack.push('third')

    with pytest.raises(StackOverflowException):
            stack.push('fourth')


    print(stack)
    stack.pop()
    stack.pop()
    stack.pop()
    with pytest.raises(EmptyStackException) as excinfo:
        stack.pop()

    print(stack)

