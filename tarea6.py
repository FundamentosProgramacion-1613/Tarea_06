#encoding: UTF-8
#Autor: José Javier Rodríguez Mota
#Descripción: Recolección de objetos y seleccionar mayor

#Inicio

#Definimos recolectar insectos
#Opción 2
def recolectarInsectos():
    
    #Iniciamos contadores
    numinsectos=0
    contador=0
    
    #Hacemos un loop
    while numinsectos<30:
        
        #Pedimos valores de entrada y alteramos nuestras variables
        numinsectos+=int(input("Número de insectos recolectados hoy"))
        contador+=1
        
        #Detenemos el código en cuanto el usuario ingresa números erróneamente
        if numinsectos<0:
            print("No puedes tener un número negativo de insectos")
            return False
        
        #Imprimimos lo que lleva actualmente    
        print("Después de %d día(s) has recolectado %d insectos."%(contador,numinsectos))
        
        #Revisamos si sobran o faltan para imprimir lo correspondiente
        if numinsectos<=30:
            faltante=30-numinsectos
            print("Te hace falta recolectar %d insectos."%faltante)
        elif numinsectos>30:
            restante=numinsectos-30
            print("Te has pasado con %d insectos."%restante)
    
    #Termina el loop si y sólo si llegó a la meta
    print("Felicidades has llegado a la meta.")         

#Definimos encontrar mayor
#Opción 1
def encontrarMayor():

    #Establecemos valores de inicio
    numero2=-1
    numero=int(input("Ingresa un número que quieras revisar.\n Pon -1 para salir"))
    
    #Iniciamos loop para encontrar los mayores
    while numero!=-1:
        
        #Revisamos qué número es el mayor
        if numero>numero2:
            numero2=numero
        #Pedimos nuevamente otro valor..    
        numero=int(input("Ingresa un número que quieras revisar.\n Pon -1 para salir"))   
    
    #Revisamos que el loop se haya realizado al menos en una ocasión
    if numero2==-1:
        numero2=False
    
    #Regresamos el resultado    
    return numero2

#Definimos nuestra función main
def main():

    #Iniciamos el menú
    opcion=int(input("1. Encontrar mayor\n2. Recolectar insectos\n3.Salir\nTeclea tu opción"))
    
    #Loop de menú
    while opcion !=3:
        
        #Encontrar el Mayor
        if opcion==1:
            mayor=encontrarMayor()
            
            #Revisamos que el resultado haya sido válido
            if mayor==False:
                print("No hay datos para encontrar el valor mayor")
            else:
                print("El mayor es: %d"%mayor)
        
        #Recolectar insectos
        if opcion==2:
            recolectarInsectos()
            
        #Volvemos a solicitar la opción a valorar
        opcion=int(input("1. Encontrar mayor\n2. Recolectar insectos\n3.Salir\nTeclea tu opción"))

#Corremos el código
main()
#Fin