"""
Lista doblemente enlazada

Requisitos:
Cada nodo debe tener referencia al siguiente y al anterior

- append(data): Agrega al final
- prepend(data): Agrega al inicio
- delete(data): Elimina el primer nodo con ese valor
- print_forward() y print_backward(): Imprime en ambas direcciones
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
    
        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        self.head.prev = new_node
        self.head = new_node
        self.head.next = temp

    def delete(self, data):

        if self.head is None:
            print("Double Linkedlist is empty")
            return
        
        current = self.head

        while current:
            if current.value == data:

                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return

            current = current.next

        print("Value not found")

    def print_forward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        print("HEAD -> ", end="")

        while current:
            print(current.value, end=" <-> ")
            current = current.next

        print("None")

    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while current.next:
            current = current.next

        print("TAIL -> ", end="")

        while current:
            print(current.value, end=" <-> ")
            current = current.prev

        print("None")