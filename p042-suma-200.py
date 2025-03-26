# Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200 y despues la suma y cuantos numeros fueros

import os
os.system('clear')

while True:
    print('\nCálculo de Suma hasta 200 ')
    
    suma = 0
    contador = 0

    while suma < 200:
        num = int(input('Ingrese un número: '))
        suma += num
        contador += 1

    print('\nSuma total:', suma)
    print('Cantidad de números ingresados:', contador)

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break 
    
print('\nProceso Terminado :)')