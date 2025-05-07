# Procesar una lista de estudiantes usando una lista de diccionarios
# Se calcula la suma de los promedios y el promedio general del grupo

import os; os.system('clear')

grupo = [
     {'nombre' : 'Carlos', 'edad': 45, 'promedio' : 9},
    {'nombre' : 'Rocio', 'edad': 35, 'promedio' : 10},
    {'nombre' : 'Jose', 'edad': 30, 'promedio' : 8},
]

print(f'Los autos: {grupo} - {len(grupo)}')

while True :
    print('\n Dame los datos del estudiante')
    datos = {}
    nombre = input('Nombre : ')
    if nombre != '':
        datos['nombre'] = nombre
        datos['edad'] = int(input('Edad: '))
        datos['carrera'] = input('Carrera: ')
        datos['promedio'] = float(input('Promedio: '))
        grupo.append(datos)
    else : break

print(f'Los autos: {grupo} - {len(grupo)}')

# Imprimir una tabla con los datos de los estudiantes
print('\nDatos de los autos en forma de tabala \n')

# Imprimir los encabezados
print('-' *40)
for llave in grupo[0].keys():
    print(f'{llave:<12}', end ='')
print()
print('-'*50)

#Imprimir cada dato de cada auto
for auto in grupo:
    for v in auto.values():
        print(f'{v:<12}', end= '')
    print()
print('-'*50)

suma = 0
for alumno in grupo:
    suma = suma + alumno['promedio']


print(f'La suma de promedios es : {suma}')
print(f'El promedio del grupo : {suma / len (grupo)}')
