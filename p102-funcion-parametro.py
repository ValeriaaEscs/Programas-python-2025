# Ejemplificar el uso de parametros en una funcion 

import os

def saluda(nombre):
    print(f'\nHola {nombre} bienvenido a las funciones en Python, tu nombre tiene {len(nombre)} caracteres')

os.system('clear')
print('\nMandando saludos desde una funcion \n')

saluda('Valeria Escobedo')
saluda('Luis Torres')
saluda('María Sánchez')

nombres = ['Fer', 'Monica', 'Blanca', 'Cindy']

#for in range(5):
#    saluda(str(s)*5)

for nombre in nombres:
    saluda(nombre)