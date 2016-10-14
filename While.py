#encoding: UTF-8
#Autor: Adrian Tellez
#Programas con while


#Calcular cantidad de insectos recolectados, dias que han pasado, etc.
def calcularInsectos():
    insectos = 0
    dias = 0
    insectost = 0
    while insectost < 30: 
        insectos = int(input("Insectos recolectados hoy"))
        insectost += insectos
        falta = 30 -  insectost
        dias += 1
        print ("Despues de",dias,"dia(s) de recoleccion, has acumulado",insectost,"insecto(s)")
        if insectost < 30:
            print ("Te faltan",falta,"insectos")
        if insectost == 30:
            print ("Te faltan",falta,"insectos")
    if insectost > 30:
        sobra = falta * (-1)
        print ("Te has pasado por",sobra,"insecto(s)")
    print ("Felicidades has llegado a la meta")

#Buscar el numero mas grande 
def buscarGrande():
    m = 0
    n = 0
    while n >= 0:
        n = int(input("Escoge un numero mayor a 0 o -1 para salir"))
        print (n)
        if m < n:      
            m = n
    if m <= 0:
        print ("No hay datos para encontrar el valor mas grande")
    else:
        print ("El numero mas grande es:", m)

#Menu de las funciones
def main():
    opcion = 0
    while opcion != 3:
        opcion = int(input("Elige tu opcion:\n1.- Recolección de insectos\n2.- Encontrar el numero mas grande\n3.- Salir"))
        if opcion == 1:
            calcularInsectos()
        elif opcion == 2:
            buscarGrande()
        elif opcion == 3:
            print ("Adios\nBuen dia\n:)")
        else:
            print("Escoge una opcion colecta")

main()
