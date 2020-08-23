from timeit import timeit
from collections import deque

if __name__ == '__main__':
    NUMBER = 100000
    some_array = []
    some_deque = deque()

    # append
    time = timeit(stmt=lambda: some_array.append(1), number=NUMBER)
    print(f'list.append(): {time}')
    time = timeit(stmt=lambda: some_deque.append(1), number=NUMBER)
    print(f'deque.append(): {time}')

    # pop
    time = timeit(stmt=lambda: some_array.pop(), number=NUMBER)
    print(f'list.pop(): {time}')
    time = timeit(stmt=lambda: some_deque.pop(), number=NUMBER)
    print(f'deque.pop(): {time}')

    # insert(0)/appendleft
    time = timeit(stmt=lambda: some_array.insert(0, 1), number=NUMBER)
    print(f'list.insert(0): {time}')
    time = timeit(stmt=lambda: some_deque.appendleft(1), number=NUMBER)
    print(f'deque.appendleft(): {time}')

    # pop(0)/popleft
    time = timeit(stmt=lambda: some_array.pop(0), number=NUMBER)
    print(f'list.pop(0): {time}')
    time = timeit(stmt=lambda: some_deque.popleft(), number=NUMBER)
    print(f'deque.popleft(): {time}')

