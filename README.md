# Brisca
Proyecto Programación 1r Trimestre




Objetivos

El objetivo de este proyecto es la creación de un juego de mesa en entorno texto mediante la cooperación del equipo de desarrollo utilizando la metodología Scrum.

El juego elegido es el famoso juego de cartas español denominado como “la Brisca”

El verdadero reto del juego será poder jugar, con resultado de ganar o perder partidas contra una IA muy básica y guardar dichos resultados.






Planificación

Por decisión unánime de los integrantes que lo conforman, el desarrollo del proyecto se dividirá en cuatro fases, la fase de investigación y desarrollo conceptual, la fase de traslado en entornos de programa, la fase de codificación y creación de funciones, y finalmente la fase de pruebas y corrección de errores.



IDC (Investigación y desarrollo conceptual)
En esta fase se procederá a buscar información sobre el funcionamiento del juego, estos datos se utilizarán para crear el pseudocódigo del programa y posteriormente presentarlo a la siguiente fase, los integrantes del equipo deberán identificar las reglas generales que componen el juego y hacer un esquema sobre las historias de usuario que se van a necesitar.



TEP (Traslado a entorno de programa)
Al haber creado las historias de usuario del programa, se creará el pseudocódigo y este deberá modificarse para adaptarse al lenguaje de programación en cuestión, en este caso Python 3, para ello se recogerán todas las historias de usuario redactadas y pasarlas a un lenguaje más técnico describiendo qué función interna llevarán a cabo sobre el programa principal.



CCF (Codificación y creación de funciones)
En esta fase es donde se creará el código de la aplicación, es una de las fases más importantes y duraderas del proyecto, en está se creará un archivo principal que recogerá todas las funciones relacionadas con el juego y su estructura. En otros dos archivos aparte se irán desarrollando en paralelo distintos menús o subprocesos que finalmente se fusionarán en el archivo principal mediante una adaptación de las variables y valores para que todo encaje correctamente.



PCE (Pruebas y corrección de errores)
Está es la última pero no menos importante fase de desarrollo, se incluirán en ella todas las pruebas unitarias y funcionales de las funciones del programa, se comprobará que todo el código esté estructurado, identificado y ordenado correctamente para la correcta interpretación y comprensión de este, aparte de que sea efectivo al ser ejecutado teniendo en cuenta las demás porciones de código.

		





# Creación del documento IDC

Cómo jugar a la brisca (2 personas)!!!

1 - Preparación.
1.1 Se adquiere una baraja de cartas española
1.2 Se sacan las cartas del sobre
1.3 Se descartan las cartas 8 y 9 de cada palo
1.4 Se barajan las cartas
1.5 Cada jugador recoge tres cartas
1.6 Se saca la carta del triunfo (la dominante)
1.7 Se elige el primer turno de forma aleatoria

2 - Jugar turnos.
	2.1 El jugador que tiene el turno primero saca una carta de las que tiene
	2.2 El siguiente jugador saca una cartas de las que posee
	2.3 Se comparan los valores y palos de esas dos cartas con la central
	2.4 Las reglas del turno surgen efecto y se decide un ganador
	2.5 El jugador que gana suma los puntos de las dos cartas tiradas
           2.6 El jugador que gana el turno es el primero en coger una carta de la baraja
	2.7 El jugador que ha ganado tiene el primer turno en la próxima jugada

3 - Finalizar la partida

	3.1 La partida finaliza cuando se acaban las cartas de la baraja
	3.1 Gana el jugador que haya conseguido más puntos en el proceso

4 - Reglas del turno
￫ Si un jugador saca una carta del palo dominante y el otro no, gana inmediatamente el jugador que la ha sacado.

￫ Si el jugador que saca primero tira la carta de un palo, y el otro jugador tira otra de distinto palo que no es el dominante, gana el  jugador que ha tirado primero ya que él decide qué palo se va a jugar esa ronda.

