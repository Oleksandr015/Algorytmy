from collections import deque

if __name__ == '__main__':

    # ---------------------------
    # ---------- STACK ----------
    # ---------------------------
    stack_deque = deque()

    stack_deque.append(1)
    stack_deque.append(2)
    stack_deque.append(3)

    assert stack_deque.pop() == 3
    assert stack_deque.pop() == 2
    assert stack_deque.pop() == 1

    assert stack_deque.__len__() == 0

    # ---------------------------
    # ---------- QUEUE ----------
    # ---------------------------
    queue_deque = deque()

    queue_deque.appendleft(1)
    queue_deque.appendleft(2)
    queue_deque.appendleft(3)

    assert queue_deque.pop() == 1
    assert queue_deque.pop() == 2
    assert queue_deque.pop() == 3

    assert queue_deque.__len__() == 0
