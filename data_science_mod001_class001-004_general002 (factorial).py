#factorial (n) = n * (n-1) * (n-2) * ...
# to calculate the number of COMBINATIONS

def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result

print factorial(4)
#>>> 24

print factorial(5)
#>>> 120

print factorial(6)
#>>> 720
