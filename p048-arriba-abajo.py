# Imprimir numeros de 1 a n o de n a 1

import os;

while(True):
    os.system('clear')

    print('\nImprimir  numeros usando ciclo for ')
    print('[ 1 ] Imprimir numeros de 1 a n ')
    print('[ 2 ] Imprimir numeros de n a 1 ')
    print('[ 3 ] Salir')
    op = int (input('Que eliges ?  '))

    if op==1:
        print(f'\nImprimir numeros de 1 a n ')
        n = int(input('Hasta donde ? '))
        for x in range(1, n+1, 1): print(x, end=' ')
    elif op==2:
        print(f'\nImprimir numeros de 1 a n ')
        n = int(input('Hasta donde ? '))
        for x in range(n, 0, -1): print(x, end=' ')
    elif op==3:
        print('\nTe vamos a extrañar :(  ')
    

    if input('\n\nDeseas continuar (S/N) ? ').upper()=='N': break
    
print('\n Hemos llegado al final ... ')