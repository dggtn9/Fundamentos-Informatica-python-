
mes=int(input("Ingrese nro de mes"))
if mes >= 1 and mes <= 12:
        if mes == 1:
           print("enero")
        elif mes == 2:
           print("febrero")
        elif mes == 3:
           print("marzo")
        elif mes==4:
           print("abril")
        elif mes == 5:
           print("mayo")
        elif mes == 6:
           print("junio")
        elif mes == 7:
           print("julio")
        elif mes == 8:
           print("agosto")
        elif mes == 9:
           print("septiembre")
        elif mes == 10:
           print("octubre")
        elif mes == 11:
           print("noviembre")
        else:
           print("diciembre")
else:
    print("Es invalido.")
print("fin")