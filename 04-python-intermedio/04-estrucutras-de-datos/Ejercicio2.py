"""
Cree una estructura de objetos que asemeje un Double Ended Queue.

1. Debe incluir los métodos de push_left y push_right (para agregar
nodos al inicio y al final) y pop_left y pop_right (para quitar nodos
al inicio y al final).

2. Debe incluir un método para hacer print de toda la estructura.

3. No se permite el uso de tipos de datos compuestos como lists, dicts o
tuples ni módulos como collections.
"""

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