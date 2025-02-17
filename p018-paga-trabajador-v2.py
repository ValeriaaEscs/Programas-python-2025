# Calcular la paga de un trabajador considerando que las horas extra se pagan al doble

import os; os.system('clear')

print('Calcular la paga de un trabajador considerando que las horas extra se pagan al doble\n')

nombre = input('Nombre del trabajador ?')
horas = int(input('Horas trabajadas ? '))
paga = float(input('Paga x hora ? '))

extra = pextra = total = 0 # asignamos el valor de 0 a las 3 variables 

if horas > 40:
    extra = horas - 40
    pextra = extra * ( 2 * paga)
    total = (40 * paga) + pextra

    total = paga * horas

print(f'{nombre} trabajo {horas} horas, con una paga de {paga} pesos, paga extra {pextra} pesos, pago total {total}')