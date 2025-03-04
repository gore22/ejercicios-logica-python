# Actividad 07. Usando la estructura "match”, leer un número y mostrar un mensaje de si es par o impar.

numero = int(input('Introduce un numero\r\n'))

match numero % 2:
    case 0:
        print('El número', numero,'es par')
    case 1:
        print('El número', numero,'es impar')