import random
import re
import string

numerify_re = re.compile('#|\+')
letterify_re = re.compile(r'\?')

def _numerify_helper(match_obj):
    if match_obj.group() == '+':
        return str(random.randint(2, 9))
    else:
        return str(random.randint(0, 9))

def numerify(number_string):
    return numerify_re.sub(_numerify_helper, number_string)

def letterify(letter_string):
    return letterify_re.sub(lambda m: random.choice(string.ascii_letters), letter_string)

def bothify(s):
    return letterify(numerify(s))
