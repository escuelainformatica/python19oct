comparar = 1 < 2  # comparar es un booleano, puede tener True o False

print(comparar)

if comparar:
    print("es verdadero")

# quiero ingresar un cliente, y validar que el cliente es correcto.
# que es correcto?
# nombre no puede ser vacio
# el apellido no puede ser vacio
# la edad, tiene que ser mayor a 18.
# la deuda, no puede ser negativo, y no puede ser mayor a 1000

cli = {"nombre": "john", "apellido": "doe", "edad": 33, "deuda": 233}

# condiciones en un solo if
if (cli["nombre"] == ""
        or cli["apellido"] == ""
        or cli["edad"] < 18
        or cli["deuda"] < 0
        or cli["deuda"] > 1000):
    print("el cliente no es correcto")
else:
    print("el cliente es correcto")

# flag o bandera.
valido=True
if cli["nombre"]=="":
    valido=False
if cli["apellido"]=="":
    valido=False
if cli["edad"]<18:
    valido=False
if cli["deuda"]<0 or cli["deuda"]>1000:
    valido=False

if valido:
    print("el cliente es valido")
else:
    print("el clientes es invalido")
