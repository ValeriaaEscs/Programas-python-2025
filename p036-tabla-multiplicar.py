# Imprime la tabla de multiplicar t hasta n

import os
while(True):
 os.system('clear')
 print('Imprimiendo tabla de multiplicar\n')
 t = int(input('Que tabla quiere ? '))
 n = int(input('Hata donde    ? '))

 k = 1

 while k <= n :
    print(f'{t} x {k} = {t * k}')
    k += 1
 if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado')
