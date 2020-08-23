from solutions.data_structures.tree.node import Node


class TreeActions:

    def __init__(self, tree: Node):
        self._tree = tree

    def get_values(self):
        array = []

        def get_values_internal(node):
            if node:
                get_values_internal(node.left)
                get_values_internal(node.right)
                array.append(node.value)

        get_values_internal(self._tree)
        return array

    def find_node_by_value(self, value):
        """
        Metoda zwraca znaleziony obiekt Node, którego wartość jest równa wartości zadanej przez parametr.
        Jeżeli podana wartość nie istanieje zwracany jest None.
        Warto użyć funkcji wewnętrznej (internala), który pokazywaliśmy sobie już wcześniej. To pozwoli nam egzaminować
        każdy z Node'ów.

        Należy użyć rekurencji!

        PODPOWIEDŹ - leży sprawdzać czy potomek (left lub right) nie jest None zanim wywołamy następne zagnieżdzenie
        rekurencyjne
        """
        pass

    def get_tree_structure(self):
        """
        Metoda zwraca string opisujący hierarchię drzewa.

        Np. dla Node(1, Node(2, None, None), Node(3, None, None)) dostaniemy:
        root -> (1 -> (None) : (None)) : (2 -> (None) : (None))

        czyli mozna to przestawić w następujący sposób:
        '{node.value} -> ({left}) : ({right})'

        Należy użyć rekurencji (funkcja wewnętrzna wydaje się tutaj nabardziej rozsądnym rozwiązaniem)

        PODPOWIEDŹ - jeżeli potomek jest równy None to należy zwrócić None

        """
        pass


if __name__ == '__main__':
    tree = Node('root', Node(1, None, None), Node(2, Node(3, None, None), None))

    tree_actions = TreeActions(tree)

    print(tree_actions.get_values())
    print(tree_actions.find_node_by_value(3))
    print(tree_actions.get_tree_structure())
