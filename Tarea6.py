#encoding: UTF-8
#Autor: Hector david Hernandez Rodriguez
#A01374009
#Tarea 6

def cazeriaInsectos(i):
    dias=0
    t=0
    f=0
    while i<30:
        dias +=1
        t=t+i
        f=30-t
        print("Despues de ",dias,"dias recolectaste",t,"insectos, te faltan",f,"insectos para llegar a la meta")
        i += int(input("Numero de Insectos cazados"))
    f=i-30
    print("llegaste a tu meta diaria con un sobrante de",f)


def calcularMayor(x,y):
    while y != -1:
        y = int(input("Escriba un numero"))
        if (y > x):
            x = y
            
    else:
        print(x)
            
def seleccionarMenu(menu):
       if menu==1:
            i = int(input("Numero de Insectos cazados"))
            cazeriaInsectos(i)
       elif menu ==2:
            x = 0
            y = 0
            calcularMayor(x,y)     
       elif menu==3:
            print("Gracias y adios")
       else:
        print ("No aplica")
              
       
def main():
    menu = int(input("1 CAZERIA DE INSECTOS, 2 CALCULAR MAYOR , 3 SALIR"))
    seleccionarMenu(menu)
    
main()