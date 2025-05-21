# Ejemplificar el uso de una funcion para con 2 parametros
import os

def tabla(t,n):
    for i in range(1, n+1):
        print(f'{t} x {i} = {t*i}')

os.system('clear')

t = int(input('Que tabla ? '))
n = int(input('Hasta donde ? '))
tabla(t,n)