import random
from .iostream import std

def srand(seed: int):
    random.seed(seed)

def rand() -> int:
    return random.randint(0, 2**31 - 1)


#-----------------------
# ADD TO THE std CLASS
#-----------------------

std.srand = srand
std.rand = rand
