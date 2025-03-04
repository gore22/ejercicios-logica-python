# Actividad 20. Sobre el importe introducido por el usuario, calcular el IVA (21%). Mostrar
# cuanto se incrementa el precio, y el precio total con el IVA.

importe = int(input("Introduce importe\n"))

total = importe * 1.21
iva = total-importe
print(f"El importe sin  iva es: {importe}€")
print(f"Total del Iva: {iva}€")
print(f"Total con Iva: {total}€")
