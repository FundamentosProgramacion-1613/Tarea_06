#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran    A01371424
#Tarea 6

def calcularInsectos(a):
    dias=0
    insectos=0
    faltantes=0
    while insectos<30:
        a = int(input("Numero de Insectos cazados"))
        dias +=1
        insectos=insectos+a
        faltantes=30-insectos
        print("Despues de ",dias,"dias tienes",insectos,"insectos, te faltan",faltantes,"insectos para llegar a la meta")
        if insectos>=30:
            faltantes=faltantes*-1
            print("Despues de ",dias,"dias recolectaste",insectos,"insectos, te faltan",faltantes,"insectos para llegar a la meta")
            print("Felicidades llegaste a la meta",faltantes,"insectos restantes")
    
def calcularNumeros():
    numActual=0
    numAnterior=0
    numActual= int(input("Ingresa un numero"))
    if numActual== -1:
        print ("No hay valoes")
    while numActual!= -1:
        numActual= int(input("Ingresa un numero"))
        print (numActual)
        if numActual>numAnterior:
            numAnterior=numActual
        if numActual== -1:
            print ("El numero mayor es:",numAnterior)
        

def main():
    numProblema=0
    while numProblema!=3:
        numProblema= int(input("Seleccione el problema \n (1) calcularInsectos \n (2) calcularNumeros \n (3) Salir del Programa")) 
        if numProblema== 1:
            a = int(input("¿Cuantos insectos has cazado?"))
            calcularInsectos(a)
        if numProblema== 2:
                calcularNumeros()
        if numProblema<=0 or numProblema>=4:
            print ("Por favor ingrese un numero del 1 al 3")
        if numProblema== 3:
            print ("Gracias")
        
main()