#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    letters_digits = string.ascii_letters + string.digits
    password = "".join(random.choice(letters_digits) for i in range(passLen))
    return password
    #
    #

RandomPasswordGenerator()
