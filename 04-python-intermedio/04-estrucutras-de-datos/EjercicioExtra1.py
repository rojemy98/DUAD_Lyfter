"""
Cree una estructura que represente una cola básica (Queue) con objetos enlazados

Métodos requeridos:
- enqueue(data): agrega un nodo al final
- dequeue(): elimina y retorna el nodo del inicio
- print_all(): imprime todos los elementos de la cola en orden
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.front = self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.tail is None:
            print("The queue is empty")
            return

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.tail = None

        return value
    
    def print_all(self):
        if self.front is None:
            print("The queue is empty")
            return

        current = self.front

        print("FRONT -> ", end="")

        while current:
            print(current.value, end=" -> ")
            current = current.next

        print("TAIL")