# operadores unitario
unitario=not True  # unitario, not convierte el valor a lo inverso, True lo convierte en false, y false en true

# operadores binarios

binario= 2+2
binario2= 1<2

# operadores ternarios

precio=5000

# si el precio es mayor a 10000 entonces indicar que es caro, en caso contrario, indicar que es economico

if precio>10000:
    print("El precio es caro")
else:
    print("el precio es economico")
#     condicion correcta     condicion         si la condicion no se cumple
print("el precio es caro" if precio>10000 else "el precio es economico")

nombre1="bob"
nombre2="peter"

print("son iguales" if nombre1==nombre2 else "no son iguales")


