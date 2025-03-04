# Actividad 01. Crear un programa donde se pidan dos números, que usaremos para realizar comparaciones con los siguientes 
# operadores relacionales.

num1 = int(input("Introduce 1er número \n\r"))
num2 = int(input("Introduce 2do número \n\r"))
operadores = ["==", "<", ">", ">=", "<="]

for operador in operadores:
    print(f"{num1}  {operador} {num2}: {eval(f'{num1} {operador}{num2}')}, {num2}  {operador} {num1}: {eval(f'{num2}{operador}{num1} ')}")
