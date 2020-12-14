#TRABAJO CONJUNTO REALIZADO POR JOSE LUIS, SANDRA Y JAUME#
version = "1.0"
#Nombre del proyecto - BrisCards

#--------------------------------Este archivo contiene el juego

#Imports
import random
import time
import os
import sys



#Declaración de variables:
cartasjugador = []
cartasmaquina = []
cardlist = []
nombreMaquina = 'Maquina'
puntosMaquina = 0
puntosJugador = 0

puntosComprobar1 = 0
puntosComprobar2 = 0


acabarPartida = False
Finalizar = False

gana = 'Nadie'
#----------------------------------------Juego



def borrar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')



#Generación de todas las cartas

def generar_cartas():

    for bastos in range (1, 13):
        if bastos != 8 and bastos != 9:
            if bastos < 10:
                cardlist.append('0' + str(bastos) + "-Bastos")
            else:
                cardlist.append(str(bastos) + "-Bastos")

    for copas in range (1, 13):
        if copas != 8 and copas != 9:
            if copas < 10:
                cardlist.append('0' + str(copas) + "-Copas")
            else:
                cardlist.append(str(copas) + "-Copas")
    
    for oros in range (1, 13):
        if oros != 8 and oros != 9:
            if oros < 10:
                cardlist.append('0' + str(oros) + "-Oros")
            else:
                cardlist.append(str(oros) + "-Oros")
    
    for espadas in range (1, 13):
        if espadas != 8 and espadas != 9:
            if espadas < 10:
                cardlist.append('0' + str(espadas) + "-Espadas")
            else:
                cardlist.append(str(espadas) + "-Espadas")



#Procedemos a sacar las cartas del sobre

generar_cartas()


#Se barajan las cartas
random.shuffle(cardlist)


#Se le entregan tres cartas al jugador y tres cartas a la máquina
cartasjugador.append(cardlist[0])
cardlist.remove(cartasjugador[0])
cartasmaquina.append(cardlist[0])
cardlist.remove(cartasmaquina[0])

cartasjugador.append(cardlist[0])
cardlist.remove(cartasjugador[1])
cartasmaquina.append(cardlist[0])
cardlist.remove(cartasmaquina[1])

cartasjugador.append(cardlist[0])
cardlist.remove(cartasjugador[2])
cartasmaquina.append(cardlist[0])
cardlist.remove(cartasmaquina[2])



#Se elige la carta dominante del juego

cartaDominante = cardlist[0]
cardlist.remove(cartaDominante)


#Se elige el turno de quien empieza

elegirPrimerTurno = random.randint(0,1)
if elegirPrimerTurno == 0:
    turno = 'Máquina'
else:
    turno = 'Jugador'



def compruba_puntos(cartasComprobar1, cartasComprobar2):

    global puntosComprobar1
    global puntosComprobar2

    if int(cartasComprobar1[0:2]) == 2:
        puntosComprobar1 = 0
    elif int(cartasComprobar1[0:2]) == 4:
        puntosComprobar1 = 0
    elif int(cartasComprobar1[0:2]) == 5:
        puntosComprobar1 = 0
    elif int(cartasComprobar1[0:2]) == 6:
        puntosComprobar1 = 0
    elif int(cartasComprobar1[0:2]) == 7:
        puntosComprobar1 = 0

    
    if int(cartasComprobar2[0:2]) == 2:
        puntosComprobar2 = 0
    elif int(cartasComprobar2[0:2]) == 4:
        puntosComprobar2 = 0
    elif int(cartasComprobar2[0:2]) == 5:
        puntosComprobar2 = 0
    elif int(cartasComprobar2[0:2]) == 6:
        puntosComprobar2 = 0
    elif int(cartasComprobar2[0:2]) == 7:
        puntosComprobar2 = 0



