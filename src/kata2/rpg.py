#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):

    password = ""

    password = password + "".join(random.choices(string.ascii_letters))
    password = password + "".join(random.choices(string.digits))
    password = password + "".join(random.choices(string.punctuation))
    password = password + "".join(random.choices(string.ascii_letters + string.digits +string.punctuation, k=passLen-3))

    return password
