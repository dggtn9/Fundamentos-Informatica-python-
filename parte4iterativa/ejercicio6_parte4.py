"""Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. ¿Cómo cambiaría el
algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?"""

tabla=int(input("Ingrese la tabla de multiplicar que quiere= "))
n=12

for i in range (1,n+1,1):
   print(str(tabla)+"x"+str(i)+"=",i*tabla)
