""" Ingresar números, hasta que la suma de los números pares supere 100. Mostrar
cuántos números se ingresaron en total."""

sumatoria=0
cont=0
while sumatoria<=100:
     nro=int(input("ingrese un numero"))
     cont=cont+1
     if nro % 2 == 0:
        sumatoria=nro+sumatoria

print("cantidad de nros que se ingresaron:",cont)


