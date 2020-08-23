def print_numbers(some_param: int):
    if some_param > 0:
        print_numbers(some_param - 1)
    print(some_param)



def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


if __name__ == '__main__':

    print_numbers(10)
    #countdown(5)
