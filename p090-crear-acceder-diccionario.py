# Crear diccionario de llave numerica dias, con los siguentes elementos:

import os; os.system('clear')

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Mostrar el diccionario completo
print("Diccionario completo: ")
for clave, valor in dias.items():
    print(clave, ":", valor)

# Acceder a los elementos
print("\nPrimer elemento :", dias[1])
print("Último elemento :", dias[7])
print("Quinto elemento :", dias.get(5))
print("Séptimo elemento :", dias.get(7))