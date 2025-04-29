# Precesar notas sobre los numero que ingrese el usuario


print("Introduce notas entre 0 y 100 (termina con 0)")

suma = 0
contador = 0
nota = -1
maxima = None
minima = None
menor_promedio_conteo = 0

while True:
    nota = int(input("Introduce una nota (0 para terminar): "))
    if nota == 0:
        break
    if nota < 0 or nota > 100:
        print("Nota inválida. Debe estar entre 0 y 100.")
        continue

    suma += nota
    contador += 1

    if maxima is None or nota > maxima:
        maxima = nota
    if minima is None or nota < minima:
        minima = nota

if contador > 0:
    promedio = suma / contador
    print(f"\nNotas ingresadas: {contador}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Nota máxima: {maxima}")
    print(f"Nota mínima: {minima}")

    print("\nVuelve a introducir las mismas notas para analizar menores al promedio:")
    contador_temp = 0
    while contador_temp < contador:
        nota = int(input(f"Nota {contador_temp + 1}: "))
        if nota < 0 or nota > 100:
            print("Nota inválida. Debe estar entre 0 y 100.")
            continue
        if nota < promedio:
            menor_promedio_conteo += 1
        contador_temp += 1

    print(f"\nNotas menores al promedio: {menor_promedio_conteo}")

else:
    print("No se ingresaron notas válidas.")