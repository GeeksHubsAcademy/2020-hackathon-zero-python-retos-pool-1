#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    caracteres = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
    password =''
    for i in range(passLen):
        password += random.choice(caracteres) 
    print("Contraseña: " + password)
    return password

RandomPasswordGenerator()
