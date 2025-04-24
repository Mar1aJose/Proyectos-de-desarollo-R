

num1=int(input("Ingresar Numero:"))
if num1 % 3 == 0 and num1 % 5 == 0:
    print("fizzbuzz")
elif num1 % 3 == 0:
    print("fizz")
elif num1 % 5 == 0:
    print("buzz")
else:
    print(f"El numero es: {num1}")

