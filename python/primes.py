def is_prime(num: int):
    if num == 1:
        return False
    elif num == 2:
        return True

    divisor = 2
    while divisor**2 <= num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True


i = 0
while True:
    print(f"2^{i} - 1: {is_prime(2**i - 1)}")
    i += 1
