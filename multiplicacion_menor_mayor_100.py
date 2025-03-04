# Actividad 06. Algoritmo que haga la multiplicación de dos números que introducirá el usuario. Si el resultado de la multiplicación 
# es mayor de 100 mostrará el mensaje “Mayor de 100”, en caso contrario “Menor de 100”, y si es 100 mostrará “El resultado es 100”.

num1 = int(input('Introduce 1er número\r\n'))
num2 = int(input('Introduce 2do número\r\n'))

resultado = num1*num2

if resultado>100:
    print('Mayor de 100')
elif resultado<100:
    print('Menor de 100')
else:
    print('El resultado es 100')