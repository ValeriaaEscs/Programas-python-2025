# Ejemplificar el uso de parametros  con valores por defecto

import os 

def saluda(nombre='nadie', edad=0):
    print(f'\nHola {nombre}, tienes una edad de {edad}')

os.system('clear')

print('\nInvocar una funcion con un numero distinto de parametros')

saluda('Andrea')
saluda()
saluda('Valeria', 24)