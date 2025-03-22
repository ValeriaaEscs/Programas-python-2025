# Imprime numeros de 1 a n 

import os; os.system('clear')

n = int(input('Hasta donde? '))
d = int(input('Decrementos? '))

c = n
while c <= 100:
    print(c, end=' ')
    c += 1
else:
    print('\n\nValor funal de c=', c)

print('\nProceso terminado')