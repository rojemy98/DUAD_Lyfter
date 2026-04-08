"""

Cree una clase Rectangle que:

1. Tenga atributos width y height
2. Tenga un método get_area() que retorne el área
3. Tenga un método get_perimeter() que retorne el perímetro
4. Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

"""

class Rectangle:
    def __init__(self, width, height):

        if width < 0:
            raise ValueError("Width cannot be negative.")

        if height < 0:
            raise ValueError("Height cannot be negative.")

        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)


"""

Cree una clase base Animal y dos clases hijas Dog y Cat:

1. Animal debe tener nombre y método speak() que retorne "Hace un sonido"
2. Dog debe sobrescribir speak() para decir "Guau"
3. Cat debe sobrescribir speak() para decir "Miau"

"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Makes a sound")


class Dog(Animal):
    def speak(self):
        print("Guau")


class Cat(Animal):
    def speak(self):
        print("Miau")


"""

Cree una clase Product con: Nombre, precio y cantidad

Cree una clase Inventory que:
Guarde productos en una lista

Tenga métodos para:
- Agregar un producto
- Mostrar todos los productos
- Calcular el valor total del inventario

"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.list_of_products = []

    def add_product(self, product):
        self.list_of_products.append(product)

    def get_all_products(self):
        print("\nList of available products: \n")
        for i, product in enumerate(self.list_of_products, start=1):
            print(f"{i}. {product.name} - Quantity: {product.quantity}")

    def get_inventory_total_value(self):
        total_value = 0.0

        for product in self.list_of_products:
            total_value = total_value + (product.price * product.quantity)
        print(f"\nThe inventory total value is: {total_value:.2f}\n")