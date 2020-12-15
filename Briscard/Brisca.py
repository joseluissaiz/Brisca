#TRABAJO CONJUNTO REALIZADO POR JOSE LUIS, SANDRA Y JAUME#
version = "1.0"
#Nombre del proyecto - BrisCards

#--------------------------------Este archivo contiene el juego




#Imports
import random
import time
import os
import sys
import msvcrt










#-----------------------------------------------------------------------------------Funciones del sistema operativo
#Borrar pantalla
def borrar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')






#   ___  ___                  ______     _              
#   |  \/  |                  | ___ \   | |             
#   | .  . | ___ _ __  _   _  | |_/ /___| |_ _ __ _   _ 
#   | |\/| |/ _ \ '_ \| | | | |    // _ \ __| '__| | | |
#   | |  | |  __/ | | | |_| | | |\ \  __/ |_| |  | |_| |
#   \_|  |_/\___|_| |_|\__,_| \_| \_\___|\__|_|   \__, |
#                                                  __/ |
#                                                 |___/ 







#---------------------------------------------------Funcion para resetear los valores iniciales de las partidas
def reset_match():
    
    global nombreMaquina
    global puntosJugador
    global puntosMaquina
    global puntosComprobar1
    global puntosComprobar2
    
    global acabarPartida
    global Finalizar
    global gana
    global turno
    
    global cartasjugador
    global cartasmaquina
    global cardlist
    
    
    cartasjugador = []
    cartasmaquina = []
    cardlist = []
    nombreMaquina = 'Maquina'
    puntosMaquina = 0
    puntosJugador = 0
            
    puntosComprobar1 = 0
    puntosComprobar2 = 0

    generar_cartas()


    random.shuffle(cardlist)


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




    cartaDominante = cardlist[0]
    cardlist.remove(cartaDominante)



    elegirPrimerTurno = random.randint(0,1)
    if elegirPrimerTurno == 0:
        turno = 'Máquina'
    else:
        turno = 'Jugador'

    acabarPartida = False
    Finalizar = False

    gana = 'Nadie'




# ----------------------------------------------------------Función para mostrar el menú "Retry"

selection = 'Retry'

def moverse_RetryMenu():
    
    global selection
    global runningRM
    global currentMenu
    

    
    
    

    
    selectBool = False # Esta variable evita que el menu parpadee infinitamente

    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == "w":
            if selection == 'Retry':
                selection = 'Volver'
                
            elif selection == 'Volver':
                selection = 'Retry'
            
            selectBool = True
        
        elif key == "s":
            if selection == 'Retry':
                selection = 'Volver'
                
            elif selection == 'Volver':
                selection = 'Retry'
            
            selectBool = True
            
        
        elif key == "x":
            if selection == 'Retry':
                
                reset_match()
                jugar()
                runningRM = False
                
            elif selection == 'Volver':
                runningRM = False
                reset_match()
                currentMenu = 'Principal'
                selection = 'Jugar'
                showmenu()

        
    if selectBool == True: # El menu solo se mostrará cuando se tenga que actualizar
        RetryMenu()    







def RetryMenu():
    
    global selection
    
    borrar_pantalla()
    print(' __________________________________________________________________')
    print('|                                                                  |')
    print('|               --  F I N  D E  L A  P A R T I D A  --             |')
    print('|__________________________________________________________________|')
    print('|                                                                  |')
    if selection == 'Retry':
        print('|                     [x]> Jugar otra vez                          |')
    else:
        print('|                          Jugar otra vez                          |')
    print('|                                                                  |')
    if selection == 'Volver':
        print('|                   [x]>   Volver al menu                          |')
    else:
        print('|                          Volver al menu                          |')
    print('|                                                                  |')
    print('|__________________________________________________________________|')
    print('')
    print('      Controles')
    print(' __________________')
    print('|                  |')
    print('| Arriba:      [W] |')
    print('| Abajo:       [S] |')
    print('| Seleccionar: [X] |')
    print('| Atras:       [Z] |')
    print('|__________________|\n')

    moverse_RetryMenu()
    
    
    
    
runningRM = True

RetryMenu()
    
def ShowRetryMenu():
    
    global selection
    global currentMenu
    
    currentMenu = 'RetryMenu'
    selection = 'Retry'
    
    RetryMenu()
    
    while runningRM == True:
        moverse_RetryMenu()





















