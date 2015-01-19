## Random ID For Database Id
import string
import random

def random_key(format, size):
    chars=string.ascii_uppercase + string.digits
    return format + ''.join(random.choice(chars) for _ in range(size))
