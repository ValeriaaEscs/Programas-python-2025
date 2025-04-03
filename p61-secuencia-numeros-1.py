# Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee

import os; os.system ('clear')

n = int(input('Dame un numero ? '))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=' ')
    print()

print('\nProceso terminado.')