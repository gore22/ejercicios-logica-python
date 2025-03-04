            
# Actividad 22.2.(Modularizar) Calcular la nota de N alumnos, introduciendo su nota teórica (60%) y su nota
# practica (40%). Mostrarlo por pantalla.

def pedirNota(cadena, alumno):
    nota = -1
    while (nota < 0 or nota >10):
        nota = int(input(f"Introduce la nota {cadena} del alumno {alumno+1}\n"))    
        if (nota < 0 or nota > 10):
            print("Debes escribir un valor entre 0 y 10")
    return nota
    

cantAlumnos= int(input("Escribe el numero de alumnos\n"))

for i in range(cantAlumnos):
    nAlumno =+ i
    notaPractica = pedirNota("practica", nAlumno)
    notaTeorica = pedirNota("teorica", nAlumno)
    nota = (notaTeorica*0.6) + ( notaPractica*0.4)
    print(f"El alumno numero {nAlumno} tiene una nota de {nota}")

#print("Debe ser mayor o igual a 1")
