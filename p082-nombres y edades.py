# Capturar nombre y edades, mostrarlos y calcular la suma y promedio de edades

import os; os.system('clear')

datos = {}

print('Introduce nombres y edades (nombre vacio para terminar)')

while True:
    nombre = input('Dame nombre ? ')
    if nombre != '':
        datos[nombre] = int(input('Edad ? '))
    else :
        break

print(f'\nLos nombres y edades {datos} - {len(datos)}')

s = 0
for n, e in datos.items():
    print(f'{n:<20} - {e:2}')
    s = s + e
p = s / len(datos)

print(f'Suma : {s} Promedio: {p}')
