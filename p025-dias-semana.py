# Solicitar el numero al usuario
num = int(input('Introduce un numero entre 1 y 7: '))

if num == 1:
    print('Domingo')
elif num == 2:
    print('Lunes')
elif num == 3:
    print('Martes')
elif num == 4:
    print('Miércoles')
elif num == 5:
    print('Jueves')
elif num == 6:
    print('Viernes')
elif num == 7:
    print('Sábado')

else:
    print('Error: numero fuera de rango. Debe estar dentro del rango.')
    