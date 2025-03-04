# Actividad 08. Crear programa, donde introducimos dos números y después nos sale un menú, indicando la operación matemática que queremos 
# realizar, mostrando finalmente el resultado de esta, y en caso de seleccionar una opción que no este contemplado, mostrar un mensaje 
# de opción no valida.


menu =['sumar', 'restar', 'multiplicar', 'dividir','salir']
operacion =""
while operacion != "salir":
    print(menu)
    
    num1 = int(input('Introduce 1ER número\r\n'))
    num2 = int(input('Introduce 2do número\r\n'))
    operacion =input('Que operación deseas realizar\r\n')
    match operacion:
        case 'sumar':
            print('La suma total es ', num1 + num2)
        case 'restar':
            print('La resta total es ', num1 - num2)
        case 'multiplicar':
            print('La multiplicación total es ', num1 * num2)
        case 'dividir':
            print('La dividición total es ', num1 / num2)
        case 'salir':
            print('Adios')
        case _:
            print('Opción no valida')