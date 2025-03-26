# El un numero 100 que es el numero limite ; obtener los nuemros pares y sumarlos entre ellos

import os
os.system('clear')

while True:
    print('\nNúmeros Pares y su Suma ')
    n = int(input('Ingrese un número límite (n, menor o igual a 100): '))

    if n > 100:
        print('Por favor, ingrese un número mayor o igual a 100.')
       

    contador = 100
    suma = 0

    print('Números pares:', end=' ')
    while contador >= n:
        print(contador, end=' ')
        suma += contador
        contador -= 2  

    print('\nSuma de los números pares:', suma)

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break 
    
print('\nProceso Terminado :)')