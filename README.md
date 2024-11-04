# Python++

Porting C++ syntax and basic functions to Python.

## Repository Structure
- `cpp/iostream.py` is the code for porting `<iostream>` to python, with the functions `std::cin`, `std::cout`, `std::endl`, and `std::flush`
- `cpp/std.py` is the code for adding the `std` class, `from cpp.std import std` is required every time you use this library.
- `cpp/cstdlib.py` is the code for porting `<cstdlib>` to python, with the functions `std::srand` and `std::rand`
- `cpp/ctime.py` is the code for porting `<ctime>` to python, with the type `std::time_t` and the function `std::time()`

# Features
- Fully functional `std::cout` and `std::endl` works just like `C++` does.
- Can use arguments `argc: int, argv: list` just like `C++`'s `int argc, char *argv[]`.
- Very fast, little to no time loss between our `std.cout` vs. the default `print()`.

## Examples
#### Below are a list of examples, with comments showing what the C++ version of each line is.
Reading input and printing said input
```python
from cpp.std import std # Always required

import cpp.iostream # #include <iostream>


def main() -> int:
    name: str # std::string name;
    std.cout << "Enter a name: " # std::cout << "Enter a name: ";
    name = std.cin >> str # std::cin >> name;
    std.cout << "Hello, " << name << std.endl # std::cout << "Hello, " << name << std::endl;
    return 0 # return 0;

std.set_main_function(main) # tell the library what your main functions is, required
```
Printing random numbers, seeded with the current unix time
```python
from cpp.std import std # Always required

import cpp.iostream # #include <iostream>
import cpp.cstdlib # #include <cstdlib>
import cpp.ctime # #include <ctime>

def main():
    current_time: std.time_t = std.time() # std::time_t current_time = std::time();
    std.srand(current_time) # std::srand(current_time);
    rand_int: int = std.rand() % 101 # int rand_int = std::rand() % 101;
    std.cout << rand_int << std.endl # std::cout << rand_int << std::endl
    return 0 # return 0;

std.set_main_function(main) # tell the library what your main functions is, required
```