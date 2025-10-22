import numpy as np

def integrand(x):
    return 1 / (1 + x**2)

# Definiujemy przedział i liczbę iteracji
a = -1
b = 1
n = 1000

# Calculating the width of each subinterval
h = (b - a) / n

# Applying Gauss-Simpson rule for integration and summing the values at endpoints
integral = h * (integrand(a) + 4*integrand((a+b)/2) + integrand(b))

# Calculating the value of e using the formula for e: e = integral * 2*pi^2
e_estimate = integral * 2 * (np.pi**2)

print("Obliczenie liczby Eulera:", e_estimate)

def approximate_e(n=1_000_000):
    return (1 + 1/n) ** n

e_2 = approximate_e(n=1_000_000)
print("Obliczenie liczby Eulera2 :", e_2)