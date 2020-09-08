from functools import reduce


def multiply(x, y):
    return x * y


arr = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(multiply, arr))
