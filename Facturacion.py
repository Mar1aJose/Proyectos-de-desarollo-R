
nProducto=input("Ingresa nombre del producto: ")
pProducto=int(input("Ingresa el precio: "))
cProductos=int(input("Ingresa la cantidad de productos: "))

while True:
    try:
        descuento_porcentaje = float(input("Ingrese el porcentaje de descuento (0-100, y 0 para si no hay descuento): ") or 0)
        if 0 <= descuento_porcentaje <= 100:
            break
        else:
            print("El porcentaje de descuento debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para el descuento.")

#costo sin descuento

if 0 == descuento_porcentaje:
   print (f"el valor sin descuento es {pProducto * cProductos}")


#monto con descuento

if descuento_porcentaje >= 1 and descuento_porcentaje <= 100:
    print(f"su descuento {descuento_porcentaje}% da como resultado que {(pProducto * cProductos)*descuento_porcentaje/100}")