#    _____           _ _                   _      _     _                        
#   /  __ \         | (_)                 | |    | |   (_)                       
#   | /  \/ ___   __| |_  __ _  ___     __| | ___| |    _ _   _  ___  __ _  ___  
#   | |    / _ \ / _` | |/ _` |/ _ \   / _` |/ _ \ |   | | | | |/ _ \/ _` |/ _ \ 
#   | \__/\ (_) | (_| | | (_| | (_) | | (_| |  __/ |   | | |_| |  __/ (_| | (_) |
#    \____/\___/ \__,_|_|\__, |\___/   \__,_|\___|_|   | |\__,_|\___|\__, |\___/ 
#                         __/ |                       _/ |            __/ |      
#                        |___/                       |__/            |___/   




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


winner = 'Nadie'
#----------------------------------------Juego

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
                




#----------------------------------------------------------------Actualiza el archivo de los resultados

def actualizar_resultados():
    
    global winner
    
    if not os.path.exists('Config/results.bcd'): # Si no existe el archivo, crea uno nuevo
        file = open('Config/results.bcd', 'w')

        file.write("0\n")
        file.write('0')
        file.close()
    
    file = open("Config/results.bcd", "r") # Lee el archivo y recoge los resultados
    currentUserMark = int(file.readline())
    currentMachMark = int(file.readline())
    file.close()
    
    
    if winner == 'JUGADOR':
        currentUserMark += 1
    else:
        currentMachMark += 1
        
        
    file = open("Config/results.bcd", "w") # Actualiza los resultados
    file.write(str(currentUserMark) + "\n")
    file.write(str(currentMachMark))
    file.close()








#---------------------------------------------------------------------------Bucle del juego


def jugar():
    
    global winner
    
    running = True
    
    while running:
    
        if not cartasjugador:
            if puntosJugador > puntosMaquina:
                winner = 'JUGADOR'
            else:
                winner = 'MÁQUINA'
        
            exit = False
        
            actualizar_resultados()
        
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
                    ShowRetryMenu()
                       
        if running:
            if turno == 'Jugador':
                turno_jugador()
            elif turno == 'Máquina':
                turno_maquina()
    
    







#   ___  ___                  ______     _            _             _ 
#   |  \/  |                  | ___ \   (_)          (_)           | |
#   | .  . | ___ _ __  _   _  | |_/ / __ _ _ __   ___ _ _ __   __ _| |
#   | |\/| |/ _ \ '_ \| | | | |  __/ '__| | '_ \ / __| | '_ \ / _` | |
#   | |  | |  __/ | | | |_| | | |  | |  | | | | | (__| | |_) | (_| | |
#   \_|  |_/\___|_| |_|\__,_| \_|  |_|  |_|_| |_|\___|_| .__/ \__,_|_|
#                                                      | |            
#                                                      |_|    






#--------------------------------Funciones del menu principal
#------------------------------------------------------Comentarios de los integrantes

# 25/11/2020 - Jose: Le ha dado un toque personal al menú
#                    añadiendo un poco de ASCII
#
#                    [!] import msvcrt -> La app solo correrá 
#                                         en windows.














#-------------------------------------------------------------------------------------Variables del menu
selection = 'Jugar'
exitMenu = 'False'




#-------------------------------------------------------------------------------------Funciones de movimiento

#------------------------------------------------------Funcion para moverse dentro del menu principal<
def moverse_menuX1():
    
    global selection
    global currentMenu
    global exitMenu
    
    selectBool = False # Esta variable evita que el menu parpadee infinitamente

    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == "w":
            if selection == 'Jugar':
                selection = 'Salir'
                
            elif selection == 'Registro':
                selection = 'Jugar'
            
            elif selection == 'Instrucciones':
                selection = 'Registro'
                
            elif selection == 'Salir':
                selection = 'Instrucciones'
            
            selectBool = True
        
        elif key == "s":
            if selection == 'Jugar':
                selection = 'Registro'
            
            elif selection == 'Registro':
                selection = 'Instrucciones'

            elif selection == 'Instrucciones':
                selection = 'Salir'

            elif selection == 'Salir':
                selection = 'Jugar'
            
            selectBool = True
            
        
        elif key == "x":
            if selection == 'Instrucciones':
                selection = 'Rules'
                currentMenu = 'Instrucciones'
                mostrar_menuX2()
            elif selection == 'Jugar':
                exitMenu = True
                jugar()
            elif selection == 'Salir':
                borrar_pantalla()
                sys.exit()
            elif selection == 'Registro':
                currentMenu = 'Registro'
                mostrar_menuX3()
        
    if selectBool == True: # El menu solo se mostrará cuando se tenga que actualizar
        mostrar_menuX1()
        


