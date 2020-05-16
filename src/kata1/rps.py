from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player_choice = player.lower()
    ai_choice = ai.lower()

    if player_choice == ai_choice:
        return "Empate!"
    elif player_choice == "piedra" and ai_choice == "papel":
        return "Perdiste!"
    elif player_choice == "papel" and ai_choice == "tijeras":
        return "Perdiste!"
    elif player_choice == "tijeras" and ai_choice == "piedra":
        return "Perdiste!"
    else:
        return "Ganaste!"

# Entry Point
def Game():
    #
    #
    
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)

