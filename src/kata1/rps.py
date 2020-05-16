from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):    
    player = player.lower()
    ai = ai.lower()

    if (player == ai):
        return "Empate!"
    
    #Piedra gana
    if (player=="piedra" and ai=="tijeras"):
        return "Ganaste!"
    
    #Piedra pierde
    if (player=="piedra" and ai=="papel"):
        return "Perdiste!"

    #Papel gana
    if (player=="papel" and ai=="piedra"):
        return "Ganaste!"
    
    #Papel pierde
    if (player=="papel" and ai=="tijeras"):
        return "Perdiste!"

    #Tijeras gana
    if (player=="tijeras" and ai=="papel"):
        return "Ganaste!"
    
    #Papel pierde
    if (player=="tijeras" and ai=="piedra"):
        return "Perdiste!"

    return ""

# Entry Point
def Game():
    #
    #
    player = input("Escribe [Piedra,Papel,Tijeras]: ")

    ai = options[randint(0,2)]

    print ("Player: " + player + " vs " + ai)
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)