￫ Si los dos sacan la carta del mismo palo, se tendrá en cuenta la puntuación de las dos cartas para establecer el ganador.

￫Puntuación de las cartas - [1 = 11pts], [3 = 10pts], [10 = 2pts], [11 = 3pts], [12 = 4pts], [Resto = 0].










# Creación del documento TEP

￫Preparación

Crear la baraja de cartas
Crear una lista vacía de cartas[]

Para cada carta del palo de bastos (hasta 12):
	Crear una carta y añadir al mazo

Para cada carta del palo de espadas (hasta 12):
	Crear una carta y añadir al mazo

Para cada carta del palo de copas (hasta 12):
	Crear una carta y añadir al mazo

Para cada carta del palo de oros (hasta 12):
	Crear una carta y añadir al mazo

Aleatoriamente cambiar el orden de los elementos de la lista



Asignar cartas iniciales al jugador, a la máquina, y a la carta dominante
Crear una baraja del jugador vacía[]

Añadir la primera carta del montón a la baraja del jugador
Quitar la primera carta del montón de la lista de cartas totales
(x3)


Crear una baraja de la máquina vacía[]

Añadir la primera carta del montón a la baraja de la máquina
Quitar la primera carta del montón de la lista de cartas totales
(x3)

Carta dominante = Añadir la primera carta del montón
Quitar la primera carta del montón de la lista de cartas totales

Elegir el primer turno aleatoriamente
Elegir un número aleatorio entre el 0 y el 1:

Si el número sale 0:
Empieza un jugador

O si el número sale 1:
Empieza otro jugador


￫Jugar Turnos

Se crea un bucle donde se gestionan los turnos
Mientras queden cartas por jugar:

Si el turno es del jugador:
Se muestra la interacción del jugador()

O si el turno es de la máquina:
Se muestra la interacción de la máquina()


Interacción del jugador
Se mostrará por pantalla un menú muy chulo con información de la partida en curso

Se mostrará la primera carta del mazo del jugador
Se mostrará la segunda carta del mazo del jugador
Se mostrará la tercera carta del mazo del jugador

Se le pedirá al usuario que introduzca qué carta desea lanzar(1,2 o 3)
Se eliminará esa carta de la mano del usuario

Se asigna una carta de la máquina de las que tiene en su mazo
Se eliminará esa carta de la mano de la máquina

Se muestra otro bonito menú con las dos cartas lanzadas parecido al anterior

Se comparan los resultados()

Interacción de la máquina
Se asigna una carta de la máquina de las que tiene en su mazo
Se eliminará esa carta de la mano de la máquina

Se muestra un menú con la carta que ha lanzado la máquina y con información de la partida en curso

Se mostrará la primera carta del mazo del jugador
Se mostrará la segunda carta del mazo del jugador
Se mostrará la tercera carta del mazo del jugador

Se le pedirá al usuario que introduzca qué carta desea lanzar(1,2 o 3)
Se eliminará esa carta de la mano del usuario
Se comparan los resultados()

Comparar resultados
Recogemos la carta que ha lanzado el jugador
Recogemos la carta que ha lanzado la máquina

Si la carta del jugador es = 1:
Esa carta vale 11
O si la carta del jugador es = 2:
Esa carta vale 0.01
O si la carta del jugador es = 3:
Esa carta vale 10
O si la carta del jugador es = 4:
Esa carta vale 0.02
O si la carta del jugador es = 5:
Esa carta vale 0.03
O si la carta del jugador es = 6:
Esa carta vale 0.04
O si la carta del jugador es = 7:
Esa carta vale 0.05
O si la carta del jugador es = 10:
Esa carta vale 2
O si la carta del jugador es = 11:
Esa carta vale 3
O si la carta del jugador es = 12:
Esa carta vale 4

(Hacemos lo mismo con la carta de la máquina)

Si las cartas son distintas y la del jugador es del palo dominante y el de la máquina no:
Gana = el jugador
Suma puntos(Jugador)

