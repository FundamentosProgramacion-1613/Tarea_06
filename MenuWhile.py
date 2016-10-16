#encoding: UTF-8
#Marlon Brandon Velasco Pinello, A01379404
#Tarea 6

#Definimos la funcion para conocer los insectos 
def conocerCantInsectos():
    insectos=0
    dias=0
    #generamos el ciclo para que el programa se salga cuando deba
    while insectos<30:
        #esta funcion si pide datos e imprime ya que hacerlo diferente es muy complicado
        insectosDia=int(input("Insectos recolectados hoy"))
        if insectosDia>=0:
            insectos+=insectosDia
            dias+=1
            print("Despues de %d dia(s),has acumulado %d"%(dias,insectos))
            if insectos<=30:
                print("Te hace falta recolectar %d insectos"%(30-insectos))
            else:
                print("Te has pasado con %d insectos"%(insectos-30))
            if insectos>=30:
                print("Felicidades has llegado a la meta")

#definimos la funcion para calcular el numero mayor
#aqui si se pudo hacer sin imprimir ni pedir datos
def calcularMayor(numeroN,numeroMayor,numeroX):
    if numeroN>=numeroX:
        numeroMayor="El mayor es: "+str(numeroN)
    return numeroMayor
    
#funcion principal main
def main():
    #se hace el while True para no darle un valor a la variable inicial
    while True:
        #se pide el menu
        menu=int(input("1. Encontrar mayor\n2. Recolectar insectos\n3. Salir\nTeclea tu opcion"))
        if menu==1:
            numeroMayor="No hay datos para comparar el numero mayor"
            numeroX=0
            while True:
                numeroN=int(input("Ingresa el numero Positivo que quieras comparar, para salir ingresa -1"))
                if numeroN>-1:
                    numeroMayor=calcularMayor(numeroN,numeroMayor,numeroX)
                    if numeroN>numeroX:
                        numeroX=numeroN
                elif numeroN==-1:
                    break
            print(numeroMayor)
                
        elif menu==2:
            conocerCantInsectos()
        #si la opcion es salir se rompe el ciclo y termina el programa
        elif menu==3:
            break
        #en caso de no elegir una opcion se da una opcion invalida
        else:
            print("Ingresa una opcion valida")

#hacemos que se llame la funcion main            
main()
            