def comprobar_ganador(turnoQuien, jugadorsacas, cartasmaquinas):

    global puntosJugador
    global puntosMaquina
    global turno
    global cartasmaquina
    global puntosComprobar1
    global puntosComprobar2
    global gana
    
    #comprobar puntos
    
    
    cartasComprobar1 = jugadorsacas
    cartasComprobar2 = cartasmaquinas
    
    
    
    #Comprobar las cartas del jugador y asignar la puntuacion que corresponde
    if int(cartasComprobar1[0:2]) == 10:
        puntosComprobar1 = 2
    elif int(cartasComprobar1[0:2]) == 11:
        puntosComprobar1 = 3
    elif int(cartasComprobar1[0:2]) == 12:
        puntosComprobar1 = 4
    elif int(cartasComprobar1[0:2]) == 1:
        puntosComprobar1 = 11
    elif int(cartasComprobar1[0:2]) == 3:
        puntosComprobar1 = 10
    elif int(cartasComprobar1[0:2]) == 2:
        puntosComprobar1 = 0.1
    elif int(cartasComprobar1[0:2]) == 4:
        puntosComprobar1 = 0.2
    elif int(cartasComprobar1[0:2]) == 5:
        puntosComprobar1 = 0.3
    elif int(cartasComprobar1[0:2]) == 6:
        puntosComprobar1 = 0.4
    elif int(cartasComprobar1[0:2]) == 7:
        puntosComprobar1 = 0.5
    
    
    #Comprobar las cartas de la maquina y asignar la puntuacion que corresponde
    if int(cartasComprobar2[0:2]) == 10:
        puntosComprobar2 = 2
    elif int(cartasComprobar2[0:2]) == 11:
        puntosComprobar2 = 3
    elif int(cartasComprobar2[0:2]) == 12:
        puntosComprobar2 = 4
    elif int(cartasComprobar2[0:2]) == 1:
        puntosComprobar2 = 11
    elif int(cartasComprobar2[0:2]) == 3:
        puntosComprobar2 = 10
    if int(cartasComprobar2[0:2]) == 2:
        puntosComprobar2 = 0.1
    elif int(cartasComprobar2[0:2]) == 4:
        puntosComprobar2 = 0.2
    elif int(cartasComprobar2[0:2]) == 5:
        puntosComprobar2 = 0.3
    elif int(cartasComprobar2[0:2]) == 6:
        puntosComprobar2 = 0.4
    elif int(cartasComprobar2[0:2]) == 7:
        puntosComprobar2 = 0.5
    
    
    
    
    
    #RESULTADO
    #Si el palo de la carta de la maquina no es del mismo que del palo del jugador
    if cartasComprobar1[3:] != cartasComprobar2[3:]:
        
        #Si el palo de la maquina no es del palo dominante
        if cartasComprobar2[3:] != cartaDominante[3:]:
            if turnoQuien == 'Máquina':
                gana = 'Máquina'
                compruba_puntos(cartasComprobar1, cartasComprobar2)
                puntosMaquina += int(puntosComprobar1) + int(puntosComprobar2)
            else:
                gana = 'Jugador'
                compruba_puntos(cartasComprobar1, cartasComprobar2)
                puntosJugador += int(puntosComprobar1) + int(puntosComprobar2)
            

        
        #Si es del palo dominante
        elif cartasComprobar2[3:] == cartaDominante[3:]:
            if cartasComprobar1[3:] != cartaDominante[3:]:
                if turnoQuien == 'Máquina':
                    gana = 'Jugador'
                    compruba_puntos(cartasComprobar1, cartasComprobar2)
                    puntosJugador += int(puntosComprobar1) + int(puntosComprobar2)
                else:
                    gana = 'Máquina'
                    compruba_puntos(cartasComprobar1, cartasComprobar2)
                    puntosMaquina += int(puntosComprobar1) + int(puntosComprobar2)

                
    #Si el palo de la carta de la maquina es el mismo que la del jugador
    else:
        
        #Si la carta del jugador es mas grande que la de la maquina
        if float(puntosComprobar1) > float(puntosComprobar2):
            if turnoQuien == 'Máquina':
                gana = 'Máquina'
                compruba_puntos(cartasComprobar1, cartasComprobar2)
                puntosMaquina += int(puntosComprobar1) + int(puntosComprobar2)
            else:
                gana = 'Jugador'
                compruba_puntos(cartasComprobar1, cartasComprobar2)
                puntosJugador += int(puntosComprobar1) + int(puntosComprobar2)    

            

        #Si la carta del jugador es mas pequeña que la de la máquina
        else:
            if turnoQuien == 'Máquina':
                gana = 'Jugador'
                compruba_puntos(cartasComprobar1, cartasComprobar2)
                puntosJugador += int(puntosComprobar1) + int(puntosComprobar2)
            else:
                gana = 'Máquina'
                compruba_puntos(cartasComprobar1, cartasComprobar2)
                puntosMaquina += int(puntosComprobar1) + int(puntosComprobar2)

        

    borrar_pantalla()

    print('Carta dominante: ' + cartaDominante + '    Puntos maquina:' + str(puntosMaquina) + '    Puntos jugador:' + str(puntosJugador))
    print()
    print('                                          EL GANADOR DE ESTA RONDA ES : ' + gana)
    print('Tus cartas')
    print('[1] ' + cartasjugador[0])
    if len(cartasjugador) > 1:
        print('[2] ' + cartasjugador[1])
    else:
        print('[2] - ')
    if len(cartasjugador) > 2:
        print('[3] ' + cartasjugador[2])
    else:
        print('[3] - ')
    print('__________________________________')
    choice = input('Pulsa [ENTER] para continuar')



    turno = gana




