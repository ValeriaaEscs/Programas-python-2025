# Aceptar estuduiante en base cierto criterios

print('Universidad UAZ SA de CV')

nombre = input('Dame tu nombre:  ')
edad = int(input('Dame tu edad:  '))

if edad < 18:
    print('Solo aceptamos a mayires de 18 años.')
else:
    print('Dame 2 calificaciones: ')
    c1 = int(input('Calificacion 1:  '))
    c2 = int(input('Calificacion 2:  '))

if c1 < 8 or c2 < 8:
    print('Solo aceptamos alumnos con calificacion mayores o iguales a 8.')
else:
    print(f'{nombre}, Bienvenid@ a la Univeridad UAZ. Tu edad ({edad}) y calificaciones ({c1} y {c2}) lo permiten.')