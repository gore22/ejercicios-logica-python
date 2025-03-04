# Actividad 18. Se tiene el siguiente menú de un restaurante de bocadillos. Diseñar un algoritmo capaz de leer el número de unidades 
# consumidas de cada alimento ordenado y calcular la cuenta total. Vamos a suponer que estos precios son fijos, es decir, que son constantes. 
# RODUCTO PRECIO: Bocadillo de jamón 1,5 €, Refresco 1,05 €, Cerveza 0,75 €

bocadillo = 1.5
refresco = 1.05
cerveza = 0.75
total = 0

cantBocadillo = int(input("introduce cantidad de Bocadillo de jamón\n"))
cantRefresco = int(input("Introduce cantidad de refresco\n"))
cantCerveza = int(input("Introduce cantidad de cerveza\n"))

total = (cantBocadillo*bocadillo)+(cantCerveza*cerveza)+(cantRefresco*refresco)
print(total)


