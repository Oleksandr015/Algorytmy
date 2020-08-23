from typing import Optional


class Node:
    def __init__(self, value, left: Optional['Node'], right: Optional['Node']):
        self.left = left
        self.right = right
        self.value = value
