# Python++

Porting C++ syntax and basic functions to Python.

# Repository Structure
- `cpp/iostream.py` is the code for porting `<iostream>` to python, with the functions `std::cin`, `std::cout`, `std::endl`, and `std::flush`
- `cpp/std.py` is the code for adding the `std` class, `from cpp.std import std` is required every time you use this library.
- `cpp/cstdlib.py` is the code for porting `<cstdlib>` to python, with the functions `std::srand` and `std::rand`
- `cpp/ctime.py` is the code for porting `<ctime>` to python, with the type `std::time_t` and the function `std::time()`
