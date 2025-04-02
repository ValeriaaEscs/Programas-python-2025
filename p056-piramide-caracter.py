# Imprime un cuadro de asterisco 

import os


while(True):
   os.system('clear')

   n = int(input('Cuantos renglones ? '))
   c = input('Caracter ? ')

   for i in range(1, n+1):
       for j in range(1, i+1):
           print(c, end='')
       print()
    
   if input('\n\nDeseas continuar (S/N) ? ').upper()=='N': 
       break

print('\nProceso Terminado')
    