numero = 3  # "tres"

# condicional anidado

if numero == 1:
    print("uno")
else:
    if numero == 2:
        print("dos")
    else:
        if numero == 3:
            print("tres")
        else:
            print("otro numero")

# varias condiciones

if numero == 1:
    print("uno")
if numero == 2:
    print("dos")
if numero == 3:
    print("tres")

# otra manera
if numero == 1:
    print("uno")
elif numero == 2:
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
