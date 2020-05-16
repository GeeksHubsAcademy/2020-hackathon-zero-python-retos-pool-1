from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player == ai:
        return 'Empate!'
    if (player == "Piedra" and ai == "Tijeras") or (player == "Papel" and ai == "Piedra") or (player == "Tijeras" and ai =="Papel"):
        return 'Ganaste!'
    else:
        return 'Perdiste!'

# Entry Point
def Game():
    print("elige entre piedra, papel o tijeras!")
    selection = input()
    if selection.lower() == "piedra":
        player = "Piedra"
    elif selection.lower() =="papel":
        player = "Papel"
    elif selection.lower() =="tijeras":
        player = "Tijeras"
    else:
        print("seleccion incorrecta")

    ai_number = random.randint(0,2)
    if ai_number ==0:
        ai = "Piedra"
    elif ai_number ==1:
        ai = "Papel"
    else:
        ai = "Tijeras"
    winner = quienGana(player, ai)

    print(winner)

