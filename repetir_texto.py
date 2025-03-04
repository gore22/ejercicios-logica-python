
# Actividad 12. Introducir un texto, y un número. Escribir el texto tantas veces como se ha indicado en el número.

texto = input('Introduce un texto\r\n')
numero = int(input("Introduce un número\r\n"))

while numero < 0:
    print(texto)

for _ in range(numero):
    print(texto)
