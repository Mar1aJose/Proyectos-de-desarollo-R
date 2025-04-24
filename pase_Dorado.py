edad=int(input("Ingresa tu edad"))
pase=(input("Tienes pase dorado: Si/No"))

if edad >= 18 and edad <=25:
    pase (input("Tienes pase dorado? Si/No:"))
    if pase == "no":
      print("Si no tienes pase dorado, pero tienes la edad, puedes ingresar!")
    else:
      print("Tienes pase dorado y tienes la edad, Bienvenido al club!")
elif edad >25 and edad <100:
    pase = ("Tienes pase dorado:? Si/No")
    if pase == "Si":
       print("Tienes la edad y pase dorado, Bienvenido al club")
    else:
       print("Aunque tienes la edad indicada, no cuentas con el pase dorado, no puedes ingresar")
else:
   print("No cuentas con la edad requerida para ingresar al club")