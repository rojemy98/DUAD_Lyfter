"""
Cree una estructura de objetos que asemeje un Binary Tree.

1. Debe incluir un método para hacer print de toda la estructura.
2. No se permite el uso de tipos de datos compuestos como lists, dicts o
tuples ni módulos como collections.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._print_vertical(self.root, "", True)

    def _print_vertical(self, node, prefix, is_last):
        if node is not None:
            print(prefix + ("└── " if is_last else "├── ") + str(node.value))

            new_prefix = prefix + ("    " if is_last else "│   ")

            if node.left or node.right:
                if node.left and node.right:
                    self._print_vertical(node.left, new_prefix, False)
                    self._print_vertical(node.right, new_prefix, True)
                elif node.left:
                    self._print_vertical(node.left, new_prefix, True)
                elif node.right:
                    self._print_vertical(node.right, new_prefix, True)