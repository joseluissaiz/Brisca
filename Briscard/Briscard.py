##TRABAJO CONJUNTO REALIZADO POR JOSE LUIS, SANDRA Y JAUME#
version = "1.0"
#Nombre del proyecto - BrisCards

#Este archivo contiene el menu del juego



#------------------------------------------------------Comentarios de los integrantes

# 25/11/2020 - Jose: Le ha dado un toque personal al menú
#                    añadiendo un poco de ASCII
#
#                    [!] import msvcrt -> La app solo correrá 
#                                         en windows.



#Imports
import os
import msvcrt
import time


#-----------------------------------------------------------------------------------Funciones del sistema operativo
#Borrar pantalla
def borrar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')


#-------------------------------------------------------------------------------------Variables del menu
selection = 'Jugar'




#-------------------------------------------------------------------------------------Funciones de movimiento

#------------------------------------------------------Funcion para moverse dentro del menu principal<
def moverse_menuX1():
    
    global selection
    global currentMenu
    global exit
    
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
                os.system("Brisca.py")
                exit = True
            elif selection == 'Salir':
                exit = True
        
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
    
    selectBool = False # Esta variable evita que el menu parpadee infinitamente

    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == "x" or key == "z":
            selection = 'Rules'
            currentMenu = 'Instrucciones'
            mostrar_menuX2()

        
    if selectBool == True: # El menu solo se mostrará cuando se tenga que actualizar
        mostrar_menuX2_1()
        
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
mostrar_menuX1()

currentMenu = 'Principal'
selection = 'Jugar'
exit = False
pantalla_principal()
mostrar_menuX1()

while exit == False:

    if currentMenu == 'Principal':
        moverse_menuX1()
    elif currentMenu == 'Instrucciones':
        moverse_menuX2()
    elif currentMenu == 'Rules':
        moverse_menuX2_1()
    elif currentMenu == 'Puntuacion':
        moverse_menuX2_2()
    
    time.sleep(0.1) #Tiempo de refresco de respuesta (evita el sobrecalentamiento)





        

        
        
        
        
        
        
