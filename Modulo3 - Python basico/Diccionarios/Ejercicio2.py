"""

Cree un diccionario que guarde el total de ventas de cada UPC.

"""

sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

sales_by_upc = {}

for sale in sales:
    for item in sale["items"]:
        upc = item["upc"]
        price = item["unit_price"]
        sales_by_upc[upc] = sales_by_upc.get(upc, 0) + price

print(sales_by_upc)

"""

Agrupar empleados por departamento
Dada una lista de empleados donde cada uno tiene nombre, correo y
departamento, cree un diccionario que agrupe los empleados por su departamento:

"""

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

grouped_by_department = {}

for employee in employees:
    department = employee["department"]
    if(department in grouped_by_department):
        grouped_by_department[department].append(employee)
    else:
        grouped_by_department[department] = [employee]

print(grouped_by_department)

"""

Dada una lista de productos vendidos, donde cada uno tiene categoría y
precio, cree un diccionario que acumule el total por categoría.

"""

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

grouped_by_category = {}

for product in products:
    category = product["category"]
    price = product["price"]
    grouped_by_category[category] = grouped_by_category.get(category, 0) + price

print(grouped_by_category)