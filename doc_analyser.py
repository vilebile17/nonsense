from collections import Counter
import sys


def word_length(lines):
    c = Counter()
    for line in lines:
        for word in line.split(" "):
            c[len(word)] += 1
    return c


def print_results(c: Counter):
    largest = max([key for key in c])
    total = sum([c[key] for key in c])
    for i in range(1, largest + 1):
        string = f"{i}: "
        for _ in range(round(c[i] / total * 200)):
            string += "#"
        print(string + f" {c[i]}")


if len(sys.argv) != 2:
    print("USAGE: python3 doc_analyser.py <file_to_analyse>")
    sys.exit(1)
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
c = word_length(lines)
print_results(c)
