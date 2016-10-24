#Autor:Ma Fernanda Rodriguez H A01371649
#Tarrea 6 hacer un programa que lleve la cuenta de insectos recolectados y en otra variable que encuentre el numero mayor 
#encoding: UTF-8 

def encontrarMayor():
    num=0
    while(1):
        valor = int(input("Ingresa solo un valor.\nPara terminar con la lista de valores teclea -1  "))
        if valor==-1:
            break;
        if valor > num:
            num=valor    
    print("el numero mayor es",num)
    
def recolectarInsectos():
     lista = []
     while (1):
        suma=0
        cantidad= int(input("cuantos insectos recolectaste hoy?\ncuando ya no quieras contar mas, teclea 0"))
        a= lista.append(cantidad)
        for i in lista:
            suma+=i
            print(suma)
       
            if suma <= 30:
                resta = 30 - suma
                print("despues de",len(lista),"dia(s), has recolectado",suma,"insectos.\nTe hace falta recolectar",resta,"insectos")
            elif suma > 30: 
                resta = suma -30
                print("despues de",len(lista),"dia(s), has recolectado",suma,"insectos.\nTe hace falta recolectar",resta,"insectos")   
        if cantidad ==0:
            break;    

def main():
  while True:
    print("MENU")
    print("1.Encontrar mayor")
    print("2.Recolectar insectos")
    print("3.Salir")
    opcion=int(input("Que deseas realizar?\nMENU\n1.Encontrar Mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opcion"))
    if (opcion==1):
        encontrarMayor()
       
    if (opcion==2):
        recolectarInsectos()
    
    if (opcion==3):
        break;
    else:
        print("esa opcion no es valida")   
    

main()