#---------------------------------------------------------------Se define la pantalla en caso de que el jugador continue el turno

def turno_jugador():

    choice = 'x'
    
    global puntosJugador
    global puntosMaquina
    global cartaDominante
    global acabarPartida
    global Finalizar

    if acabarPartida == True:
        Finalizar = True

    finishTurn = False
    
    while finishTurn == False:
        borrar_pantalla()
        print('Carta dominante: ' + cartaDominante + '    Puntos maquina:' + str(puntosMaquina) + '    Puntos jugador:' + str(puntosJugador))
        print()
        print()
        print('Tus cartas')
        print('[1] ' + cartasjugador[0])
        if len(cartasjugador) > 1:
            print('[2] ' + cartasjugador[1])
        else:
            print('[2] - ')
        if len(cartasjugador) > 2:
            print('[3] ' + cartasjugador[2])
        else:
            print('[3] - ')
        print('__________________________________')
        choice = input('Escoje una carta, 1, 2, o 3 : ')
        
        if choice == '1':
            jugadorsaca = cartasjugador[0]
            finishTurn = True
        elif choice == '2' and len(cartasjugador) > 1:
            jugadorsaca = cartasjugador[1]
            finishTurn = True
        elif choice == '3' and len(cartasjugador) > 2:
            jugadorsaca = cartasjugador[2]
            finishTurn = True

    borrar_pantalla()
    print('Carta dominante: ' + cartaDominante + '    Puntos maquina:' + str(puntosMaquina) + '    Puntos jugador:' + str(puntosJugador))
    print()
    print('                                          Jugador saca: ' + jugadorsaca + '    Maquina saca: ' + cartasmaquina[0] )
    print('Tus cartas')
    print('[1] ' + cartasjugador[0])
    if len(cartasjugador) > 1:
        print('[2] ' + cartasjugador[1])
    else:
        print('[2] - ')
    if len(cartasjugador) > 2:
        print('[3] ' + cartasjugador[2])
    else:
        print('[3] - ')
    print('__________________________________')
    choice = input('Pulsa [ENTER] para continuar')
    
    

    comprobar_ganador('Jugador', jugadorsaca, cartasmaquina[0])

    #Borrar la carta del mazo del jugador y de la máquina
    cartasjugador.remove(jugadorsaca)
    cartasmaquina.remove(cartasmaquina[0])
    
    #Poner otra carta en el lugar del mazo principal
    

    
    if not cardlist:
        pass
    else:
        if gana == 'Jugador':
            cartasjugador.append(cardlist[0])
            cardlist.remove(cardlist[0])
            if cardlist:
                cartasmaquina.append(cardlist[0])
                cardlist.remove(cardlist[0])
            else:
                cartasmaquina.append(cartaDominante)
                acabarPartida = True
        else:
            cartasmaquina.append(cardlist[0])
            cardlist.remove(cardlist[0])
            if cardlist:  
                cartasjugador.append(cardlist[0])
                cardlist.remove(cardlist[0])
            else:
                cartasjugador.append(cartaDominante)
                acabarPartida = True
                
        

        
    



