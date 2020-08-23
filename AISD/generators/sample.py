def sample_with_list():
    # przyklad z lista
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in array:
        print(x)


def sample_with_generator():
    # przykład z generatorem
    for x in range(10):
        print(x)


def generator_manual_iteration():
    range_generator = range(10).__iter__()
    print(range_generator.__next__())
    print(range_generator.__next__())
    print(next(range_generator))
    print(next(range_generator))
    # co się stanie gdy dojdziemy do końca?


def string_generator():
    yield 'Ala'
    yield 'ma'
    yield 'kota'


def string_generator_sample():
    gen = string_generator()
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    try:
        print(gen.__next__())
    except StopIteration:
        print('Exception occurred!')


if __name__ == '__main__':
    # sample_with_list()
    # sample_with_generator()
    generator_manual_iteration()

    string_generator_sample()
