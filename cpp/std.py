import sys
from typing import Callable
import inspect

class Std:
    def set_main_function(self, m: Callable):
        # Check the number of arguments `m` accepts
        if callable(m):
            params = inspect.signature(m).parameters
            if len(params) == 2:
                # Call with arguments if it expects two parameters
                sys.exit(m(len(sys.argv), sys.argv))
            elif len(params) == 0:
                # Call without arguments if it expects none
                sys.exit(m())
            else:
                raise TypeError("Function must accept either 0 or 2 arguments.")
        else:
            raise TypeError("Provided argument is not callable.")


std = Std()
