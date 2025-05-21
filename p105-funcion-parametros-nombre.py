# Emplificar el uso de nombre en los parametros,
# Esto permite invocar a la funcion con los parametros en el orden deseando nombre

import os

def saluda(paterno, materno, nombre):
    print(f'\n Hola {paterno} {materno} {nombre} bienvenido a esta Universidad ')

os.system('clear')

print(f'\nInvocar una funcion usando los nombres de los parametros')

saluda('Escobedo','Sánchez', 'Valeria')

saluda('Valeria', 'Escobedo', 'Sánchez')