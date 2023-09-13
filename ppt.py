import random

#0 - Piedra
#1 - Papel
#2 - Tijera

def numero_a_nombre(numero):
    if numero == 0:
        return "Piedra"
    elif numero == 1:
        return "Papel"
    elif numero == 2:
        return "Tijera"
    else:
        return "Número fuera de rango"

def nombre_a_numero(nombre):
    if nombre == "Piedra":
        return 0
    elif nombre == "Papel":
        return 1
    elif nombre == "Tijera":
        return 2
    else:
        return -1

def juego(opcion_jugador):
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

    print(f"El usuario seleccionó {nombre_jugador}")
    print(f"La computadora seleccionó {nombre_computadora}")
    print(resultado)
    

def inicio():
    opcion = int(input("0.-Piedra\n1.-Papel\n2.-Tijera\nSeleccione una opción: "))
    juego(opcion)


inicio()
