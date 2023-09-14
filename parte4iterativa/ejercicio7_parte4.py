"""Leer 10 números enteros e imprimir su promedio, el mayor valor leído y en qué
posición se encontraba. Si se ingresó más de una vez sólo debe informar la primera."""

sumatoria = 0
mayor=0
menor=20000000000000000000
posicion=0
for i in range(0,10):
    numero = int(input("Ingrese nro="))
    sumatoria = sumatoria + numero
    if numero >mayor:
       mayor = numero
       posicion=i+1
    if numero <menor:
        menor=numero
        posicionmenor=i+1


print("Posicion menor es",posicionmenor)
print("Numero menor es", menor)
print("Posicion del mayor es",posicion)
print("El mayor es",mayor)
promedio = sumatoria / 10
print("El promedio es", promedio)





