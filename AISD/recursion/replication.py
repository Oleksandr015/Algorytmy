def replicat(value, times):

    if times == 0:
        return []
    array = replicat(value,times-1)
    array.append(value)
    return array

def replicat_two(value, times):
    lista = []
    def replicat_internal(value, times):
        if times == 0:
            return lista
        lista.append(value)
        return replicat_internal(value, times - 1)
    return replicat_internal(value, times)


def replicat_three(value, times):

    if times == 0:
        return []
    return [value] + replicat_three(value, times - 1)


if __name__ == '__main__':
    print(replicat(3,5)) #[3,3,3,3,3]
    print(replicat_three(3, 5))