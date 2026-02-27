from sympy import gcd

# Compute GCD
def compute_gcd(a, b):
    return gcd(a, b)

# Extended Euclidean Algorithm
def extended_euclidean(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)

# Euclidean Algorithm Steps
def euclidean_steps(a, b):
    steps = []
    while b != 0:
        q = a // b
        r = a % b
        steps.append(f"{a} = {b}({q}) + {r}")
        a, b = b, r
    return steps