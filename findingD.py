# pseudocode refernce: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

def mod_inv(a, b):
    n, new_n = 0, 1
    m, new_m = b, a
    iterations = [("n", "new_n", "m", "new_m")]

    while new_m:
        quotient = m // new_m
        n, new_n = new_n, n - quotient * new_n
        m, new_m = new_m, m - quotient * new_m
        iterations.append((n, new_n, m, new_m))

    if m > 1:
        return None, iterations  # no solution

    if n < 0:
        n = n + b

    return n, iterations


N = 682929935168456011800260390123
e = 288546253195154448765672969661


p = 752304375247267
q = 907784080006169
phi = (p - 1) * (q - 1)

d, iterations = mod_inv(e, phi)

print("values:")
for row in iterations:
    print("{: <8} {: <32} {: <32} {: <32}".format(*row))

print("\nd:", d)