#-------------------------------------------------------Funcion para moverse dentro del menu de instrucciones<
def moverse_menuX2():
    
    global selection
    global currentMenu
    
    selectBool = False # Esta variable evita que el menu parpadee infinitamente

    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == "w":
            if selection == 'Rules':
                selection = 'Volver'
                
            elif selection == 'Puntuacion':
                selection = 'Rules'
                
            elif selection == 'Volver':
                selection = 'Puntuacion'
            
            selectBool = True
        
        elif key == "s":
            if selection == 'Rules':
                selection = 'Puntuacion'

            elif selection == 'Puntuacion':
                selection = 'Volver'

            elif selection == 'Volver':
                selection = 'Rules'
            
            selectBool = True
            
        
        elif key == "x":
            if selection == 'Rules':
                currentMenu = 'Rules'
                mostrar_menuX2_1()
            elif selection == 'Puntuacion':
                currentMenu = 'Puntuacion'
                mostrar_menuX2_2()
            elif selection == 'Volver':
                selection = 'Instrucciones'
                currentMenu = 'Principal'
                mostrar_menuX1()
                
        elif key == "z":
                selection = 'Instrucciones'
                currentMenu = 'Principal'
                mostrar_menuX1()            
        
    if selectBool == True: # El menu solo se mostrará cuando se tenga que actualizar
        mostrar_menuX2()


#----------------------------------------------------Funcion para salir del menu de reglas del juego<
def moverse_menuX2_1():
    
    global selection
    global currentMenu
    
    
    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == "x" or key == "z":
            selection = 'Rules'
            currentMenu = 'Instrucciones'
            mostrar_menuX2()

        
#---------------------------------------------------Funcion para salir del menu de Puntuacion de cartas<
def moverse_menuX2_2():
    
    global selection
    global currentMenu
    

    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == "x" or key == "z":
            selection = 'Puntuacion'
            currentMenu = 'Instrucciones'
            mostrar_menuX2()

#-------------------------------------------------------------Funcion para salir del menu de Resultados<

def moverse_menuX3():
    
    
    global selection
    global currentMenu
    

    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == "x" or key == "z":
            selection = 'Registro'
            currentMenu = 'Principal'
            mostrar_menuX1()
 

#------------------------------------------------------------------Funciones de Pantallas

#------------------------------------------------------Mostrar el menu principal<
def mostrar_menuX1():
    
    global selection
    
    borrar_pantalla()
    print(' __________________________________________________________________')
    print('|                                 |                                |')
    print('|            BRISCARD             |           version 1.0          |')
    print('|_________________________________|________________________________|')
    print('|                                                                  |')
    if selection == 'Jugar':
        print('|                       [x]>    Jugar                              |')
    else:
        print('|                               Jugar                              |')
    print('|                                                                  |')
    if selection == 'Registro':
        print('|                      [x]>   Registros                            |')
    else:
        print('|                             Registros                            |')
    print('|                                                                  |')
    if selection == 'Instrucciones':
        print('|                   [x]>    Instrucciones                          |')
    else:
        print('|                           Instrucciones                          |')
    print('|                                                                  |')
    if selection == 'Salir':
        print('|                       [x]>    Salir                              |')
    else:
        print('|                               Salir                              |')
    print('|                                                                  |')
    print('|__________________________________________________________________|')
    print('')
    print('      Controles')
    print(' __________________')
    print('|                  |')
    print('| Arriba:      [W] |')
    print('| Abajo:       [S] |')
    print('| Seleccionar: [X] |')
    print('| Atras:       [Z] |')
    print('|__________________|\n')

    moverse_menuX1()
    


#--------------------------------------------------------------------------------------------------------------------------------Mostrar el menu de instrucciones<

