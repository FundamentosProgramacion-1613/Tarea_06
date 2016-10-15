#encoding: UTF-8
#By Diego Perez
#Bitacora de Insectos, Mayor Valor, en Menu

#ENCONTRAR MAYOR VALOR; USAR CONTADOR PARA VERIFICAR QUE EXISTEN MAS DE 1 DATO
def mayorNumero():
    n = 0
    nDatos = 0
    nMayor = 0
    while (n != - 1):
        n = int(input("Escriba un valor"))
        nDatos +=1
        if (n > nMayor):
            nMayor = n  
    else:
    #VERIFICAR QUE EXISTE MAS DE 1 DATO
        if (nDatos == 2):
            nMayor = "No hay datos para encontrar el valor mayor"
        else:
            nMayor = "El numero mayor es: "+str(nMayor)       
        return nMayor
        
#Recoleccion de Insectos
def bitacoraInsectos():
    dias = 0
    insectos = 0
    insectosRec = 0
    insectosPA = 30
    
    while (insectos < insectosPA):
        insectosRec = int(input("Insectos Recolectados hoy"))
        insectos += insectosRec
        dias +=1
        #IMPRIMIR ESO SI NO SE HA LLEGADO A LA META
        if (insectos < insectosPA):
            print("Despues de",dias,"dia(s),has acumulado",insectos,"insectos")
            print("Te hace falta recollectar",insectosPA-insectos,"insectos")
        
    else:
    #IMPRIMIR ESO SI sE HA LLEGADO A LA META
        print("Despues de",dias,"dia(s),has acumulado",insectos,"insectos")
        #IMPRIMIR ESO SI SE SOBREPASO LA META
        if (insectos > insectosPA):
            print("Te has pasado con",insectos-insectosPA,"insecto(s)")
        else:
            print("Te hace falta recollectar",insectosPA-insectos,"insecto(s)")
        print("Felicidades, has llegado a la meta")
    


def main():
    num = int(input("""
    1. Encontrar Mayor
    2. Recolectar Insectos
    3. Salir"""))
    
    while (num==1) or (num ==2): #PARA EVITAR QUE SE CICLE EL PROGRAMA
        if (num == 1):
            nMayor = mayorNumero()
            print(nMayor)
            num = int(input("""
            1. Encontrar Mayor
            2. Recolectar Insectos
            3. Salir"""))
        if (num == 2):
            bitacoraInsectos()
            num = int(input("""
            1. Encontrar Mayor
            2. Recolectar Insectos
            3. Salir"""))
main()