# Muestra el tipo de ángulo según sus grados
print('Mostrando el tipo de ángulo en base a los grados')

try:
    # Solicitar el ángulo al usuario
    angulo = int(input('Dame un ángulo: '))

    # Mostrar el resultado
    print(f'El ángulo tiene {angulo} grados, por lo tanto, es un ángulo ', end='')

    # Clasificación del ángulo
    if angulo < 90:
        print('agudo.')
    elif angulo == 90:
        print('recto.')
    elif 90 < angulo < 180:
        print('obtuso.')
    elif angulo == 180:
        print('llano.')
    elif 180 < angulo < 360:
        print('cóncavo.')
    else:
        print('fuera de rango.')

except ValueError:
    print('Error: Debes ingresar un número entero.')