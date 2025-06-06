# Usar una lista de diccionarios para almacenar los datos de diferentes automoviles
# Calcular la suma de los años de cada auto

import os; os.system('clear')

autos = [
    {'marca' : 'ford', 'modelo': 'mustang', 'año' : 1964},
    {'marca' : 'vw', 'modelo': 'jetta', 'año' : 2015},
    {'marca' : 'renault', 'modelo': 'duster', 'año' : 2019},
]

print(f'Los autos: {autos} - {len(autos)}')
autos.append({'marca' : 'honda', 'modelo': 'cvr', 'año' : 2025})
print(f'Los autos: {autos} - {len(autos)}')

print('\nLos elementos (diccionarios) individuales que contiene la lista:  ')
for auto in autos:
    print(auto)

# Imprimir una tabla con los datos de los autos
print('\nDatos de los autos en forma de tabala \n')

# Imprimir los encabezados
print('-' *40)
for llave in autos[0].keys():
    print(f'{llave:<15}', end ='')
print()
print('-'*40)

#Imprimir cada dato de cada auto
for auto in autos:
    for v in auto.values():
        print(f'{v:<15}', end= '')
    print()
print('-'*40)

print(f'\nDatos en forma de registro, de los {len(autos)} autos: \n')
for auto in autos:
    for llave, valor in auto.items():
        print(f'{llave:<12} : {valor}')
    print()