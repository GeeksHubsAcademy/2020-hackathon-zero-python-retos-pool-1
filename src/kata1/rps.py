from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    resultado = 'Perdiste!'
    piedra = '0'
    papel = '1'
    tijeras = '2'
    player = str(player)
    ai = str(ai)
    if player == piedra:
        if ai == piedra:
            resultado = 'Empate!'
        elif ai == tijeras:
            resultado = 'Ganaste!'
    elif player == papel:
        if ai == papel:
            resultado = 'Empate!'
        elif ai == piedra:
            resultado = 'Ganaste!'
    else:
        if ai == tijeras:
            resultado = 'Empate!'
        elif ai == piedra:
            resultado = 'Ganaste!'
    return resultado

# Entry Point
def Game():
    #programar
    #player = input("Escribe una opcion [0.Piedra - 1.Papel - 2.Tijera]: ")
    player = options[1]
    ai = randint(0,2)
    print("AI: "+ str(ai))
    print("Player: "+ player)
    winner = quienGana(player, ai)
     
    print(winner)

Game()