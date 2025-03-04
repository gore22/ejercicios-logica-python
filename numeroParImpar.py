# Actividad 03. Crear un programa que lea un número y diga que es cierto si es mayor de 20 o es impar.

numero =int(input('Introduce un número\r\n'))

print('El número es verdadero' if numero>=20 or numero % 2 != 0  else 'El número es falso')

