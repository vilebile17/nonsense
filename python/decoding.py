string = "NCHHLKBPNLHO"

print(ord("A"))
print(ord("F"))

for char in string:
    if ord(char) <= 70:
        print(char, end="")
    else:
        print(ord(char) - 70, end="")
