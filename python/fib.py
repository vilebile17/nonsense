import sys

sys.set_int_max_str_digits(13000)
a = 0
b = 1
count = 0
iterations = 50000

for i in range(iterations - 2):
    c = a + b
    a = b
    b = c

    for char in str(b):
        if char == "3":
            count += 1

print(count)
