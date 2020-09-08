from itertools import count
from itertools import cycle


counter = 0
for el in count(int(input('Введите число '))):
    counter += 1
    print(el)
    if counter == 10:
        break

print('Вторая часть задания: ')

counter = 0
arr = [1, 2, 3, 'abc', 3.123]
for el in cycle(arr):
    counter += 1
    print(el)
    if counter == 10:
        break

