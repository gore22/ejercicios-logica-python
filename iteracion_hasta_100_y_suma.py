# Actividad 09. Crear un programa, donde leerá un número y hará una iteración hasta 100, mostrándolo en pantalla y 
# sumando sus valores donde finalmente mostrará el resultado.

cont = int(input('Introduce un número\r\n'))
resultado =0
while cont <100:
    print('número vale ', cont)
    cont += 1
    resultado += cont 

print('Resultado de la suma es ', resultado)