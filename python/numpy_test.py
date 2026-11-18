import numpy as np

rng = np.random.default_rng(1)
arr = rng.integers(low=0, high=20, size=(5, 10))
print(arr)
print(np.exp(arr))
