# Dividir en cifras un numero entero
#145

import os;os.system('clear')

print('Dividir un nuemro entero de 3 cifras en unidades, decenas y centenas')

#numero = int(input('Dame un numero de 3 cifras ? '))

n =145

u = n % 10
n = n // 10
d = n % 10
n = n // 10
c = n

print(f'Centenas : {c}\nDecenas: {d}\nUnidade:{u}')
