# Pedir al usuario que ingreses colores, y hacer todas las conbinaciones posibles

import os; os.system ('clear')

colores = input('Dame los colores separados por coma : ').split(',')
print(colores)
for c1 in colores:
    for c2 in colores:
        if c1 != c2:
            print(f'>>> {c1.strip()} - {c2.strip()}')
    print()