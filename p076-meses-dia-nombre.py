# Mes, dia, nombre al que corresponda del mes decidido por el usuario 

nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

dias_meses = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]


numero_mes = int(input("Introduce el número del mes (1-12): "))


if 1 <= numero_mes <= 12:
    indice = numero_mes - 1
    print(f"{nombres_meses[indice]}, {dias_meses[indice]} días.")
else:
    print("Número de mes inválido. Debe estar entre 1 y 12.")