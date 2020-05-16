#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #    
    diccionario = string.ascii_letters + string.digits + string.punctuation

    """
    token_array = random.choices(diccionario,k=passLen)
    
    token = ''
    for caracter in token_array:
        token = token + caracter

    return token
    """

    token = "".join(random.choice(diccionario) for x in range(passLen))

    return token
    #
    #
    return ""

#longitud = input("Longitud: ")
#print(RandomPasswordGenerator(int(longitud)))