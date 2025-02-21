# Solicitar datos al usuario 
nombre = input('Nombre del estudiante: ')
sexo = input ('Sexo (h/m): ').lower()
edad = int(input('Edad: '))

print('Introduce tres calificaciones: ')

cal1 = float(input('Calificacion 1: '))
cal2 = float(input('Calificacion 2: '))
cal3 = float(input('Calificacion 3: '))

#Promedio de las calificaiones 
promedio = (cal1 + cal2 + cal3) / 3

if sexo == 'm' and edad > 21 and 8 <= promedio <= 9.5:
    print(f'\n¡Felicidades {nombre}! Has sido aceptado en la Universidad Kitty Kat SA. ')
else:
    print(f'\nLo sentimos {nombre}, no cumples con los requicitos de admisión')