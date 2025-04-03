# Se desea imprimir los numeros de 1 a n de 10 en 10

import os; os.system ('clear')


n = int(input('Dame número: '))

for i in range(1, n + 1, 10):
    print(i, end=' ')


print('\nProceso terminado.')