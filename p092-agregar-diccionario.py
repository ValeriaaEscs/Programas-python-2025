# Crear el diccionario de ventas, con los siguentes elementos:

import os; os.system('clear')

ventas = {
    "Juan": 1550,
    "Jose": 2600,
    "Maria": 2220
}

# Mostrar el diccionario original
print("Diccionario original:")
for nombre, cantidad in ventas.items():
    print(nombre, "-", cantidad)

# Agregar elementos usando []
ventas["Rocio"] = 2500
ventas["Mateo"] = 1567

# Agregar elementos usando update()
ventas.update({"Andrea": 9567})
ventas.update({"Miguel": 1234})

# Mostrar el diccionario actualizado
print("\nDiccionario actualizado:")
for nombre, cantidad in ventas.items():
    print(nombre, "-", cantidad)