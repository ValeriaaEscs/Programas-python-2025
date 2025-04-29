# Ejemplo de uso de un diccionario

import os; os.system('clear')

estudiante = {
    'nombre':'Juan Perez',
    'edad' : 45, 
    'email': 'jperez@msn.com', 
    'carrera' : 'Sistemas' } 

print(f'El diccionario: {estudiante}, elementos {len(estudiante)}')

# modificar / agregar
estudiante['calificacion'] = 9.5
estudiante['email'] = 'juanp@gamil.com'
print(f'\nEl diccionario: {estudiante}, elementos {len(estudiante)}')

print(f'\nIterar por las llaves:')
for k in estudiante.keys():
    print (k)

print('\nIterar por valores: ')
for v in estudiante.values():
    print(v)

for k, v in estudiante.items():
    print(f'{k:<13} : {v}')
    
