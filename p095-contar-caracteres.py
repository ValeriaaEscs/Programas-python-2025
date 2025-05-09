# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

import os; os.system('clear')

cadena = input("Escribe una cadena: ")

# Crear diccionario vacío para almacenar los conteos
conteo = {}

# Recorrer cada carácter de la cadena
for caracter in cadena:
    if caracter in conteo:
        conteo[caracter] += 1  # Si ya existe, incrementa el conteo
    else:
        conteo[caracter] = 1   # Si no existe, lo agrega con valor 1

# Mostrar el diccionario resultante
print("\nFrecuencia de caracteres:")
print(conteo)