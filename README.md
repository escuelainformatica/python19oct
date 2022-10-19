# python19oct
Ejercicio de la clase

## condición usando if

```python
numero1=1
numero2=2
if numero1 < numero2:
    print("numero1 es menor")
else:
    print("numero1 es mayor o igual")
```

# comparaciones (binarias)

* == igualdad
* != no son iguales
* < menor a
* \> mayor a
* <= menor o igual
* \>= mayor o igual

# lógica

* and (si lógico)

```python
numero1=1
numero2=2
numero3=3
# quiero comparar si los 3 son iguales
if numero1==numero2 and numero2==numero3:
    print("los tres son iguales")
# otra forma
if numero1==numero2:
    if numero2==numero3:
        print("los tres son iguales")
```

* or (o lógico)

```python
numero1=1
numero2=2
numero3=3
# quiero comparar si alguno de los valores son iguales
if numero1==numero2 or numero1==numero3 or numero2==numero3:
    print("algunos son iguales")
```



# compara varios valores con match

```python
# otra manera
if numero == 1:
    print("uno")
elif numero == 2:  # elif es un else mas un if.
    print("dos")
elif numero == 3:
    print("tres")
else:
    print("otro valor")

# otra manera switch/case
match numero:
    case 1:
        print("uno")
    case 2:
        print("dos")
    case 3:
        print("tres")
    case _:  # si no se cumple otra condicion
        print("otro valor")
```
