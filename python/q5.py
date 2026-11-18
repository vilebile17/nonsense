counter = 0
for x in range(1, 1024):
    for y in range(1, 1024):
        if x**3 + 6 * x**2 * y + 12 * x * y**2 + 8 * y**3 == 2**30:
            print(f"{x}, {y}")
            counter += 1
print(counter)
