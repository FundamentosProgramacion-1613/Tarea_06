#encoding: UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descripción: Tarea While

#Inicio

def colectarInsector():
    recolectados=int(input("Cuantos insectos has recolectado?"))
    dia=0
    otros=0
    count=0
    while recolectados<30:
        recolectados=recolectados+otros
        dia=dia+1
        if recolectados<30:
            restantes=30-recolectados
            print("En %d dias, has conseguido %d insectos. Hacen falta %d" %(dia,recolectados,restantes))
            otros=int(input("Cuantos insectos has recolectado?"))
        elif recolectados>=30:
            sobrantes=recolectados-30
            print("En %d dias, has conseguido %d insectos. Has recolectado %d de mas" %(dia,recolectados, sobrantes))      
        count=count+1
    if count==0:
        dia=dia+1
        sobrantes=recolectados-30
        print("Felicidades, en %d dia has conseguido %d insectos. Has recolectado %d de mas" %(dia,recolectados, sobrantes))
    
def encontrarMayor():
    valor=int(input("Introduce un valor, si introduces -1 el programa terminara"))
    mayor=0
    count=0
    while valor!=-1:
        if valor>mayor:
            mayor=valor
        valor=int(input("Introduce otro valor"))
        count=count+1
    if count==0:
        print("No hay valores para comparar")
    elif count>0:
        print("El mayor valor es: %d" %mayor)
    
def main():
    print ("""
    Bienvenido, selecciona que programa deseas ejecutar:
    
    1. Insectos recolectados
    2. Valor mayor de un conjunto
    0. Salir
    """)
    opcion=int(input("Elige el programa que deseas utilizar"))
    while opcion!=0:
        if opcion==1:
            colectarInsector()
            opcion=int(input("""
    Que otra accion deseas realizar?
    
    1. Insectos recolectados
    2. Valor mayor de un conjunto
    0. Salir
    """))
        
        elif opcion==2:
            encontrarMayor()
            opcion=int(input("""
    Que otra accion deseas realizar?
    
    1. Insectos recolectados
    2. Valor mayor de un conjunto
    0. Salir
    """))
        else:
            print("Valor incorrecto")
            opcion=int(input("""
    Que otra accion deseas realizar?
    
    1. Insectos recolectados
    2. Valor mayor de un conjunto
    0. Salir
    """))
        
main()

#Fin
