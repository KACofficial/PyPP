from cpp.std import std

import cpp.iostream # #include <iostream> for input output stuff


def main() -> int:
    name: str 
    std.cout << "Enter a name: "
    name = std.cin >> str # C++ version is just `std::cin >> name;`, its almost like python isn't meant for this.
    std.cout << "You entered: " << name << std.endl
    return 0

std.set_main_function(main)