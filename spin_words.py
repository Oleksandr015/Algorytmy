def spin_words(sentence):
    s = sentence.split()
    for i in s:
        i = list(i).reverse()
        s.append(i)

        return s



if __name__ == '__main__':

    print(spin_words("Hey fellow warriors"))
