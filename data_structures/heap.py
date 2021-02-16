
if __name__ == '__main__':

    import heapq
    li = [5, 7, 9, 1, 3]

    heapq.heapify(li)
    print(f'The created heap is: {li}')

    heapq.heappush(li, 4)
    print(f'The modified heap after push is: {li}')

    print(f'The popped and smallest element is: {heapq.heappop(li)}')
    print(f'The modified heap: {li}')
    print(f'The popped and smallest element is: {heapq.heappop(li)}')
    print(f'The modified heap: {li}')
    print(f'The popped and smallest element is: {heapq.heappop(li)}')
    print(f'The modified heap: {li}')
