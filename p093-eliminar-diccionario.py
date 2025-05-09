# Crear un diccionario de llave de cadena municipios con los siguientes elementos:

import os; os.system('clear')

municipios = {
    "Apozol": 1863,
    "Calera": 1868,
    "Fresnillo": 1554,
    "Guadalupe": 1821,
    "Jalpa": 1824,
    "Jerez": 1824,
    "Loreto": 1931,
    "Mazapil": 1824,
    "Momax": 1857
}

# Mostrar diccionario original
print("Diccionario original:")
print(municipios)

# Eliminar "Apozol" con del
del municipios["Apozol"]
print("\nDespués de eliminar 'Apozol' con del:")
print(municipios)

# Eliminar "Fresnillo" con pop()
municipios.pop("Fresnillo")
print("\nDespués de eliminar 'Fresnillo' con pop():")
print(municipios)

# Eliminar el último elemento con popitem()
municipios.popitem()
print("\nDespués de eliminar el último elemento con popitem():")
print(municipios)

# Eliminar todos los elementos con clear()
municipios.clear()
print("\nDespués de eliminar todos los elementos con clear():")
print(municipios)
