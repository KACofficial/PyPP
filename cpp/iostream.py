from .std import std
from typing import Callable, Union, Type

class Cout:
    def __lshift__(self, a: Union[str, Callable]):
        if callable(a):
            print(a(), end="")
        else:
            print(a, end="")
        return self

class Cin:
    def __rshift__(self, var_type: Type) -> Union[int, float, str, None]:
        user_input = input()
        try:
            return var_type(user_input)
        except ValueError:
            print("Input type error! Please enter a valid value.")
            return None

def Endl() -> str:
    return "\n"

def Flush():
    sys.stdout.flush()


#-----------------------
# ADD TO THE std CLASS
#-----------------------

std.cout = Cout()
std.cin = Cin()

std.endl = Endl
std.flush = Flush