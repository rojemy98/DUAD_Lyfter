"""
Implemente un bubble_sort que funcione para los ejercicios de estructura de datos:
"""

# STACK

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")

        temp = self.top
        self.top = self.top.next
        return temp.value
    
    def print_stack(self):
        current = self.top
        if current is None:
            print("Stack is empty")
            return

        print("Top")
        print("↓")
        while current:
            print(current.value)
            current = current.next

    def bubble_sort(self):
        if self.top is None:
            return

        swapped = True

        while swapped:
            swapped = False
            current = self.top

            while current.next is not None:
                if current.value > current.next.value:
                    # intercambia valores
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True

                current = current.next


# Dequeu

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None  # izquierda
        self.tail = None  # derecha

    # Agrega al inicio
    def push_left(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Agrega al final
    def push_right(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Quita del inicio
    def pop_left(self):
        if self.head is None:
            raise IndexError("pop_left from empty deque")

        value = self.head.value
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return value

    # Quita del final
    def pop_right(self):
        if self.tail is None:
            raise IndexError("pop_right from empty deque")

        value = self.tail.value
        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return value

    def print_deque(self):
        current = self.head

        if current is None:
            print("Deque is empty")
            return

        print("LEFT -> ", end="")
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("RIGHT")

    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True

        while swapped:
            swapped = False
            current = self.head

            while current.next is not None:
                if current.value > current.next.value:
                    # cambia valores
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True

                current = current.next


# BinaryTree

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

    def print_sorted(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)