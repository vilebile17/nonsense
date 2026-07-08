from sys import argv
from typing import List, Self, Tuple


class PolynomialPart:
    # a(x-k1)(x-k2)...(x-kn)
    def __init__(self, k: List[float], a: float = 1) -> None:
        self.coefficient = a
        self.constants = k

    # basically just substituting the x value in
    def value(self, x: float) -> float:
        result = self.coefficient
        for constant in self.constants:
            result *= x - constant
        return result

    def __repr__(self) -> str:
        result = f"{round(self.coefficient, 4)}"
        for k in self.constants:
            result += f"(x - {round(k, 3)})"
        return result

    def update_coefficient(
        self, poly_so_far: List[Self], coord: Tuple[float, float]
    ) -> None:
        x = coord[0]
        y = coord[1]
        lhs = y - sum([pp.value(x) for pp in poly_so_far])

        self.coefficient = 1
        rhs = self.value(x)
        self.coefficient = lhs / rhs


def parse_coordinate(coord: str) -> Tuple[float, float]:
    if coord[0] != "(" or coord[-1] != ")" or coord.count(",") != 1:
        raise ValueError(
            "Invalid coordinate, must be of the format (x,y); try 'python3 function_finder.py --help'"
        )

    x = ""
    y = ""
    foundComma = False
    for char in coord[1:-1]:
        if char == ",":
            foundComma = True
            continue

        if foundComma:
            y += char
        else:
            x += char

    x_num = 0
    y_num = 0
    try:
        x_num = float(x)
        y_num = float(y)
    except Exception as e:
        raise ValueError(
            f"Invalid coordinate: {e}, try python3 function_finder.py --help if you're confused"
        )

    return (x_num, y_num)


def print_polynomial(polynomial: List[PolynomialPart]):
    if len(polynomial) == 0:
        print()
        return

    result = f"f(x) = {str(polynomial[0])} "
    for part in polynomial[1:]:
        if part.coefficient != 0:
            result += f"+ {part} "

    print(result)


def find_value(polynomial: List[PolynomialPart], x: float) -> float:
    return sum(pp.value(x) for pp in polynomial)


def main():
    if "--help" in argv or "-h" in argv or len(argv) == 1:
        print("function_finder.py finds a function given a list of coordinates")
        print()
        print("USAGE: python3 function_finder.py '(x1,y1)' '(x2,y2)' ... '(xn,yn)'")
        print("Note that each coordinate must be surrounded by quotation marks due")
        print("to the way that the terminal parses brackets")
        print()
        print("E.g. python3 function_finder.py '(0,8)' '(5,33)' '(2,6)' ")
        return

    coords = []
    for coord in argv[1:]:
        coords.append(parse_coordinate(coord))

    polynomial: List[PolynomialPart] = [PolynomialPart([], a=coords[0][1])]
    for i in range(1, len(coords)):
        pp = PolynomialPart([coord[0] for coord in coords[:i]])
        pp.update_coefficient(polynomial, coords[i])
        polynomial.append(pp)

    print_polynomial(polynomial)


if __name__ == "__main__":
    main()
