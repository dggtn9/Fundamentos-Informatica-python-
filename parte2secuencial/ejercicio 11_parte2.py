#Ejercicio 11
"""Un banco necesita para sus cajeros automáticos un programa que lea
una cantidad de dinero e imprima a cuántos billetes equivale, considerando
que existen billetes de $1000, $500, $100, $50, $10, $5 y $1.
Desarrollar dicho programa de tal forma que se minimice la cantidad de
billetes entregados por el cajero."""

monto=int(input("Ingrese valor="))
billetes_1000=(monto//1000)
resto=(monto%1000)
billetes_500=resto//500
resto=resto%500
billetes_100=(resto//100)
resto=resto%100
billetes_50=(resto//50)
resto=resto%50
billetes_10=(resto//10)
resto=resto%10
billetes_5=(resto//5)
resto=resto%5
billetes_1=(resto//1)
resto=resto%1

print("Billetes de mil",billetes_1000)
print("Billetes de quinientos",billetes_500)
print("Billetes de cient",billetes_100)
print("Billetes de cincuenta",billetes_50)
print("Billetes de diez",billetes_10)
print("Billetes de cinco",billetes_5)
print("Billetes de uno",billetes_1)

print("No olvide su tarjeta")




