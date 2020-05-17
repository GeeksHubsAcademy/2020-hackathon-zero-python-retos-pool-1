#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    allowedChars = string.ascii_lowercase
    generatedSequence = []

    for i in range(passLen):
        generatedSequence.append(random.choice(allowedChars)) 

    return ''.join(generatedSequence)
