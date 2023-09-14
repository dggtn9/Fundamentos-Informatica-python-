"""En los ejercicios siguientes es necesario probar el programa con al menos tres conjuntos
de datos de entrada, detallando los resultados obtenidos en cada caso.
Ejercicio 1: Leer números que representan edades de un grupo de personas, finalizando la
lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18
años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos.
Descartar valores que no representan una edad válida. (Se considera válida una
edad entre 0 y 100)."""

suma_menos18=0
suma_mas18=0

for i in range (1,100):
    if i<18:
        i=+1
        suma_menos18=suma_menos18+i
    if i>18:
        i=+1
        suma_mas18=suma_mas18+i
    if i ==-1:
        print ("fin")
print("Son menores de edad",suma_menos18,"personas")
print("Son mayores de edad", suma_mas18, "personas")
print("Promedio de edad del grupo es",(suma_mas18+suma_menos18)/2)
