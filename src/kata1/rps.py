from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):

    result = ""

    player = player.lower()
    ai = ai.lower()

    if player == "piedra":
        if ai == "papel":
            result = "Perdiste!"
        elif ai == "tijeras":
            result = "Ganaste!"
        else:
            result = "Empate!"
    elif player == "papel":
        if ai == "papel":
            result = "Empate!"
        elif ai == "tijeras":
            result = "Perdiste!"
        else:
            result = "Ganaste!"
    else:
        if ai == "papel":
            result = "Ganaste!"
        elif ai == "tijeras":
            result = "Empate!"
        else:
            result = "Perdiste!"

    return result

# Entry Point
def Game():
    
    ai = options[randint(0, 2)]

    player = input("\nElige entre Piedra, Papel y Tijeras: ")
    
    winner = quienGana(player, ai)

    print(winner)

