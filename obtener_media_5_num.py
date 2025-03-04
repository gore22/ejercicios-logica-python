# Actividad 14. Obtener la media de 5 números leídos por teclado. 

resultado = 0
for i in range (0, 5):
    numero = int(input())
    resultado += numero / 5
print(resultado)
