# Actividad 05. Algoritmo que haga la suma de los números, solo si los números son mayores de 5, si alguno de los dos números es menor, 
# que muestre un mensaje de texto indicando que no se puede hacer la operación.

def pedirNumero():
    num = int(input('Para sumar, introduce número mayor a 5\r\n'))
    while num<5:
        print('El número es menor a 5 no se puede realizar la suma')
        num = int(input('Introduce 1er número mayor a 5\r\n'))
    return num

num1 = pedirNumero()
num2 = pedirNumero()

resultado =num1+num2
print("de suma es ", resultado )