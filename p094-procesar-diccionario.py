# Listas de nombres y sueldos

import os; os.system('clear')

nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

# Crear el diccionario uniendo nombres y sueldos
trabajadores = dict(zip(nombres, sueldos))

# Mostrar el diccionario resultante
print("Diccionario de trabajadores:")
print(trabajadores)

# Iterar usando las llaves
print("\nNombres de los trabajadores (keys):")
for nombre in trabajadores.keys():
    print(nombre)

# Iterar usando los valores
print("\nSueldos de los trabajadores (values):")
for sueldo in trabajadores.values():
    print(sueldo)

# Iterar usando la llave y el valor basado en la llave
print("\nNombre y sueldo (basado en llave):")
for nombre in trabajadores.keys():
    print(nombre, "->", trabajadores[nombre])

# Iterar usando items()
print("\nNombre y sueldo (usando items()):")
for nombre, sueldo in trabajadores.items():
    print(nombre, "->", sueldo)

# Calcular la suma de sueldos
suma_sueldos = sum(trabajadores.values())
print("\nSuma de todos los sueldos:", suma_sueldos)

# Calcular el promedio de sueldos
promedio_sueldos = suma_sueldos / len(trabajadores)
print("Promedio de los sueldos:", promedio_sueldos)