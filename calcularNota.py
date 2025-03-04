
# Actividad 22.1. Calcular la nota de N alumnos, introduciendo su nota teórica (60%) y su nota
# practica (40%). Mostrarlo por pantalla.

cantAlumnos = 0
while cantAlumnos < 1:
    cantAlumnos = int(input("Escribe el número de alumnos:\n"))   
    if cantAlumnos < 1:
        print("Debe ser mayor o igual a 1")

for i in range(cantAlumnos):  # Empezar en 1 para numerar los alumnos
    notaTeorica = -1
    while notaTeorica < 0 or notaTeorica > 10:  # Validar rango entre 0 y 10
        notaTeorica = int(input(f"Introduce la nota teórica del alumno {i+1} (0-10):\n"))
        if notaTeorica < 0 or notaTeorica > 10:
            print("Debes escribir un valor entre 0 y 10.")
    
    notaPractica = -1
    while notaPractica < 0 or notaPractica > 10:  # Validar rango entre 0 y 10
        notaPractica = int(input(f"Introduce la nota práctica del alumno {i+1} (0-10):\n"))
        if notaPractica < 0 or notaPractica > 10:
            print("Debes escribir un valor entre 0 y 10.")
    
    nota = (notaTeorica * 0.6) + (notaPractica * 0.4)
    print(f"El alumno número {i} ha sacado una nota de {nota}")
