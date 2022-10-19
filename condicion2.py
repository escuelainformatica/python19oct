# ingresar un producto y validar que el producto esta correcto
print("ingrese nombre:")
nombre=input()
print("ingrese precio:")
precio=int(input())

prod={"nombre":nombre,"precio":precio}
print(prod)

# que es valido?
# 1) el precio no puede ser 0 o negativo
# 2) el nombre no puede ser vacio.
if prod['precio']<=0:
    print("el producto es incorrecto")
else:
    print("el producto es correcto")

if prod['nombre']=='':
    print("el producto es incorrecto")
else:
    print("el producto es correcto")

if prod['precio']>0 and prod['nombre']!='':
    print("el producto es correcto")
else:
    print("el producto es incorrecto")
