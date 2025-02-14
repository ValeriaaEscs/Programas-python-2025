# Dar el numeros de horas para calcular de día, minutos y segundos 

horas = int(input("Ingrese la cantidad de horas: "))

# Cálculos
dias = horas // 24
minutos = horas * 60
segundos = minutos * 60

# Mostrar resultados
print("Equivalente en días:", dias)
print("Equivalente en minutos:", minutos)
print("Equivalente en segundos:", segundos)