# Solicitar las 5 calificaciones al usuario
print("Introduce 5 calificaciones:")
cal1 = float(input("Calificación 1: "))
cal2 = float(input("Calificación 2: "))
cal3 = float(input("Calificación 3: "))
cal4 = float(input("Calificación 4: "))
cal5 = float(input("Calificación 5: "))

# Calcular el promedio
promedio = (cal1 + cal2 + cal3 + cal4 + cal5) / 5


print(f"\nTu promedio es: {promedio:.2f}")


if 0 < promedio < 6:
    print("Quedas reprobado")
elif 6 <= promedio < 7:
    print("Pasas de panzazo")
elif 7 <= promedio < 8:
    print("Muy bien, puedes mejorar")
elif 8 <= promedio < 9:
    print("Excelente, sigue así")
elif 9 <= promedio <= 10:
    print("Perfecto, tu esfuerzo valió la pena")
else:
    print("Error: El promedio debe estar entre 0 y 10.")