import random

print(f"¡Bienvenidos!\n Las normas del juego son las siguientes: ") 
print( " \t 1) Ninguna palabara puede exceder los 15 caracteres \n \t 2) En cada ronda, un jugador puede tratar de adivinar solo 1 palabra propuesta por el otro \n \t 3) Para adivinar cada palabra, se tendran 6 intentosque corresponden a ingresar 6 letras erroneas \n \t 4) Cuando la letra ingresada esta en la palabra, se debe mostrar en que posicón de la palabra se encuentra si la letra no esta, se agrega una parte de ahoracado")

#Creamos el juego
def Juego(n1,n2): 

    #Determinamos quien va primero
    jugador1={"nombre":n1,"ganadas":0,"intentos":0,"correctos":0}
    jugador2={"nombre":n2,"ganadas":0,"intentos":0,"correctos":0}

    #Cada ronda cuenta por 2 debido a que hay 2 jugadores
    g=[]
    for p in range(2):

        player=""
        #El jugador escoge la palabra para su adversario
        print()
        if p==0:
            print(jugador2["nombre"],f"¿cual palabra quiere que ",jugador1["nombre"]," adivine?")
            player=jugador1
        else:
            print(jugador1["nombre"],f"¿cual palabra quiere que ",jugador2["nombre"]," adivine?")
            player=jugador2

        #Ingresa la palabara con cantidad de caracteres especificos
        palabra=""
        descubrir=""
        while True:
            palabra=input("\n Ingrese una palabra con más de 2 caracteres y menos de 15 caracteres: ").lower()
            if len(palabra)<15 and len(palabra)>2:
                for _ in range(len(palabra)):
                    descubrir+="_"
                break
            else:
                pass

        #Empiezan los intentos
        intentos=0
        print("Comience a adivinar, ¡Buena suerte!")
        print("\nSi desea ayuda esta pone una letra correcta de manera aleatoria, en el momento en el que le aparezca 'Digite la letra' ingrese 'ayuda' ")

        while intentos<7:

            if descubrir==palabra:
                print(player["nombre"],"Adivinaste")
                player["ganadas"]+=1
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
                        print("Lleva ",player["correctos"]+1,f"asiertos correctos y {intentos} fallados")
                        player["correctos"]+=1
                    else:
                        print(f" \n {letra} no está en la palabra \n Tiene {6-intentos} mas \n {descubrir}")
                        intentos+=1
                        archivo = open(f'./ahorcado#{intentos}.txt',"rt",encoding="utf-8")
                        print(archivo.read())
                        player["intentos"]+=1
                        
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
                print(player["nombre"],f"Perdiste, la palabra era {palabra.upper()}")
                break
        print()

        #le agregamos a "g" el ganador para irlo sumando
        if jugador1["ganadas"]!=jugador2["ganadas"]:
            if jugador1["ganadas"]>jugador2["ganadas"]:
                g.append("1")
            else:
                g.append("2")
        #si ambos ganaron se escoge el que tiene menos fallos 
        else:
            if jugador1["intentos"]<jugador2["intentos"]:
                g.append("1")
            else:
                g.append("2")
    return g,jugador1["intentos"],jugador2["intentos"]

#Al final del juego se puede escoger si desea volver a continuar o no
again=""
while again!="no":
    modalidad=input("\nPara determinar la duración del juego: \n \t opcion #1-se puede pactar un número de rondas desde el principio \n \t opcion #2-Al final de cada ronda puede decidir si quiere continuar o terminar el juego \n\nDigite 1 para elegir la opcion#1 o 2 para elegir la opcion#2: ")

    if modalidad=="1":

        n1=input("\nPrimero ingrese el nombre de quien desea comenzar adivinando: ")
        n2=input("Nombre del jugador #2: ")
        

        ganador1=[n1,0]
        ganador2=[n2,0]

        #Ejecutamos las rondas ingresadas por el cliente
        for i in range(int(input("\nDigite el numero de rondas que desean jugar: "))):
            juego=Juego(n1,n2)
            for i in range(2):
                if juego[i]=="1":
                    ganador1[1]+=1
                else:
                    ganador2[1]+=1


        #Ganador del juego
        if ganador1[1] != ganador2[1]:
            if ganador1[1]>ganador2[1]:
                print(f"{ganador1[0].upper()} Es el ganador ")
            else:
                print(f"{ganador2[0].upper()} Es el ganador ")
        else:
            print(f"¡EMPATE!")





    elif modalidad=="2":

        n1=input("\nPrimero ingrese el nombre de quien desea comenzar adivinando: ")
        n2=input("Nombre del jugador #2: ")

        ganador1=[n1,0]
        ganador2=[n2,0]

        stop=""
        while stop!="si":
            juego=Juego(n1,n2) 
            for i in range(2):
                if juego[i]=="1":
                    ganador1[1]+=1
                else:
                    ganador2[1]+=1
            stop=input("¿Desea detener el juego? \n ingrese si o no:").lower()

        #Ganador del juego
        if ganador1[1]!=ganador2[1]:
            if ganador1[1]>ganador2[1]:
                print(f"{ganador1[0].upper()} Es el ganador ")
            else:
                print(f"{ganador2[0].upper()} Es el ganador ")
        else:
            print(f"¡EMPATE!")

    else:
        print("Deje de ser bobo y digite una opcion valida")

    again=input("El juego termino \n¿Desea intentarlo de nuevo? ingrese si o no: ")