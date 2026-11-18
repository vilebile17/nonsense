i = 1
acc = 1
while acc > 0.5:
    acc *= (15000 - i + 1) / 15000
    i += 1
print(i)
