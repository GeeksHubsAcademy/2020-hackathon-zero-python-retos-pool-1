from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player_cap = player.lower().capitalize()
    ai_cap = ai.lower().capitalize()
    if player_cap == 'Piedra' and ai_cap == 'Piedra':
        return 'Empate!'
    if player_cap == 'Papel' and ai_cap == 'Papel':
        return 'Empate!'
    if player_cap == 'Tijeras' and ai_cap == 'Tijeras':
        return 'Empate!'
    if player_cap == 'Piedra' and ai_cap == 'Papel':
        return 'Perdiste!'
    if player_cap == 'Papel' and ai_cap == 'Tijeras':
        return 'Perdiste!'
    if player_cap == 'Tijeras' and ai_cap == 'Piedra':
        return 'Perdiste!'
    if player_cap == 'Piedra' and ai_cap == 'Tijeras':
        return 'Ganaste!'
    if player_cap == 'Papel' and ai_cap == 'Piedra':
        return 'Ganaste!'
    if player_cap == 'Tijeras' and ai_cap == 'Papel':
        return 'Ganaste!'
    return ""

# Entry Point
def Game():
    #
    #
    player = input("Escoge (Piedra, Papel o Tijera):")
    value_ia = randint(0, 2)
    ai = options[value_ia]
    #
    #
    print(player, ai)
    winner = quienGana(player, ai)

    print(winner)
Game()
