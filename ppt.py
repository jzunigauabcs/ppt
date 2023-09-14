'''
    Juego Piedra, Papel o Tijera
    Las opciones a seleccionar son:
    0 - Piedra
    1 - Papel
    2 - Tijera
'''
import random

#Devuelve el nombre de la opción seleccionada
def numero_a_nombre(numero):
    if numero == 0:
        return "Piedra"
    elif numero == 1:
        return "Papel"
    elif numero == 2:
        return "Tijera"
    else:
        return "Número fuera de rango"

def juego(opcion_jugador):
    #Genera una opción aleatoria con rango de 0-2
    opcion_computadora = random.randrange(0, 3)

    diferencia = (opcion_jugador - opcion_computadora) % 3
    
    if diferencia == 0:
        resultado = "Los jugadores empataron"
    elif diferencia == 1 or diferencia == 3:
        resultado = "El jugador es el ganador"
    else:
        resultado = "La computadora es la ganadora"

    nombre_computadora = numero_a_nombre(opcion_computadora)
    nombre_jugador = numero_a_nombre(opcion_jugador)

    print("El usuario seleccionó {}".format(nombre_jugador))
    print("La computadora seleccionó {}".format(nombre_computadora))
    print(resultado)
    

def inicio():
    while True:
        opcion = int(input("0.-Piedra\n1.-Papel\n2.-Tijera\nSeleccione una opción: "))
        juego(opcion)
        opcion_juego = int(input("\n1.- Jugar de nuevo\n2.-Salir\nSeleccione una opción: "))
        if opcion_juego == 2:
            break

inicio()
