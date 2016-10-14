#encoding: UTF-8
#Autor: Jesus Perea
#Tarea 6

def recoleccionInsectos(i):
    dias=0
    total=0
    faltantes=0
    while i<30:
        dias +=1
        total += i
        faltante = 30-total
        print("Despues de ",dias,"dias recolectaste",total,"insectos \nTe faltan",faltante,"insectos para llegar a la meta")
        if i >= 30:
            print("Felicidades, has llegado a tu meta diaria.\nTe pasaste por",faltante*-1)
        elif faltante > 0: 
            i = int(input("Numero de Insectos cazados"))
        elif faltante <= 0:
            i = 30
                    
def calcularMayor():     
    guardarNumero = 0
    opcion = int(input("Teclea los valores numericos positivos que gustes y te dire el mayor.\nSi quieres parar, teclea -1"))
    if opcion == -1:
        m = 0
        if opcion == m:
            print("No hay datos para encontrar el mayor")
    print(opcion)
    while opcion != -1:
        if opcion > guardarNumero:
            mayor = opcion
        guardarNumero = opcion
        opcion = int(input("Teclea numeros!\nRecuerda que son ilimitados(No te pases)"))
        print(opcion)
    print("El mayor es",mayor)   
    
                   
def main():
    opcion = int(input("Elige una opcion:\n1.Recolectar Insectos\n2.Numero Mayor\n3.Salir"))
    while opcion != 3:
        if opcion == 1:
            i = int(input("Numero de Insectos cazados"))
            recoleccionInsectos(i)  
            opcion = int(input("Elige una opcion:\n1.Recolectar Insectos\n2.Numero Mayor\n3.Salir"))
        if opcion == 2:
            calcularMayor()
            opcion = int(input("Elige una opcion:\n1.Recolectar Insectos\n2.Numero Mayor\n3.Salir"))
        if opcion == 3:
            print("Adios")
    
main()
