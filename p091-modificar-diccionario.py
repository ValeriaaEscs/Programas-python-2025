# Crear un diccionario de llaves de cadena países, con los siguientes elementos

import os; os.system('clear')

paises = {
    "Argentina": 100,
    "Brasil": 200,
    "Colombia": 300,
    "Chile": 400,
    "Ecuador": 500,
    "Bolivia": 600,
    "Jamaica": 700
}

# Mostrar el diccionario original
print("Diccionario original:")
for pais, valor in paises.items():
    print(pais, "-", valor)

# Modificar elementos usando []
paises["Brasil"] = 250
paises["Chile"] = 450

# Modificar elementos usando update()
paises.update({"Bolivia": 650})
paises.update({"Jamaica": 750})

# Mostrar el diccionario modificado
print("\nDiccionario modificado:")
for pais, valor in paises.items():
    print(pais, "-", valor)