p1=int(input("Nota parcial 1="))
p2=int(input("Nota parcial 2="))

if p1<=10 and p2<=10:
    if p1>=7 and p2>=6:
      print("Promociona")
    elif p1>=4 and p2>=4:
      print("aprueba")
    elif p1<4 and p2<4:
      print("recursa")
    else:
      print("debe recuperar")
else:
    print("error")
print("fin")