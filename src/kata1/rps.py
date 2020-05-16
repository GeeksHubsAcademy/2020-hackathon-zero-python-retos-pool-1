from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    resultado = ''
    
    player = player.lower()
    ai = ai.lower()
    
    if player == ai:
        resultado = 'Empate!'
    elif "piedra" == player:
        if ai == "papel":
            resultado = 'Perdiste!'
        else:
            resultado = 'Ganaste!'
    elif "papel" == player:
        if "piedra" == ai:
            resultado = 'Ganaste!'
        else:
            resultado = 'Perdiste!'
    else:
        if "piedra" == ai:
            resultado = 'Perdiste!'
        else:
            resultado = 'Ganaste!'
    return resultado

# Entry Point
def Game():
    # Eleccion usuario
    player = input()
    
    # Elección AI
    ai = options[randint(0, 2)]
    winner = quienGana(player, ai)

    print(winner)

Game()