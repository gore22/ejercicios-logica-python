# Actividad 19. Modularizar la actividad anterior.

def sumar(a, b):
    print(f"La suma total es {a + b}")

def restar(a, b):
    print(f"La resta total es {a - b}")

def dividir( a, b):
    print(f"La divición total es {a / b}")

def multiplicar(a, b):
    print(f"La multiplicación total es {a * b}")

def menu():
    opciones = [
        '0 - Salir',
        '1 - Sumar',
        '2 - Restar',
        '3 - Multiplicar',
        '4 - Dividir'
    ]
    opcion = -1
    
    while not (0 <= opcion <= 4):
        aprendiendo = f'Selecciona el número de la operación que quieres realizar:\n' + '\n'.join(opciones)
        print(aprendiendo)
        opcion = int(input('Ingresa opcion\n'))

        if opcion < 0 or opcion > 4:
            print(f"error la opción {opcion} no es valida\n")
    
    return opcion



opcion_seleccionada = 0

while 0 <= opcion_seleccionada  <= 4:
    opcion_seleccionada = menu()
    print(f'La opción seleccionada fue: {opcion_seleccionada}')
    if opcion_seleccionada == 0:
        print("Hasta pronto")
        break
    num1 = int(input('introduce 1er numero\n'))
    num2 = int(input('introduce 2do numero\n'))
    
    if opcion_seleccionada == 1:
        sumar(num1,num2)
    elif opcion_seleccionada == 2:
        restar(num1, num2)
    elif opcion_seleccionada == 3:
        multiplicar(num1, num2)
    elif opcion_seleccionada == 4:
        dividir(num1, num2)