from random import randint

TIE = 'Empate!'
WIN = 'Ganaste!'
LOSE = 'Perdiste!'

options = ["Piedra", "Papel", "Tijeras"]

player_option = {
    'Piedra' : {'Piedra': TIE, 'Papel': LOSE, 'Tijeras': WIN},
    'Papel': {'Piedra': WIN, 'Papel': TIE, 'Tijeras': LOSE},
    'Tijeras': {'Piedra': LOSE, 'Papel': WIN, 'Tijeras': TIE},
}

def quienGana(player, ai):
    player = player.capitalize()
    ai = ai.capitalize()
    
    return player_option[player][ai]

def Game():
    player = input('Introduce Piedra, Papel o Tijeras: ')
    ai = options[randint(0,2)]

    print ('Elejiste ' + player)
    print ('AI elijio ' + ai)
    
    winner = quienGana(player, ai)

    print(winner)
