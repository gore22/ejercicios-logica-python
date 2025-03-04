# Actividad 16. Hacer un programa donde se pasará un número, dirá si es par o impar, y al final
# preguntará si quiere introducir un nuevo número.

salir = "s"
while salir != "n":
    numero = int(input("Introduce un número\r\n"))    
    if numero % 2 == 0:
        print("Tu número es PAR")
    else:
        print("Tu número es IMPAR")

    salir = input("Quieres introducir un nuevo número (S/N)?\r\n").lower()

print("Juego finalizado")

