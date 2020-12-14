#Imports
import os
import msvcrt
import time
import Briscard

selection = 'Retry'




def borrar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')



def moverse_RetryMenu():
    
    global selection
    
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
                pass
            elif selection == 'Volver':
                Briscard.mostrar_menuX1()

        
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
    
    
    
    
running = True

RetryMenu()
    
def ShowRetryMenu():
    
    
    while running == True:
        moverse_RetryMenu()