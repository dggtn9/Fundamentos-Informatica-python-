"""Diseñar un programa que calcule y muestre el sueldo neto de un empleado en
base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es
casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social:
3%, Sindicato: 3%
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad
y estado civil (1 si es soltero o 2 si es casado). Se debe informar:
(reemplazar los 9 por los valores que correspondan)
Estado Civil: Soltero/Casado
Sueldo básico Antigüedad Descuentos Importe
$ 999.99 99 años + 999.99
Jubilación - 999,99
Obra Social - 999,99
Sindicato - 999,99
------------
Sueldo Neto 999,99"""

# Entrada de datos
sueldo_basico = float(input("Sueldo basico="))
antiguedad = int(input("Antiguedad="))
estado_civil = int(input("Estado civil (1 soltero, 2 casado="))

# Acciones
if estado_civil == 1: #SOLTERO
    porcentaje = 0.05
else:
    porcentaje = 0.07

incremento = sueldo_basico + ((sueldo_basico * porcentaje) * antiguedad)

descuento_jubilacion = sueldo_basico * 0.11
obra_social = sueldo_basico * 0.03
sindicato = sueldo_basico * 0.03

neto = incremento - descuento_jubilacion - obra_social - sindicato

print("Sueldo Neto", neto)


























