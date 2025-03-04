# Actividad 17. Crear un programa que sea una calculadora con un menú donde se podrá seleccionar que tipo de operación se quiere realizar,
# además de una última opción que será para salir de programa. Mientras no se seleccione “Salir”, el programa se repetirá. 

selecion = ''

while selecion != '0':
    print('Selecciona el número de la operación que quieres realizar')
    print('0 - Salir')
    print('1 - Sumar')
    print('2 - Restar')
    print('3 - Multiplicar')
    print('4 - Dividir')
    selecion = input('Ingresa tu opción\r\n')

    if selecion in ['1','2','3','4']:
        num1 = int(input('Introduce 1er número\r\n'))
        num2 = int(input('Introduce 2do número\r\n'))
        if selecion == '1':
                print('La suma total es ', num1 + num2)
        elif selecion == '2':
                print('La restar total es ', num1 - num2)
        elif selecion == '3':
                print('La multiplicación total es ', num1 * num2)
        elif selecion == '4':
                print('La divición total es ', num1 / num2)
    elif selecion == '0':
            print('Finalizado')
    else:
           print('Opción incorrecta')




