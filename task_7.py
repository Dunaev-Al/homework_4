from itertools import count
from math import factorial


def fact(n):
    generator = (el for el in range(1, n))
    for el in generator:
        yield factorial(el)


for element in fact(7):
    print(element)
