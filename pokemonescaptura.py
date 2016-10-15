#encoding: UTF-8
#Blanca Calderón
#Ciclos For


def colectarPokemones():
    dias=0
    pokes=0
    pokemones=0
    while pokes<30 :
        pokemones =int(input("¿Cuantos pokemones colectaste hoy?"))
        dias += 1
        pokes +=pokemones
        pokerestantes=30
        operacion= pokerestantes-pokes
        if operacion<0:
            respuesta= "pokemones y te sobran"
            operacion=operacion*(-1)
        else:
            respuesta="pokemones y te hacen falta"
        print("Tu colectaste en tu dia número",dias, pokemones,"pokemones, llevas",pokes,respuesta,operacion, ". Eres un experto en atrapar pokemones")
        if pokes>=30:
            print("Felicidades, Eres un verdadero maestro pokemon ")
            
def compararCombatPower():
    #pokemones=int(input("¿Cuantos pokemones vas a comparar?"))#si no sabíamos cuántos datos entraran, ahora sabemos
    
    while pokepoder>=0:
        pokepoder=int(input("Intruduce el Poder de Combate de tu pokemon"))
        #INTENTÉ HACERLO A LAPIZ, PERO IGUAL, SIENTO QUE ALGO HACE FALTA
        #COMO CUANDO ESTOY PASANDO POR ALTO ALGO Y NO LO VEO AUN
                
        
def main():
    menu=int(input("1.-Colectar pokemones/ 2.-Comparar poder de combate/ 3.-Salir/ Elige qué hacer."))
    if menu==1:
        colectarPokemones()
    elif menu==2:
        compararCombatPower()
    else:
        print("Ve a atrapar pokemones y sé el mejor maestro entrenado pokemón")

main()

