#encoding: UTF-8
#Autor: Allan Sánchez Iparrazar

def cazeriaInsectos():
	dias = 0
	insectosCazados = 0
	faltantes = 30
    
	while faltantes <= 30 :
		
		insectos = int(input("Numero de Insectos cazados hoy"))

		insectosCazados = insectosCazados + insectos
		dias = dias + 1 
		faltantes = faltantes - insectos
		if faltantes < 0 :        
			faltantes =  faltantes * -1			
			print("Despues de ",dias,"dias recolectaste",insectosCazados,"\nLograste tu meta con",faltantes,"insectos de mas")

			print("\n")
			faltantes = 31
		else :
			print("Despues de ",dias,"dias recolectaste",insectosCazados,"insectos, te faltan",faltantes,"insectos para llegar a la meta")


def calcularMayor():
	x = 0
	y = 0
	while y != -1:
		y = int(input("Ingresa un numero, presiona -1 para salir:\n"))
		if y == -1 and x == 0 :
			print("No hay datos para encontrar el mayor numero\n")

		elif y > x  : 
			x = y
			
		elif y == -1 :
			print("El mayor numero tecleado es:",x)
            
def main():
    menu = int(input("1. Cazeria de insectos\n2. Calcular mayor \n3. Salir\n"))
    
    
    while menu != 8 :
	
		
        if menu == 1 : 
        	cazeriaInsectos()
            
        elif menu == 2 :
            calcularMayor()
            
        elif menu == 0 : 
        		print("1. Cazeria de insectos\n2. Calcular mayo\n3. Salir")
        		
        menu = int(input("Ingresa una nueva opcion, si deseas ver el menu presiona 0\n"))
        
        if menu==3:
            print("Gracias y adios")
            menu = 8        
    
main()
