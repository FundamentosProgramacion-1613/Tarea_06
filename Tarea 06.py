#encoding: UTF-8
#Autor: Marina Itzel Haro Hernández, A01373471
#Tarea 06 - While


def calcularInsectos():
    insectos = int(input("Insectos recolectados hoy"))
    dia = 1
    while insectos < 30 :
        e = 30 - insectos
        print ("Después de %d día(s) de recolección has acumulado %d insecto(s)" % (dia, insectos))
        print ("Te hace falta recolectar", e, "insectos")
        dia += 1
        insectos2 = int(input("Insectos recolectados hoy"))
        insectos += insectos2
        
        
    if insectos >= 30:
        if insectos == 30:
            e = 30 - insectos
            print ("Después de %d día(s) de recolección has acumulado %d insecto(s)" % (dia, insectos))
            print ("Te hace falta recolectar %d insecto(s)" % e)
             
        if insectos > 30:
            f = insectos - 30
            print ("Después de %d día(s) de recolección has acumulado %d insecto(s)" % (dia, insectos))
            print ("Te has pasado con %d insecto(s)" % f)
            
        print ("Felicidades has llegado a la meta")
        
    return (dia, insectos)
    
    
    
def calcularMayor():
    numero = 0
    m = 0
    while numero != -1 :
        numero = int(input("Teclea un número entero positivo"))
        print(numero)
        if numero > m:
            m = numero
    if m == 0 :
        print("No hay datos para encontar el valor mayor.")
    else:
        print ("El mayor es:", m)

  
def main():
    opcion = 0
    while opcion != 3 :
        print ("\n")
        opcion = int(input("1. Encontrar mayor \n2. Recolectar insectos \n3. Salir \nTeclea tu opción"))
        if opcion == 1 :
            calcularMayor()
        elif opcion == 2 :
            calcularInsectos()
        elif opcion == 3 :
            print("Adios")
        else:
            print("Ingresa una oción válida")
            
main()
        
        
        