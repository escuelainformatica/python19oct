num1=555
num2=33
num3=3

if num1>num2:
    mayor=num1
else:
    mayor=num2

if mayor<num3:
    mayor=num3

print(f"el numero mayor es {mayor}")

if num1>num2 and num1>num3:
    mayor=num1
elif num2>num1 and num2>num3:
    mayor=num2
else:
    mayor=num3
