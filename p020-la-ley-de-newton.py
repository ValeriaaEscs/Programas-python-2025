# Calcular la ley de newton con su formula(fuerza = masa * aceleracion)

print('Calculando los valores de la Segunda Ley de Newton')
print('[1] Calcular la Fuerza')
print('[2] Calcular la Masa')
print('[3] Calcular la Aceleracion')

op = int(input('Elige una opcion'))

if op == 1:
    print('\nCalculando la fuerza... ')
    m = float(input('Dame la masa: '))
    a = float(input('Dame la aceleracion'))
    f = m * a
    print(f'La fuerza es {f} N')

elif op == 2:
    print('\nCalculando la masa... ')
    f = float(input('Dame la fuerza...'))
    a = float(input('Dame la aceleracion...'))
    if a != 0:
        m = f / a
        print(f'La masa es {m} kg')
    else:
        print('Error: La aceleracion no puede ser cero.')
elif op == 3:
     print('\nCalculando la aceleracion... ')
     f = float(input('Dame la fuerza:  '))
     m = float(input('Dame la masa:  '))
     if m != 0:
         a = f / m 
         print(f'La aceleracion es {a} m/s2')
     else:
       print('Error: la masa no puede ser cero')

else:
 print('Opcion invalida')