#Se desea imprimir los pares de 2 a n y su suma 

import os; os.system ('clear')


n = int(input('Dame número: '))

suma = 0

for i in range(2, n + 1, 2):
    print(i, end= ' ')
    suma += i

print(f'\nLa suma es = {suma}')

print('\nProceso terminado.')