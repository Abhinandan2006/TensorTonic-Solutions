import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    a = np.asarray(A)
    n, m = a.shape
    t = np.zeros((m, n), dtype = a.dtype)
    for i in range(n):
        for j in range(m):
            t[j, i] = a[i, j]
    return t
