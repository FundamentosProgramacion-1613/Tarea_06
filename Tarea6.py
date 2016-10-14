#encoding: UTF-8
#Karla Valeria Alcantara Duarte
#Ciclos while 

def contarInsectos():
    insectos = int(input("¿Cuantos insectos recolectaste hoy?"))
    contadorDias = 0
    acumuladorIns = 0
    while insectos<31:
        if acumuladorIns<30:
            acumuladorIns = acumuladorIns + insectos
            faltan = (30-acumuladorIns)
            contadorDias = contadorDias+1
            print("Despues de %d dia(s) de recoleccion has acumulado %d \nTe hacen falta %d insectos."%(contadorDias,acumuladorIns,faltan))
            
            if acumuladorIns>30:
                acumuladorIns = acumuladorIns + insectos
                sobran = (acumuladorIns-30)
                contadorDias = contadorDias+1
                print("Despues de %d dia(s) de recoleccion has acumulado %d \nTe sobran %d insectos.\nFelicidades has llegado a la meta."%(contadorDias,acumuladorIns,sobran))
            
            insectos = int(input("Cuantos insectos recolectaste hoy?"))
            
        elif insectos==30:
            print("Despues de %d dia(s) de recoleccion has acumulado %d \nTe hacen falta %d insectos. \nFelicidades has llegado a la meta."%(contadorDias,insectos,faltan))
        
        insectos = int(input("¿Cuantos insectos recolectaste hoy?"))
            
    while insectos>30:
        acumuladorIns = acumuladorIns + insectos
        sobran = (acumuladorIns-30)
        contadorDias += 1
        print("Despues de %d dia(s) de recoleccion has acumulado %d \nTe sobran %d insectos.\nFelicidades has llegado a la meta."%(contadorDias,acumuladorIns,sobran))
        
        insectos = int(input("¿Cuantos insectos recolectaste hoy?"))     
              
                       
                                
                                         
def encontrarMayor():
    n = int(input("Dame el valor"))
    numeros = 0
    while n!=-1:
        print(n)
        if numeros<n:
            numeros = n
        n = int(input("Dame el valor"))
    print ("El numero mayor es",numeros)
               
                           
def main():
 
    opciones = int(input("¿Que programa quieres? \n1- Contador de insectos \n2- Encontrar en numero mayor \n3- Salir"))
    while opciones<4:
        if opciones==1:
            contarInsectos()
            
            opciones = int(input("Que programa quieres? \n1- Contador de insectos \n2- Encontrar en numero mayor \n3- Salir"))
            
        elif opciones==2:
            encontrarMayor()
            
            opciones = int(input("Que programa quieres? \n1- Contador de insectos \n2- Encontrar en numero mayor \n3- Salir"))
           
        else: 
            print("Adios")
            
main()
        
