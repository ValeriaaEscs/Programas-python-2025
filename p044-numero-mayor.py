# Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir 0.


import os
os.system('clear')
    
while (True):
    print('Encontrar el número mayor')

    num = int(input('Introduce un número (0 para finalizar): '))
    
    if num == 0:
        print('No ingresaste ningún número válido.')
    else:
        mayor = num  
        
        while True:
            num = int(input('Introduce otro número (0 para finalizar): '))
            
            if num == 0:
                break  
            
            if num > mayor:
                mayor = num  
        
        print(f'El número mayor introducido es: {mayor}')


        if input('Deseas Continuar (S/N) ? ').upper() == 'N': break 
    
print('\nProceso Terminado :)')