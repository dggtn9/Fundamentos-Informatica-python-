#Ejercicio 9
"""Una inmobiliaria paga a sus vendedores un salario de $50000, más una
comisión de $5000 por cada venta realizada, más el 5% del valor de las
ventas. Realizar un programa que imprima el número del vendedor y el
salario que le corresponde en un determinado mes. Se leen el número
del vendedor, la cantidad de ventas que realizó y el valor total de las
mismas"""

salario=50000
comision_x_venta=5000
comision_x_valordelaventa=5

numero_de_vendedor=int(input("Inserte el numero de vendedor"))
cantidad_ventas=int(input("Inserte cantidad de ventas que realizó"))
valor_total_ventas=int(input("Inserte valor total de las mismas"))

salario_final=salario + (comision_x_venta * cantidad_ventas) + ((comision_x_valordelaventa * valor_total_ventas)/100)
print("vendedor:" + str(numero_de_vendedor) + " debe cobrar: " + str(salario_final))

