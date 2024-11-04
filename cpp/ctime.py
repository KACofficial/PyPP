from .iostream import std
import time as t

class time_t:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return str(self.value)
    
    def __int__(self):
        return self.value

def time() -> time_t:
    return int(t.time())

#-----------------------
# ADD TO THE std CLASS
#-----------------------

std.time = time

std.time_t = time_t