O si las cartas son distintas y la carta de la máquina es del palo dominante y la del jugador no:
Gana = la máquina
Suma puntos(Máquina)

O si el palo del jugador es del mismo que el de la máquina:
Si el valor de la carta del jugador es mayor que la de la máquina:
Gana = el jugador
Suma puntos(Jugador)
O si no:
Gana = la máquina
Suma puntos(Máquina)

Si Gana = Jugador:
El turno es del jugador
O si no:
El turno es de la máquina

Si quedan cartas en el montón:
Se añade la primera carta del montón a la mano de la máquina
Se elimina la primera carta del montón
Se añade la primera carta del montón a la mano del jugador
Se elimina la primera carta del montón




Comparar resultados(Sumar puntos)
Si la suma de los puntos de la carta de la máquina y la del jugador supera a 1:
Si ha ganado el Jugador:
Se recogen los puntos del jugador y se le suman estos
O si ha ganado la Máquina:
Se recogen los puntos de la máquina y se le suman estos
Se pone si la puntuación de las cartas es mayor a 1, ya que las que valen 0,01, 0,02, etc. No suman nada, sólo se usa su valor para saber quién ha ganado el turno!



￫Terminar Partida

Cuando se rompe el bucle del juego
Si los puntos del jugador son  mayores que los de la máquina:
Gana la partida el Jugador
O si no:
Gana la máquina
//No puede haber empate

Se muestra un menú muy chulo que indica quién ha ganado

Se actualiza el archivo del registro y se le suma 1 a quien haya ganado(Jugador/Máquina)










# Creación del documento CCF

Sprints realizados durante el proceso de desarrollo del producto.




⟲Primer día

SCRUM MASTER = Jaume Tomás
Tiempo estimado: 3 horas
Tiempo real : 5 horas

Lo primero que vamos a hacer es declarar las variables que vamos a utilizar a lo largo de todo el código del juego. 
También hemos declarado algunos imports que nos pueden ser de gran ayuda para futuras funciones como el random, os, o sys

A continuación hemos empezado con las funciones. Hemos definido y probado la función que va a generar las cartas y hemos repartido las cartas al jugador y a la màquina. También hemos definido la función de borrar pantalla.

El siguiente paso ha sido programar cómo elegir el palo dominante (ya que en este juego es muy importante a la hora de contar los puntos) y el como elegir los turnos de juego.

Las últimas funciones que hemos definido son las de comprobar los puntos  y comprobar las cartas del ganador.


⟲Segundo día:

SCRUM MASTER = Jose Luis Saiz
Tiempo Estimado : 2 horas
Tiempo real: 2 horas y 30 minutos

Hemos programado la asignación de los puntos que corresponden al jugador y también a la máquina.
A continuación comprobamos los distintos tipos de resultados de cada turno: si el palo de la máquina es dominante o no, si lo es el del jugador o no

También hemos construido el “menú” principal que informa de cómo va la partida, tanto si el turno lo continua la máquina o el jugador. Lo hemos hecho definiendo diferentes funciones de acuerdo a quien gana/continúa el turno


⟲Tercer día.

SCRUM MASTER = Sandra Lopez
Tiempo estimado: 4 horas
Tiempo real : 7 horas

Hemos continuado definiendo los turnos en caso de que sea la máquina quien continúe el turno.
Posteriormente  hemos hecho el código para borrar las cartas del jugador y de la máquina cada vez que se tira una carta, y también lo que pasa cuando ya no quedan cartas en el mazo.
A continuación definimos la función que sirve para actualizar los resultados.
Y finalmente hemos conseguido hacer el bucle del juego. Para lograr este bucle tuvimos que repasar varias veces el código entero para revisar que fallaba, ya que surgieron unos cuantos errores, pero al final lo conseguimos hacer funcionar correctamente.


⟲Cuarto día

SCRUM MASTER = Jose Luis Saiz
Tiempo estimado : 8 horas
Tiempo real : 1d 

