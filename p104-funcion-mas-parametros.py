# Ejemplificar el uso de una funcion que recibe n parametros

import os

def saludatodos(*todos):
    print(f'\nSludos para {todos}')
    print(f'\nTu eres un lciente especial: {todos[0]}')
    print(f'\nSludos a todos los clientes de esta tienda:  {'/'.join(todos)}\n')
    for nombre in todos:
        print(f'{nombre} - Es un placer contar con tu preferencia en esta tienda')


os.system('clear')
print('\nInvocando una funcion con un numero n de parametros')

saludatodos('Luis', 'Andrea', 'Camila', 'Emiliano')