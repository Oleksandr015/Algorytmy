def print_list_content(array, index=0):
    if index == len(array):
        return
    print(array[index])

    print_list_content(array, index + 1)



if __name__ == '__main__':
    print_list_content([])
    print_list_content([1,2,3])
    print_list_content([-1,5,'s',True])
    print_list_content([[1,2], [5,8]])
