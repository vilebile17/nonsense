from typing import List, Self, Tuple, Mapping
from sys import argv


class PolynomialPart:  # idk what else to call it
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

    def convert_to_powers(self):
        powers = {}

        # This part creates a binary number that is len(self.constants) digits long.
        # This is used to multiply each term in each bracket with each term in every
        # other bracket. E.g 0b110 for the brackets (x + a)(x + b)(x + c) means multiply
        # the second two terms in the first two brackets and the first term in the
        # last bracket i.e a * b * x

        for i in range(2 ** len(self.constants)):
            bin_repr = bin(i)[2:]  # Removes the 0b prefix

            while len(bin_repr) < len(self.constants):
                bin_repr = "0" + bin_repr

            result = self.coefficient
            current_power = 0
            for j in range(len(self.constants)):
                if bin_repr[j] == "1":
                    result *= -self.constants[j]
                else:
                    current_power += 1

            if current_power in powers:
                powers[current_power] += result
            else:
                powers[current_power] = result

        return powers


def add_polynomial_parts(polynomial: List[PolynomialPart]) -> Mapping[int, float]:
    all_powers = [pp.convert_to_powers() for pp in polynomial]

    result = {}
    for powers in all_powers:
        for key in powers:
            if key in result:
                result[key] += powers[key]
            else:
                result[key] = powers[key]

    return result


def parse_coordinate(coord: str) -> Tuple[float, float]:
    if coord[0] != "(" or coord[-1] != ")" or coord.count(",") != 1:
        raise ValueError(
            "Invalid coordinate, must be of the format (x,y); try 'python3 function_finder.py -h'"
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


def print_polynomial(polynomial: List[PolynomialPart]) -> None:
    if len(polynomial) == 0:
        print()
        return

    powers = add_polynomial_parts(polynomial)

    powers_list = []
    for key in powers:
        powers_list.append((key, powers[key]))
    sorted_powers = sorted(powers_list, key=lambda x: x[0], reverse=True)

    result = "f(x) ="
    for power, coefficient in sorted_powers:
        if round(coefficient, 4) == 0.0:
            continue

        if coefficient >= 0:
            result += " + "
        else:
            result += " - "

        if power > 1:
            result += f"{round(abs(coefficient), 4)}x^{power}"
        elif power == 1:
            result += f"{round(abs(coefficient), 4)}x"
        else:
            result += str(round(abs(coefficient), 4))

    if sorted_powers[0][1] > 0:
        result = result.replace("+ ", "", 1)

    print(result)


def find_value(polynomial: List[PolynomialPart], x: float) -> float:
    return sum(pp.value(x) for pp in polynomial)


def main():
    # This little bit of code generates coordinates for e^x from x=-2 to x=5
    # string = ""
    # for i in range(8):
    #    x = -2 + 7 * i / 7
    #    y = 2.71828182818**x
    #    string += f" '({x},{y})' "
    # print(string)
    # return

    if "-h" in argv or len(argv) == 1:
        print(
            "\033[33mfunction_finder.py\033[0m finds a \033[36mpolynomial function\033[0m that fits a list of coordinates"
        )
        print(
            "(can also be used to find the \033[36mnth term\033[0m of a sequence btw)"
        )
        print()
        print(
            "\033[31mUSAGE:\033[0m python3 \033[33mfunction_finder.py\033[0m '(x1,y1)' '(x2,y2)' ... '(xn,yn)'"
        )
        print(
            "Note that each coordinate must be surrounded by \033[36mquotation marks\033[0m due"
        )
        print("to the way that the terminal parses brackets")
        print()
        print(
            "\033[31mE.g.\033[0m python3 \033[33mfunction_finder.py\033[0m '(0,8)' '(5,33)' '(2,6)' "
        )
        print("-> f(x) = 2.0x^2 - 5.0x + 8.0")
        print()
        print("\033[31mFlags:\033[0m -h -> help message")
        print("       -V -> verbose printing")
        return

    input_coords = []
    verbose = False
    for i in range(len(argv)):
        if argv[i] == "-V":
            verbose = True
            input_coords = argv[:i] + argv[i + 1 :]

    if not verbose:
        input_coords = argv

    coords = []
    for coord in input_coords[1:]:
        coords.append(parse_coordinate(coord))

    polynomial: List[PolynomialPart] = [PolynomialPart([], a=coords[0][1])]
    for i in range(1, len(coords)):
        pp = PolynomialPart([coord[0] for coord in coords[:i]])
        pp.update_coefficient(polynomial, coords[i])
        polynomial.append(pp)

        if verbose:
            print(str(pp))

    print_polynomial(polynomial)


if __name__ == "__main__":
    main()
