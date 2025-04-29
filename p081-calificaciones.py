# Simular un riesgo de calificaciones usando un diccionario, sacamos el promedio 
# realizmaos cambios y actualizaciones

import os; os.system('clear')

materias = ['Fisica', 'Quimica','Matematicas','Geografia', 'Estadisticas']
califs = [10, 9, 8, 7.5, 6]

print(f'Lista de materias : {materias} - {len(materias)}')
print(f'Lista de califs : {califs} - {len(califs)}')

notas =  dict( zip(materias, califs) )

print(f'\nEl diccionario completo de notas es: {notas} - {len(notas)}')

notas.update({'Ingles': 10,'Programacion':7})
print(f'\nEl diccionario  es: {notas} - {len(notas)}')

notas.pop('Fisica')
notas.popitem()
print(f'\nEl diccionario  es: {notas} - {len(notas)}')

notas['Quimica'] = 10
notas.update({'Matematicas': 10})
print(f'\nEl diccionario  es: {notas} - {len(notas)}')

s = 0
print('\nMatematicas y Calificiones')
for m, c in notas.items():
    print(f'{m:<12} - {c:5}')
    s = s + c
p = s / len(notas)

print(f'La suma es {s} el primedio es {p}')

notas.clear()
print(f'\nEl diccionario es {notas} - {len(notas)}')
