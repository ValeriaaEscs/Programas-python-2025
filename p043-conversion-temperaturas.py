# Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores introducidos por el usuario

import os
os.system('clear')

while True:
    print('\nConversión de Celsius a Fahrenheit ')
    
    # Solicitar la temperatura inicial y final
    temp_inicial = int(input('Ingrese la temperatura inicial en °C: '))
    temp_final = int(input('Ingrese la temperatura final en °C: '))

    if temp_inicial > temp_final:
        print('Error: La temperatura inicial debe ser menor o igual a la temperatura final.')
    else:
        temp_actual = temp_inicial
        
        while temp_actual <= temp_final:
            fahrenheit = (temp_actual * 9/5) + 32
            print(f'{temp_actual}°C = {fahrenheit:.2f}°F')
            temp_actual += 1  

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break 
    
print('\nProceso Terminado :)')