Hemos declarado la función del menú principal, la idea del menú es que podamos seleccionar mediante unos controles la opción deseada y también que se pueda retroceder si es necesario. En primer lugar, declaramos la función de mostrar el menú, esta función únicamente consiste en como se verá la interfaz del menú.
En segundo lugar, declaramos las variables del menú. Después de la declaración de las variables definimos varias funciones que nos permitan movernos por todo el menú mediante los controles ya mostrados al principio.
Finalmente, creamos distintas funciones para cada opción de nuestro menú. La opción de las instrucciones enseñará mediante otro uso de prints las instrucciones de nuestro juego ya sea la puntuación de las cartas como las reglas de los turnos. En cuanto a la opción de registro, hemos tenido algún que otro impedimento a la hora de hacer su función puesto que queríamos hacer un registro de todas las partidas realizadas y se nos ha hecho más complejo de lo que esperábamos.La función de registro consiste en crear un archivo de 2 líneas, la primera línea de arriba es el número de partidas que ha ganado el usuario y la segunda línea es el número de partidas que ha ganado la máquina. La función lee por líneas el archivo y guarda el número en una variable ya creada. Al final de cada partida, dependiendo del resultado le suma uno al usuario o a la máquina y por último reescribe el documento con los registros actualizados. Finalmente muestra el registro actualizado en la opción del menú.
Por otra parte, la opción de jugar te dirige directamente al juego con sus funciones explicadas anteriormente incorporadas. 
Finalmente, la opción de salir evidentemente sale del menú principal del juego.
Por otro lado, creamos una función llamada menú retry que lo que hace es que cada vez que acabe una partida se muestre un menú que te dé la opción de jugar otra vez o volver al menú principal. Cada opción junto a sus funciones ya explicadas anteriormente.












Creación del documento PCE

(Errores en las pruebas unitarias e integradas)

Fallo :
Los puntos no se suman al acabar la ronda (fallo de la variable de las cartas)

Solución :
Asignar las variables de puntos y de cartas como globales, podríamos haber hecho que fuesen paramétricas pero superan las 4 variables y mejor si las dejamos como globales.





Fallo :
Cuando al jugador le quedan menos de 3 cartas se produce un error en el índice de la lista.

Solución :
Poner otra condición en el menú del tablero y en la selección de opciones que cuente las cartas que le quedan al jugador y muestre diferentes opciones.





Fallo :
No acaba nunca la partida (error de índice en la lista de cartas de la máquina)

Solución :
Cambiar el orden en la que se ejecuta el bucle, haciendo que en cada turno se compruebe el total de cartas del jugador, y no las del mazo.
 



Fallo :
El menú principal no se muestra(no se reconoce la función)

Solución :
Cambiar de orden el código del programa, poniendo las funciones del menú principal a lo último.



Fallo :
El menú principal no deja de parpadear y el ordenador se empieza a sobrecalentar a los pocos segundos

Solución :
Hacer que en el código msvcrt sólo ejecute el evento de elegir opción y no la del refresco del menú, y que este sólo se actualice cuando se interactúa.


Fallo :
Al pasar de opción en el menú Retry se muestra el menú principal y no deja seleccionar nada

Solución :
Añadir la función ‘moverse_menuRetry()’ en el loop del menú principal.



Fallo :
Al volver a jugar no se restablecen por defecto los valores de la partida, dando un error de índice en las cartas del jugador y de la máquina.

Solución :
Crear una función que restablezca todas las variables esenciales de la partida a por defecto y se vuelvan a generar las cartas (añadir al menú Retry)


Fallo: 
El archivo de las partidas guardadas no se puede escribir (permiso denegado)

Solución :
Cambiar el componente ‘r’ (read) por el de ‘w’ (write) en el comando de ‘file.open()’



Fallo: 
Los resultados de las partidas desestructuran el menú cuando sobrepasan los dos dígitos.

Solución: 
Crear un bucle ‘for’ que cuente los dígitos de ambos resultados y les sume los espacios necesarios para que los bordes del menú se vean bien.



