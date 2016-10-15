#encoding: UTF-8
#Autor: Luis Martín Barbosa Galindo A01337485
# Tarea 6

def atraparInsectos():
    dias = 0
    ins = 0
    insectos = int(input("¿Cuantos insectos atrapaste hoy?"))
    ins += insectos
    while ins < 30 :
        dias += 1
        falta = 30 - ins
        print("Despues de",dias,"dias has recolectado:",ins,"insectos, y te faltan:",falta,"insectos.")
        insectos = int(input("Cuantos insectos atrapaste hoy?"))
        ins += insectos
        if ins == 30 and falta == 0:
            dias +=1
            print("Despues de",dias,"dias has recolectado los 30 insectos, felicidades.")
        elif ins >= 31 and falta != 0:
            dias +=1
            print("Vaya te has pasado, en",dias,"dias has recolectado :",ins,"insectos, y te pasaste por:",falta,"insectos")    
def encontrarNúmeroMayor():
    num = int(input("Dame un número, si quieres terminar con el programa marca -1"))
    if num <= -1 :
        print("No lo puedo hacer, adios")
    elif num > -1 :
        mayor = 0
        while num > -1:
            if mayor < num:
                mayor = num
            num = int(input("Dame otro número, si quieres terminar con el programa marca -1"))
        print("De todos los números el mas grande fue :",mayor)

def main():
    print("1.- Recolectando insectos")
    print("2.- El número mayor")
    print("3.- Salir")
    opcion = int(input("Dime que funcion queires usar"))
    if opcion == 1 :
        atraparInsectos()
    elif opcion == 2:
        encontrarNúmeroMayor()
    else:
        print("Vuelve pronto")

main()