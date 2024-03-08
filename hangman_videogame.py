## Importamos la libreria "random" para poder usar la aleatoridad.
import random
## Importamos la libreria "os" para poder utilizar comandos de consola.
import os

## Definimos la funcion principal que tomara el main al ejecutarse el codigo.
def run():

    ## Creamos una lista con las imagenes que utilizaremos para nuesto juego, usamos el formato ASCII.
    IMAGES = [ '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''  
  +---+
  |   |
      |
      |
      |
      |
=========''']
    
    ## Creamos una base de datos que contiene las palabras que se usaran para el juego.
    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP"
    ]

    ## La variable "word" toma una palabra aleatoria de la base de datos y la guarda para usarla mas adelante.
    word = random.choice(DB)
    ## La variable "spaces" crea una lista de espacios y le da la longitud de la variable "word", esta se dibuja mas adelante.
    spaces = ["_"] * len(word)
    ## La variable "attemps" hace referencia a las oportunidades de fallo que tenemos al jugar.
    attemps = 6

    ## Este while true sirve como una funcion de dibujado por fps ya que se repetira constantemente hasta que el juego se termine.
    while True:

        ## utilizamos la libreria "os" con el metodo "system" para ejecutar el comando "cls" en la ventana de comando para limpiar la pantalla y redibujar.
        os.system("cls")
        ## Con este for vamos a dibujar los espacios en blanco para simular cuantas letras tiene la palabra secreta.
        for character in spaces:
            ## En este print usamos el "end=" "" para que al hacer print no genere un salto de linea y todos los espacios queden uno al lado del otro.
            print(character, end=" ")
        ## Esto dibuja a nuestro orcado usando el "attemps" como indice para que se dibuje la imagen dependiendo de los intentos. Cabe aclarar que el dibujo tiene un salto de linea.
        print(IMAGES[attemps])
        ## Se le pide una letra al usuario para guardarla y ver si es correcta mas adelante.
        letter = input("Elige una letra: ").upper()
        
        ## Guardamos en "found" si se encontro o no la letra en la palabra secreta, de base se pone "False".
        found = False
        ## En este ciclo tomamos cada letra de la palabra secreta y su indice para ver si el usuario adivino.
        for idx, character in enumerate(word):
            ## Vemos si la letra es la que eligio el usuario.
            if character == letter:
                ## Si el usuario adivino cambiamos el espacio en blanco por la letra del usuario.
                spaces[idx] = letter
                ## Aclaramos que se encontro una letra.
                found = True
        
        ## Si el usuario no adivino con su letra elegida.
        if not found:
            ## Se resta una oportunidad.
            attemps -= 1
        
        ## Si no existen mas letras que adivinar.
        if "_" not in spaces:
            ## Limpiamos la pantalla.
            os.system("cls")
            ## Cartel de WIN.
            print("************** :D GANASTE **************")
            ## Este corte se utiliza para que el juego pare y no siga dibujandose, tambien esto permite liberar la ventana para que el usuario pueda hacer otra cosa.
            break
        
        ## Si te quedas sin oportunidades.
        if attemps == 0:
            ## Limpiamos la pantalla.
            os.system("cls")
            ## Cartel de GAME OVER.
            print("************** D: PERDISTE **************")
            ## Lo mismo que arriba :D.
            break

## Inicializar Main.
if __name__ == "__main__":
    ## Usamos la funcion antes implementada como primera linea.
    run()