if __name__ == '__main__':
    array = [1, 3, 5, 9, 2, 6]
    generator = (item for item in array if item > 3)
    print(generator.__next__())
    print(generator.__next__())
    print(generator.__next__())
