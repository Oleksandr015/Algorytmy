def find_first_capital_letter(array, index=0):
    if array == '':
        return 'empty'
    if len(array) == index:
        raise ValueError(f'No capital letter {array}')
    if array[index].isupper():
        return array[index]

    return find_first_capital_letter(array, index + 1)


def find_first_capital_letter_internal(array):
    def find_first_capital_letter_internal(array, index):
         if array == '':
             return 'empty'
         if len(array) == index:
             raise ValueError(f'No capital letter {array}')
         if array[index].isupper():
             return array[index]

         return find_first_capital_letter_internal(array, index + 1)

    return find_first_capital_letter_internal(array, 0)


if __name__ == '__main__':
    print(find_first_capital_letter('Aawd'))
    print(find_first_capital_letter_internal('Bawd'))