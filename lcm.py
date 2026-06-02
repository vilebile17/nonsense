import sys


def lcm(num1: int, num2: int) -> int:
    largest = max([num1, num2])
    smallest = min([num1, num2])
    i = 1
    while True:
        if (largest * i) % smallest == 0:
            return largest * i
        i += 1


def main():
    print(lcm(int(sys.argv[1]), int(sys.argv[2])))


if __name__ == "main":
    main()
