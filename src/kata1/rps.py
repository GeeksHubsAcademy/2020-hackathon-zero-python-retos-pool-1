from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):

    # Pasamos las opciones recibidad a minusculas para que no pueda haber fallos
    player = player.lower()
    ai = ai.lower()

    # Si son iguales
    if player == ai:
        return 'Empate!'
    # Piedra gana a tijeras
    elif player == "piedra" and ai == "tijeras":
        return "Ganaste!"
    # Papel gana a piedra
    elif player == "papel" and ai == "piedra":
        return "Ganaste!"
    # Tijeras gana a papel
    elif player == "tijeras" and ai == "papel":
        return "Ganaste!"
    # Si no es ninguna de las opciones anteriores quiere decir que pierdo
    return "Perdiste!"

# Entry Point
def Game():

    # Pregunta al usuario su eleccíon
    player = input("¿Piedra, Papel o Tijeras?")
    print("JUGADOR: " + player)
    
    # Utilizamos el randint para sacar una opción de la lista de opciones
    ai = options[randint(0,2)]
    print("MÁQUINA: " + ai)
    
    # Asignamos a la variable winner la función quienGana
    winner = quienGana(player, ai)
    
    # Imprimimos resultado
    print("RESULTADO: " + winner)

Game()
