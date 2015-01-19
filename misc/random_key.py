from random import choice
from string import ascii_uppercase, digits

def random_key(format, size):
	chars = ascii_uppercase + digits
	ret = format + ''.join(choice(chars) for _ in range(size))
	return ret

