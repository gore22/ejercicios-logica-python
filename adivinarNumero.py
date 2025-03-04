# Actividad 21. Hacer un pequeño juego donde el usuario tendrá que adivinar un número generado por la aplicación entre 0 y 100. 
# Tendrá 10 intentos, en cada intento si no lo ha acertado se le indicará al usuario un mensaje de si el número es mayor o menor 
# con respecto al que tiene que acertar. 


from random import randint

numeroGenerado = (randint(0, 100)) 

intento = 0
for i in range (0, 10): 
    intento +=1
    print(f"Intento {intento}")
    numero = int(input("Introduce un número:\n"))
    if numero > numeroGenerado:
        print("Incorrecto, el número introducido es mayor.\n")
    elif numero < numeroGenerado:
        print("Incorrecto, el número introducido es menor.\n")
    elif numeroGenerado == numeroGenerado:
        print(f"Correcto, has acertado el número!!{numeroGenerado}")
        break

