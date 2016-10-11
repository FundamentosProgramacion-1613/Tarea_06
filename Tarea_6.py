#encoding: UTF-8
#Aldo Fuentes A01373294
#Menu con funciones encontrar mayor y recoleccion de insectos



def calcularRecoleccionDeInsectos(insectos, dias, total, faltantes):
    total += insectos
    dias += 1
    faltantes -= insectos
    return dias, total, faltantes
def main():

    funcion = int(input("""Teclea la funcion:
        1. Recoleccion de insectos
        2. Encontrar mayor
        3. Salir"""))
        
    while funcion != 3:
        if funcion == 1:
            total = 0
            dias = 0
            faltantes = 30
            while total < 30:
                print("""

                """)
                insectos = int(input("Insectos recolectados hoy"))
                dias, total, faltantes = calcularRecoleccionDeInsectos(insectos, dias, total, faltantes)
                print("Despues de ",dias," dia(s) de recoleccion has acumulado ",total," insectos")
                if total-30>0:
                    print("Te pasaste por ", (faltantes*-1))
                else:
                    print("Te hace falta recolectar ",faltantes," insectos")
            print("Felicidades, alcanzaste la meta")
        elif funcion == 2:
            num = int(input("Numero"))
            mayor = num
            while num != -1:
                num = int(input("Numero"))
                if mayor < num:
                    mayor = num
                
            print("El mayor es: ", mayor)
            
        funcion = int(input("""Teclea la funcion:
            1. Recoleccion de insectos
            2. Encontrar mayor
            3. Salir"""))
            

main()