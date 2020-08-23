"""
Napisz funkcję sprawdzającą poprawność nawiasów. Np.

(()) -> True
((()) -> False
(13(2)23) -> True
() -> True
)( -> False

Wykorzystaj do tego celu stworzony stos - Stack.
"""
from AISD.data_structures.stack.stack import Stack


def is_balanced_parentheses(expresion):
    stack = Stack(1000)
    for i in expresion:
        if i == ')':
            return False
        break
    for j in expresion:
        if j == '(':
            stack.push(j)
        elif j == ')':
            stack.pop()
    return stack.is_empty()




if __name__ == '__main__':

    print(is_balanced_parentheses('((())'))
    print(is_balanced_parentheses('(2(1)3)'))
    print(is_balanced_parentheses(');\'(;);(;'))


# (()) -> True
# ((()) -> False
# (13(2)23) -> True
# () -> True
