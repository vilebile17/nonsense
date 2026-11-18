import numpy as np
import math

num_iterations = int(input("num_iterations -> "))
binomial_coefs = [
    np.array([j - 0.5 for j in range(1, 1 - i, -1)], dtype=np.float128).prod()
    / math.factorial(i)
    for i in range(num_iterations)
]
integration_divisions = np.array(
    [(2 * i + 1) if i % 2 == 0 else (-2 * i - 1) for i in range(num_iterations)]
)
x_coefficients = binomial_coefs / integration_divisions
sum_of_terms = sum(
    [x_coefficients[i] * 0.5 ** (2 * i + 1) for i in range(x_coefficients.size)]
)
print(sum_of_terms * 12 - (3 * math.sqrt(3) / 2))
