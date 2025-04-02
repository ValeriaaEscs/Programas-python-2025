# Tablas de multiplicar con ciclo for

import os;

while(True):

  os.system('clear')
  t = int(input('Que tabla  ? '))
  n = int(input('Hasta donde  ? '))

  for i in range(1, n + 1):
    print(f'{t} x {i} = {t * i }')

  if input('\n\nDeseas continuar (S/N) ? ').upper()=='N': break

print('\nProceso Terminado')
