"""

Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
Si el precio es menor a 100, el descuento es del 2%.
Si el precio es mayor o igual a 100, el descuento es del 10%.
Ejemplos:
120 → 108
40 → 39.2

"""

product_price = 0
final_price = 0

product_price = int(input("Enter the product price: "))

if(product_price >= 100):
    final_price = product_price - (product_price * 0.1)
else:
    final_price = product_price - (product_price * 0.02)

print(f"Your final product price is: {final_price}")

"""

Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos.
Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”.
Si es exactamente igual, muestre “Igual”.
Ejemplos:
1040 → Mayor
140 → 460
600 → Igual
599 → 1

"""

seconds = 0
target = 600
remaining_time = 0

seconds = int(input("Enter the time in seconds: "))

if(seconds > target):
    print("Greater than 10 minutes")
elif(seconds == target):
    print("Equal to 10 minutes")
else:
    remaining_time = target - seconds
    print(f"{remaining_time} seconds left until 10 minutes")

"""

Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado.
Luego muestre el resultado de la suma.
5 → 15 (1 + 2 + 3 + 4 + 5)
3 → 6 (1 + 2 + 3)
12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

"""

number = 0
counter = 0
result = 0

number = int(input("Enter a number: "))

while (counter <= number):
    result = result + counter
    counter += 1

print(f"The result is: {result}")

"""

Convertidor de unidades de temperatura
Pida al usuario ingresar una temperatura en Celsius
Conviértala a Fahrenheit y Kelvin
Muestre los tres valores
Ejemplo:
Entrada: "Ingrese temperatura en Celsius:" 25
Salida:
Fahrenheit: 77.0
Kelvin: 298.15

"""
celsius = 0

celsius = int(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

kelvin = celsius + 273.15

print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")

"""

Tabla de multiplicar personalizada
Pida al usuario un número del 1 al 10
Muestre su tabla de multiplicar del 1 al 12

"""

input_number = int(input("Enter a number (1-10): "))

count = 1

while count <= 12:
    result = input_number * count
    print(f"{input_number} x {count} = {result}")
    count += 1