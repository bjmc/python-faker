import random

from faker.generators.utils import numerify

"""Generator module for phone numbers.
For details about valid North American phone numbers
refer to http://en.wikipedia.org/wiki/NANP#Current_system
"""

formats = [
    '+##-+##-####',
    '(+##)+##-####',
    '1-+##-+##-####',
    '+##.+##.####',
    '+##-+##-####',
    '(+##)+##-####',
    '1-+##-+##-####',
    '+##.+##.####',
    '+##-+##-#### x###',
    '(+##)+##-#### x###',
    '1-+##-+##-#### x###',
    '+##.+##.#### x###',
    '+##-+##-#### x####',
    '(+##)+##-#### x####',
    '1-+##-+##-#### x####',
    '+##.+##.#### x####',
    '+##-+##-#### x#####',
    '(+##)+##-#### x#####',
    '1-+##-+##-#### x#####',
    '+##.+##.#### x#####'
]

def phone_number():
    return numerify(random.choice(formats))
