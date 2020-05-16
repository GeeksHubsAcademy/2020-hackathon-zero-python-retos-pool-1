#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #    
    diccionario = string.ascii_letters + string.digits + string.punctuation

    token_array = random.choices(diccionario,k=passLen)
    
    token = ''
    for caracter in token_array:
        token = token + caracter

    #token = 'a'
    #objeto = (chr in token for chr in string.ascii_letters)

    #for kk in objeto:
    #    print (kk)

    return (token)
    #
    #
    return ""
