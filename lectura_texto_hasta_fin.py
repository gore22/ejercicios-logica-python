# Actividad 11. Crea un algoritmo que leerá texto pasado por la pantalla, continuamente hasta 
# que escribamos “Fin”. Todo el texto se irá concatenando. Al finalizar el ciclo, mostrará el texto final.

cadena = " "

while True:
    texto = input("Escribe un texto, escribe 'fin' para terminar\r\n")
    if texto.lower() == "fin":
        break 
    cadena += texto + " "
print(cadena)
