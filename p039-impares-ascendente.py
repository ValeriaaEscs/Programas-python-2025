# Dar un numero limite; obtener los nuemros impares y sumarlos entre ellos

import os
os.system('clear')

while True:
    print('\nNúmeros Impares y su Suma ')
    n = int(input('Ingrese un número límite (n): '))

    if n < 1:
        print('Por favor, ingrese un número mayor o igual a 1.')
       

    contador = 1
    suma = 0

    print('Números impares:', end=' ')
    while contador <= n:
        print(contador, end=' ')
        suma += contador
        contador += 2  

    print('\nSuma de los números impares:', suma)

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break 
    
print('\nProceso Terminado :)')