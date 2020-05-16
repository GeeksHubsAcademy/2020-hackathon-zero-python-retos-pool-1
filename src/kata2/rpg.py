#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    letters = string.ascii_lowercase
    letters += string.ascii_uppercase
    letters += string.digits
    letters += string.punctuation

    randString = ''.join(random.choice(letters) for i in range(passLen))
    
    return randString

RandomPasswordGenerator()