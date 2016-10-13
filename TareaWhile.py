# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Programa con dos funciones donde se aplica el ciclo while

#Función que lleva el registro diario de insectos recolectados
def recolectarInsectos():
    insectosTotal = 0 #acumulador
    dias = 0 #contador
    while insectosTotal < 30:
        insectosDia = int(input("Insectos recolectados hoy"))
        insectosTotal += insectosDia
        dias += 1
        insectosRestantes = 30 - insectosTotal
        print("Después de", dias, "día(s) de recolección has acumulado", insectosTotal, "insectos")
        if insectosTotal <= 30:
            print("Te hace falta recolectar", insectosRestantes, "insectos")
    if insectosTotal > 30:
        print("Te has pasado con", (-1)*insectosRestantes, "insectos")
    print("Felicidades has llegado a la meta")

#Función que encuentra el número mayor de un conjunto de números que ingresa el usuario  
def encontrarMayor():
    mayor = 0
    numero = 0 #Variable que cuando tiene un valor de -1 detendrá el ciclo
    while numero != -1:
        numero = int(input("Introduce un entero positivo o -1 para finalizar"))
        if numero > mayor:
            mayor = numero
    if mayor == 0:
        print("No hay datos para encontrar el valor mayor")
    else:
        print("El mayor es: ", mayor)    
           

def main():
    opcion = 1
    while opcion != 3:
        opcion = int(input("1. Encontrar el mayor\n2. Recolectar insectos\n3. Salir\nTeclea tu opción"))
        if opcion == 1:
            encontrarMayor()
        elif opcion == 2:
            recolectarInsectos()
        elif opcion == 3:
            print("Hasta luego!")
        else:
            print("opción no válida")
main()