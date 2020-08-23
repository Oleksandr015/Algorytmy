def recursion():
    t = 0
    recursion()


def recursion_with_param_print_before(param):
    print(param)
    recursion_with_param_print_before(param)


def recursion_with_param_print_after(param):
    recursion_with_param_print_after(param)
    print(param)


if __name__ == '__main__':
    recursion()
    recursion_with_param_print_before('Hello World')
    recursion_with_param_print_after('Hello World')
