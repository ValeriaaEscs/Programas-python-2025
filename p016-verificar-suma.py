# Verificar si un numero entero es positivo, negativo o cero

import os; os.system('clear')

print('Verificar si un numero entero es positivo, negativo o cero\n')

print('Dame 3 numeros enteros separados por <Enter> ')
n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3:
    print('\nLa suma de los dos primeros numeros es igual al tercero \n')
else:
    print('\nLa suma de los dos primeros numeros NO ES igual al tercero\n')

print('\nGracias por utilizar este programa')