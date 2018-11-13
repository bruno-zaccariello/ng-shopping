import random as r
import string as s

choices = s.ascii_letters + s.digits

def pick(length):
    for i in range(length):
        yield r.choice(choices)

def genToken():
    return ''.join(x for x in pick(14))

def TokenError():
    pass