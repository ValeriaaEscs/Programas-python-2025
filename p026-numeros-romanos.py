# Solicitar el numero al usuario
num = int(input('Introduce un numero romano entre 1 al 10: '))

romanos = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"
}

if 1 <= num <= 10:
    print(f'El número {num} en romano es {romanos[num]}')
else:
    print('Error: el número debe estra entre 1 y  10.')
    