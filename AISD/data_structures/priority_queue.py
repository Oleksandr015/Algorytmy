
if __name__ == '__main__':
    from queue import PriorityQueue

    priority_queue = PriorityQueue()

    priority_queue.put((2, 'code'))
    priority_queue.put((1, 'eat'))
    priority_queue.put((3, 'sleep'))

    assert priority_queue.get() == (1, 'eat')
    assert priority_queue.get() == (2, 'code')
    assert priority_queue.get() == (3, 'sleep')