def mostrar_menuX2():
    
    global selection
    
    borrar_pantalla()
    print(' __________________________________________________________________')
    print('|                                 |                                |')
    print('|            BRISCARD             |          Instrucciones         |')
    print('|_________________________________|________________________________|')
    print('|                                                                  |')
    if selection == 'Rules':
        print('|                 [x]>   Reglas de los turnos                      |')
    else:
        print('|                        Reglas de los turnos                      |')
    print('|                                                                  |')
    if selection == 'Puntuacion':
        print('|              [x]>    Puntuacion de las cartas                    |')
    else:
        print('|                      Puntuacion de las cartas                    |')
    print('|                                                                  |')
    if selection == 'Volver':
        print('|                       [x]>    Volver                             |')
    else:
        print('|                               Volver                             |')
    print('|                                                                  |')        
    print('|__________________________________________________________________|')
    print('')
    print('      Controles')
    print(' __________________')
    print('|                  |')
    print('| Arriba:      [W] |')
    print('| Abajo:       [S] |')
    print('| Seleccionar: [X] |')
    print('| Atras:       [Z] |')
    print('|__________________|\n')

    moverse_menuX2()
    

#-----------------------------------------------------------------------------------------------------------------------------Mostrar el menu de reglas del juego<

def mostrar_menuX2_1():
    
    global selection
    
    borrar_pantalla()
    print(' __________________________________________________________________')
    print('|                                 |                                |')
    print('|            BRISCARD             |      Reglas de los turnos      |')
    print('|_________________________________|________________________________|')
    print('|                                                                  |')
    print('|   Al iniciar la partida el turno se elige aleatoriamente, pero   |')
    print('|   cuando la primera ronda termina, empieza sacando carta el      |')
    print('|   jugador que ha ganado anteriormente.                           |')
    print('|                                                                  |')
    print('|   Ese jugador seguira sacando carta primero hasta que pierda.    |')
    print('|                                                                  |')        
    print('|__________________________________________________________________|')
    print('')
    print('      Controles')
    print(' __________________')
    print('|                  |')
    print('| Arriba:      [W] |')
    print('| Abajo:       [S] |')
    print('| Seleccionar: [X] |')
    print('| Atras:       [Z] |')
    print('|__________________|\n')

    moverse_menuX2_1()



#-------------------------------------------------------Mostrar el menu de puntuacion de las cartas<
def mostrar_menuX2_2():
    
    global selection
    
    borrar_pantalla()
    print(' __________________________________________________________________')
    print('|                                 |                                |')
    print('|            BRISCARD             |    Puntuacion de las cartas    |')
    print('|_________________________________|________________________________|')
    print('|                                                                  |')
    print('|              01   =>  11 pts          06   =>  -- pts            |')
    print('|              02   =>  -- pts          07   =>  -- pts            |')
    print('|              03   =>  10 pts          10   =>   2 pts            |')
    print('|              04   =>  -- pts          11   =>   3 pts            |')
    print('|              05   =>  -- pts          12   =>   4 pts            |')
    print('|                                                                  |')
    print('|  El jugador que saca primero decide el palo que debe sacar       |')
    print('|  el adversario, si este saca un palo diferente y no es del mismo |')
    print('|  que la carta dominante, pierde automaticamente.                 |')
    print('|                                                                  |')
    print('|  En cambio, si la carta que saca el adversario es del palo       |')
    print('|  dominante y la del otro jugador no lo era, gana siempre aquel   |')
    print('|  que ha lanzado la carta del palo dominante.                     |')
    print('|                                                                  |')
    print('|  En el caso de que ambos hayan lanzado cartas del mismo palo     |')
    print('|  se tendrá en cuenta la puntuacion de las cartas para determinar |')
    print('|  el ganador de la ronda.                                         |')                                                                                                                                
    print('|__________________________________________________________________|')
    print('')
    print('      Controles')
    print(' __________________')
    print('|                  |')
    print('| Arriba:      [W] |')
    print('| Abajo:       [S] |')
    print('| Seleccionar: [X] |')
    print('| Atras:       [Z] |')
    print('|__________________|\n')

    moverse_menuX2_2()








#-------------------------------------------------------Mostrar el menu de los resultados<


