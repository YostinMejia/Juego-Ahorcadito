import re
import random
import getpass

print(f"¡Bienvenidos!\n Las normas del juego son las siguientes: ") 
print( " \t 1) Ninguna palabara puede exceder los 15 caracteres. \n \t 2) En cada ronda, el jugador solo puede tratar de adivinar 1 palabra propuesta por el otro. \n \t 3) Para adivinar cada palabra, se tendrán 6 intentos, que corresponden a ingresar 6 letras erroneas. \n \t 4) Cuando la letra ingresada está en la palabra, se debe mostrar en qué posicón de la palabra se encuentra. Si la letra no está, se agrega una parte al cuerpo de ahorcado.")

#Creamos el juego
def Juego(n1,n2): 

    #Determinamos quien va primero
    jugador1=[n1,0,0,0]
    jugador2=[n2,0,0,0]

    #Cada ronda cuenta por 2 debido a que hay 2 jugadores
    ganador=[]
    for p in range(2):

        player=""
        #El jugador escoge la palabra para su adversario
        print()
        if p==0:
            print(n2,f"¿Cuál palabra quiere que ",n1," adivine?")
            player=jugador1
        else:
            print(n1,f"¿Cuál palabra quiere que ",n2," adivine?")
            player=jugador2

        #Ingresa la palabara con cantidad de caracteres especificos
        palabra=""
        descubrir=""
        while True:
            palabra=getpass.getpass("\n Ingrese una palabra que contenga entre 2 y 15 caracteres ").lower()

            if len(palabra)<15 and len(palabra)>2:
                for _ in range(len(palabra)):
                    descubrir+="_"
                break
            else:
                pass

        #Empiezan los intentos
        intentos=0
        print("Comience a adivinar, ¡Buena suerte!")
        print("\nSi desea ayuda, digite la palabra 'ayuda' cuando en el juego diga 'Digite la letra' \ny el juego pondrá de manera aleatoria una letra de la palabra que se está adivinando")

        while intentos<7:

            if descubrir==palabra:
                print(player[0],"Adivinaste")
                player[1]+=1
                break
            elif intentos<6:
                letra=input("\nDigite la letra: ").lower()
                if letra!="ayuda":
                    #Si la letra esta en la palabra
                    if letra in palabra:    
                        for j in range(len(palabra)):
                            #Cambiamos los "_" por la letra
                            if palabra[j]==letra:
                                temp=list(descubrir)
                                temp[j]=letra
                                descubrir="".join(temp)
                                print(descubrir)        
                        print("Lleva ",player[3]+1,f"asiertos y {intentos} intentos fallados")
                        if letra not in descubrir: #Se controla que no sume aciertos si digita una letra que ya adivino
                            player[3]+=1

                    else:
                        intentos+=1
                        archivo = open(f'./ahorcado#{intentos}.txt',"rt",encoding="utf-8")
                        print(f" \n {letra} no está en la palabra \n Tiene {6-intentos} mas \n {descubrir}")
                        print(archivo.read())
                        player[2]+=1

                #Se activa la ayuda
                else:
                    while True:
                        temp=list(descubrir)
                        r=random.randint(0,len(palabra)-1)
                        if temp[r]=="_":
                            palabra=list(palabra)
                            temp[r]=palabra[r]
                            descubrir="".join(temp)
                            palabra="".join(palabra)
                            print(descubrir)
                            break
                        else:
                            pass           
            else:
                print(player[0],f"Perdiste, la palabra era {palabra.upper()}")
                break
        print()

    if jugador1[2]<jugador2[2]:
        ganador.append("1")
    else:
        ganador.append("2")

    return ganador,jugador1[2],jugador2[2]

#ganador 
def Ganador(juego):  
        #0 nombre 1 rondas ganadas 2 intentos fallidos  
        jugador1=[0,0]
        jugador2=[0,0]
        for i in range(len(juego[0])):
            if juego[0][i]=="1":
                jugador1[0]+=1
            else:
                jugador2[0]+=1

        #Agrega los intentos a las listas que se retornan
        jugador1[1]=juego[1]
        jugador2[1]=juego[2]

        #Ganador del juego
        if jugador1[0] != jugador2[0]:
            if jugador1[0]>jugador2[0]:
                print(f"{n1.upper()} Es el ganador ")
            else:
                print(f"{n2.upper()} Es el ganador ")
        else:
            print(f"¡EMPATE!")

        return jugador1,jugador2

#Al final del juego se puede escoger si desea volver a continuar o no
again=""
while again!="no":
    
    modalidad=input("\nPara determinar la duración del juego: \n \t Opción #1-se puede pactar un número de rondas desde el principio \n \t Opción #2-Al final de cada ronda puede decidir si quiere continuar o terminar el juego \n\nDigite 1 para elegir la opción#1 o 2 para elegir la opción#2: ")
    n1=input("\nPrimero ingrese el nombre de quien desea comenzar adivinando: ")
    n2=input("Nombre del jugador #2: ")
    jugador1=[0,0]
    jugador2=[0,0]
    partida=0

    if modalidad=="1":

        #Ejecutamos las rondas ingresadas por el cliente
        rondas=input("¿Cuantas rondas desea jugar?")
        while True:
            x=re.findall("[a-zA-Z]",rondas)
            if x==[]:
                break
            else:
                print("Digite un número valido")
                rondas=input("¿Cuantas rondas desea jugar?")
        rondas=int(rondas)
        for i in range(rondas):
            juego=Juego(n1,n2)
            temp=Ganador(juego)
            partida+=1
            #sumamos las rondas ganadas a cada jugador
            jugador1[0]+=temp[0][0]
            jugador2[0]+=temp[1][0]
            #Sumamos los intentos a cada jugador
            jugador1[1]+=temp[0][1]
            jugador2[1]+=temp[1][1]

            print(f"Han jugado {partida} partidas, {n1} lleva {jugador1[0]} partidas ganadas y {jugador1[1]} intentos fallidos mientras que {n2} lleva {jugador2[0]} partidas ganadas y {jugador2[1]} intentos fallidos  ")

    elif modalidad=="2":

        stop=""
        while stop!="si":
            juego=Juego(n1,n2) 
            temp=Ganador(juego)
            partida+=1
            #sumamos las rondas ganadas a cada jugador
            jugador1[0]+=temp[0][0]
            jugador2[0]+=temp[1][0]
            #Sumamos los intentos a cada jugador
            jugador1[1]+=temp[0][1]
            jugador2[1]+=temp[1][1]

            print(f"Han jugado {partida} partidas, {n1} lleva {jugador1[0]} partidas ganadas y {jugador1[1]} intentos fallidos mientras que {n2} lleva {jugador2[0]} partidas ganadas y {jugador2[1]} intentos fallidos  ")

            stop=input("¿Desea detener el juego? \n ingrese si o no:").lower()

    else:
        print("Deje de ser bobo y digite un modo valido")

    again=input("El juego terminó \n¿Desea intentarlo de nuevo? ingrese si o no: ")