# Solicititar tres numeros al usuario

print('Ingresar tres números enteros')
a = int(input('Primer número: '))
b = int(input('Segundo número: '))
c = int(input('Tercer numero: '))

if b == a + 1 and c == b + 1 :
    print('Los numeros son consecutivos.')

else:
    print('Error: Los numeros no son consecutivos.')
