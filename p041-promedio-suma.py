# Se desea calcular la suma y el promedio de una serie de números introducidos hasta el usuario introduce 0


import os
os.system('clear')

while True:
    print('\nCálculo de Suma y Promedio ')
    
    suma = 0
    contador = 0

    while (True):
        num = int(input('Ingrese un número (0 para finalizar): '))
        
        if num == 0:
            break
        
        suma += num
        contador += 1

    if contador > 0:
        promedio = suma / contador
    else:
        promedio = 0

    print('\nSuma total:", suma')
    print('Cantidad de números ingresados:', contador)
    print('Promedio:', promedio)
    
    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break 
    
print('\nProceso Terminado :)')