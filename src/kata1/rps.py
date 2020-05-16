from random import randint

options = ["Piedra", "Papel", "Tijeras"]

winers_rules = {"Piedra": "Tijeras", "Papel": "Piedra", "Tijeras": "Papel"}
# El resultado de salida son las siguientes String
# 'Empate!'
# 'Ganaste!'
# 'Perdiste!'


def quienGana(player, ai):
    if(player == ai):
        return "Empate!"
    elif(ai == winers_rules[player]):
        return "Ganaste!"
    else:
        return "Perdiste!"

# Entry Point


def Game():
    #
    #
    option_user = input("selecciones su opción : ")
    option_ia = options[randint(0, 2)]
    #
    #

    winner = quienGana(option_user, option_ia)
    print("Elegiste:", option_user)
    print("AI:", option_ia)

    print(winner)


Game()