def mostrar_menuX3():
    
    global selection
    
    
    
    if not os.path.exists('Config/results.bcd'): # Si no existe el archivo, crea uno nuevo
        file = open('Config/results.bcd', 'w')

        file.write("0\n")
        file.write('0')
        file.close()
    
    file = open("Config/results.bcd", "r") # Lee el archivo y recoge los resultados
    currentUserMark = int(file.readline())
    currentMachMark = int(file.readline())
    file.close()
    
    
    
    
    file = open("Config/results.bcd", "r") # Lee el archivo y recoge los resultados
    currentUserMark = int(file.readline())
    currentMachMark = int(file.readline())
    file.close()    
    
    
    #---------------Formatea el resultado dependiendo del número de digitos de este
    
    # Para los resultados del jugador
    userBlankSpaces = 17
    
    for i in range(0,len(str(currentUserMark))):
        userBlankSpaces -= 1
    
    userSpaces = ''
    
    for i in range (0,userBlankSpaces):
        userSpaces = userSpaces + ' '
    
    
    
    # Para los resultados de la máquina
    
    machBlankSpaces = 14
    
    for i in range(0,len(str(currentMachMark))):
        machBlankSpaces -= 1
    
    machSpaces = ''
    
    for i in range (0,machBlankSpaces):
        machSpaces = machSpaces + ' '
    
    
    
    
    borrar_pantalla()
    print(' __________________________________________________________________')
    print('|                                 |                                |')
    print('|            BRISCARD             |            Registro            |')
    print('|_________________________________|________________________________|')
    print('|                                                                  |')
    print('|                                                                  |')
    print('|' + machSpaces + 'La máquina ha ganado en total ' + str(currentMachMark) + ' partidas             |')
    print('|                                                                  |')
    print('|' + userSpaces + 'Tu has ganado en total ' + str(currentUserMark) +' partidas                 |')
    print('|                                                                  |')                                                                                                                              
    print('|__________________________________________________________________|')
    print('')
    print('      Controles')
    print(' __________________')
    print('|                  |')
    print('| Arriba:      [W] |')
    print('| Abajo:       [S] |')
    print('| Seleccionar: [X] |')
    print('| Atras:       [Z] |')
    print('|__________________|\n')

    moverse_menuX3()








#--------------------------------------------------------Muestra la pantalla pricipal
def pantalla_principal():
    
    
    borrar_pantalla()
    print(' __________________________________________________________________')
    print('|                                                                  |')
    print('|                       BIENVENIDO A BRISCARD                      |')
    print('|__________________________________________________________________|')
    print('|                ______      _                       _             |')
    print('|               |  ___ \    (_)                     | |            |')
    print('|               |  |_/ /_ __ _ ___  ___ __ _ _ __ __| |            |')
    print('|               |  ___ \  __| / __|/ __/ _  |  __/ _  |            |')
    print('|               |  |_/ / |  | \__ \ (_| (_| | | | (_| |            |')
    print('|                \____/|_|  |_|___/\___\__,_|_|  \__,_|            |')
    print('|                                                                  |')
    print('|                     Pulsa [ENTER] para continuar                 |')
    print('|                                                                  |')
    print('|__________________________________________________________________|')
    print('')
    print('      Controles')
    print(' __________________')
    print('|                  |')
    print('| Arriba:      [W] |')
    print('| Abajo:       [S] |')
    print('| Seleccionar: [X] |')
    print('| Atras:       [Z] |')
    print('|__________________|\n')

    moverse_menuX1()
    choice = input('')





#----------------------------------------------------------Loop funcional del menu


def showmenu():
    mostrar_menuX1()
    global currentMenu
    
    currentMenu = 'Principal'
    
    exitMenu = False
    mostrar_menuX1()

    while exitMenu == False:

        if currentMenu == 'Principal':
            moverse_menuX1()
        elif currentMenu == 'Instrucciones':
            moverse_menuX2()
        elif currentMenu == 'Rules':
            moverse_menuX2_1()
        elif currentMenu == 'Puntuacion':
            moverse_menuX2_2()
        elif currentMenu == 'Registro':
            moverse_menuX3()
        elif currentMenu == 'RetryMenu':
            moverse_RetryMenu()
    
        time.sleep(0.1) #Tiempo de refresco de respuesta (evita el sobrecalentamiento)
        
        
pantalla_principal()
currentMenu = 'Principal'
showmenu()