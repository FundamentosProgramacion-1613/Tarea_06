#Oswaldo Morales Rodriguez A01378566
#Realiazr la funcion que el usuario pida
#Encoding: UTF-8

def funcionInsectos():
    dia=0
    insectosTotales=0
    insectos=int(input("Numero de insectos capturados hoy"))
    while insectosTotales<30:
        dia+=1
        insectosTotales+=insectos
        if insectosTotales<30:
            insectosFaltantes=30-insectosTotales
            print("Han pasado", dia, "dia(s), desde que empezaste, te faltan", insectosFaltantes)
        elif insectosTotales==30:
            print("Pasaron",dia, "dias para que cumplieras tu meta")
        elif insectosTotales>30:
            sobrante=insectosTotales-30
            print("Pasaron",dia,"dias, para cumplir tu meta, te pasaste por",sobrante)
        insectos=int(input("Numero de insectos capturados hoy"))
            
def funcionMayor():
    numero=int(input("Deme un numero"))
    numeroA=0
    while numero>0:
        print(numero)
        if numeroA<numero:
            numeroA=numero
        numero=int(input("Deme un numero"))
    print("El mayor de la serie es", numeroA)
    

def main():
    opcion=0
    while opcion!=3:
        opcion=int(input("1. Saber la cantidad de insectos faltantes \n2. Encontrar el mayor \n3. Salir."))
        if opcion==1:
            numeroInsectos=int(input("Insectos capturados hoy"))
            resultado=funcionInsectos()
        elif opcion==2:
            funcionMayor()
        elif opcion==3:
            print("ADIOS")
        else:
            print("Escoja un numero existente")
            
main()