# Ejemplificar el uso de una funcion que recibe mas de 1 parametro

import os

def saluda(paterno, nombre, edad):
    print(f'\n Hola {paterno}, {nombre} tienes una edad de {edad}')

os.system('clear')
print('\nInvocando una fundacion con mas de 1 parametro')
saluda('Escobedo','Valeria', 24)
# saluda('Escobedo') # se genra error por falta de parametros
# saluda('Escobedo','Valeria', 25,28) # se genera error, sobran parametros
