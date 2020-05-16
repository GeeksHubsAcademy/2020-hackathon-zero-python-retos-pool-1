#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = passLen

    return ''.join(random.choice(chars) for x in range(size))
