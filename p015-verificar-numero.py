# Verificar si un numero entero es positivo, negativo o cero

import os; os.system('clear')

print('Verificar si un numero entero es positivo, negativo o cero\n')

n = int(input('Dame un numero entero ? '))

if n > 0:
    print('El numero es positivo\n')
if n < 0:
    print('El numero es negativo\n')
if n == 0:
    print('El numero es cero\n')

print('\nProceso terminaado')