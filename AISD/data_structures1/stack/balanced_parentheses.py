"""
Napisz funkcję sprawdzającą poprawność nawiasów. Np.

(()) -> True
((()) -> False
(13(2)23) -> True
() -> True
)( -> False

Wykorzystaj do tego celu stworzony stos - Stack.
"""


def is_balanced_parentheses(expresion):
    pass


if __name__ == '__main__':
    assert is_balanced_parentheses('(())')
    assert is_balanced_parentheses('(2(1)3)')
    assert is_balanced_parentheses(');\'(;);(;') is False
