# Mostrar las operaciones que se pueden efectuar entre dos conjuntos

import os ; os.system('clear')

c1 = {1,2,3,4,5}
c2 = {5,6,7,8,9,10}
c3 = {9.10,11,12,13}
c4 = {3,4,5}

print('\nEjemplo de las operaciones entre dos conjuntos')
print(f'c1 : {c1}\nc2 : {c2}\nc3 : {c3}\nc4 : {c4}')

print(f'Union: ')
print(f'c1 union c2 : {c1.union(c2)}')
print(f'c1 union c3 : {c1 | c3 }')

print('\nIntersección: ')
print(f'c1 interseccion c2 : {c1.intersection(c2)}')
print(f'c1 interseccion c3 : {c1 & (c3)}')

print('\nDiferencia : ')
print(f'c1 diferencia c4 : {c1.difference(c4)}')
print(f'c2 diferencia c3 : {c2 - c3}')

print('\nDiferencia simetrica : ')
print(f'c1 diferencia simetrica c4 : {c1.symmetric_difference(c2)}')
print(f'c2 diferencia simetrica c3 : {c2 ^ c3}')

print('\nProbar por subconjuntos : ')
print(f'c4 es subconjunto de c1 : {c4.issubset(c1)}')
print(f'c3 diferencia simetrica c2 : {c3<=c2}')

print('\nProbar por supersubconjuntos : ')
print(f'c1 es supersubconjunto de c4 : {c1.issubset(c4)}')
print(f'c2 diferencia simetrica c3 : {c2<=c3}')

print('\nVerificar la presidencia de un elemento en el conjunto:')
print(f'2 esta en c1 ?: {2 in c1}')
print(f'6 no esta en c2 ? :{6 not in c1}')