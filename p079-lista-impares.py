# Lista de impares que desea el usuario; sumarlos y el  promedio de los numeros impares 

n = int(input("¿Cuántos números impares deseas? "))


impares = []
num = 1
while len(impares) < n:
    impares.append(num)
    num += 2


print("\nLista de impares:", impares)


suma_total = sum(impares)
promedio = suma_total / len(impares)

print(f"\nSuma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")


div3 = []
for valor in impares:
    if valor % 3 == 0:
        div3.append(valor)

suma_div3 = sum(div3)
print(f"\nNúmeros divisibles entre 3: {div3}")
print(f"Suma de ellos: {suma_div3}")


buscar = int(input("\n¿Número a buscar en la lista? "))
if buscar in impares:
    posicion = impares.index(buscar)
    print(f"{buscar} está en la lista, en la posición {posicion}.")
else:
    print(f"{buscar} no está en la lista.")