#encoding: UTF-8
#Nombre de el Alumno: Manuel Alejandro Bracho Mendoza
#Mátricula: A01378897
#Tarea 6

from math import *

def contarInsectos():
    dias = 1
    insectos = (int(input("Insectos recolectados hoy")))
    while insectos < 30 :
        restante = 30-insectos
        print ("Después de" ,dias,"día(s) de recolección has acumulado", insectos)
        print ("Te hace falta recolectar",restante,"insectos")
        dias+=1
        insectosSegundoDia = (int(input("Insectos recolectados hoy")))
        insectos=insectosSegundoDia + insectos
        if insectos == 30:
            print ("Despues de" ,dias,"día(s) de recolección has acumulado", insectos)
            print ("te hace falta recolectar 0 insectos \nFelicidades has llegado a la meta")
    if insectos >= 31:
        print ("Despues de",dias,"día(s) de recolección has acumulado", insectos)
        print ("Te has padado con", insectos - 30 ,"insectos \nFelicidades has llegado a la meta")
def calcularNumero():
    numero = (int(input("Ingrese los numeros, para salir de el colector de números escriba -1")))
    if numero <= -1:
        print("no hay datos para encontrar el número mayor.")
    else:
        acumulador = 0 
    
        while numero != -1:
            if acumulador < numero:
                acumulador = numero
            numero = (int(input("ingrese el número, recuerda que tecleando -1 indicas que terminas de escribir")))        
        print("El mayor es", acumulador) 
def main():
    opcion = 0
    while opcion != 3:
        opcion = (int(input("1°.- Contador de Insectos \n2°.- Encontrar el número mayor \n3°.- Salir")))
        if opcion == 1:
            contarInsectos()
        elif opcion == 2:
            calcularNumero()
        elif opcion == 3:
            print("hasta pronto")
        else:
            print("teclea una opción válida")
main()            
            
        
        
        
        
        