#-----------------------------------Se define la pantalla en caso de que la maquina continue el turno

def turno_maquina():

    choice = 'x'
    
    global puntosJugador
    global puntosMaquina
    global cartaDominante
    global acabarPartida
    global Finalizar
    
    finishTurn = False
    
    if not cartasjugador:
        Finalizar = True
    
    while finishTurn == False:
        borrar_pantalla()
        print('Carta dominante: ' + cartaDominante + '    Puntos maquina:' + str(puntosMaquina) + '    Puntos jugador:' + str(puntosJugador))
        print()
        print('                                          Maquina saca: ' + cartasmaquina[0] )
        print('Tus cartas')
        print('[1] ' + cartasjugador[0])
        if len(cartasjugador) > 1:
            print('[2] ' + cartasjugador[1])
        else:
            print('[2] - ')
        if len(cartasjugador) > 2:
            print('[3] ' + cartasjugador[2])
        else:
            print('[3] - ')
        print('__________________________________')
        choice = input('Escoje una carta, 1, 2, o 3 : ')
        
        if choice == '1':
            jugadorsaca = cartasjugador[0]
            finishTurn = True
        elif choice == '2' and len(cartasjugador) > 1:
            jugadorsaca = cartasjugador[1]
            finishTurn = True
        elif choice == '3' and len(cartasjugador) > 2:
            jugadorsaca = cartasjugador[2]
            finishTurn = True

    borrar_pantalla()
    print('Carta dominante: ' + cartaDominante + '    Puntos maquina:' + str(puntosMaquina) + '    Puntos jugador:' + str(puntosJugador))
    print()
    print('                                          Maquina saca: ' + cartasmaquina[0] + '    Jugador saca: ' + jugadorsaca + '    ' )
    print('Tus cartas')
    print('[1] ' + cartasjugador[0])
    if len(cartasjugador) > 1:
        print('[2] ' + cartasjugador[1])
    else:
        print('[2] - ')
    if len(cartasjugador) > 2:
        print('[3] ' + cartasjugador[2])
    else:
        print('[3] - ')
    print('__________________________________')
    choice = input('Pulsa [ENTER] para continuar')
    
    
    comprobar_ganador('Máquina', cartasmaquina[0], jugadorsaca)


    #Borrar la carta del mazo del jugador y de la máquina
    cartasjugador.remove(jugadorsaca)
    cartasmaquina.remove(cartasmaquina[0])
    
    #Poner otra carta en el lugar desde el mazo principal



    if not cardlist:
        pass
    else:
        if gana == 'Jugador':
            cartasjugador.append(cardlist[0])
            cardlist.remove(cardlist[0])
            if cardlist:
                cartasmaquina.append(cardlist[0])
                cardlist.remove(cardlist[0])
            else:
                cartasmaquina.append(cartaDominante)
                acabarPartida = True
        else:
            cartasmaquina.append(cardlist[0])
            cardlist.remove(cardlist[0])
            if cardlist:
                cartasjugador.append(cardlist[0])
                cardlist.remove(cardlist[0])
            else:
                cartasjugador.append(cartaDominante)
                acabarPartida = True
                

#---------------------------------------------------------------------------Bucle del juego
running = True

while running:
    
    if not cartasjugador:
        if puntosJugador > puntosMaquina:
            winner = 'JUGADOR'
        else:
            winner = 'MÁQUINA'
        
        exit = False
        
        while exit == False:
                borrar_pantalla()
                print('Carta dominante: ' + cartaDominante + '    Puntos maquina:' + str(puntosMaquina) + '    Puntos jugador:' + str(puntosJugador))
                print()
                print('                                          EL GANADOR DE LA PARTIDA ES: ' + winner)
                print()
                print()
                print()
                print()
                print('__________________________________')
                choice = input('Pulsa [1] para continuar')
                
                if choice == '1':
                    running = False
                    exit = True
                    sys.exit()   
    
    if turno == 'Jugador':
        turno_jugador()
    elif turno == 'Máquina':
        turno_maquina()
    
    

                

