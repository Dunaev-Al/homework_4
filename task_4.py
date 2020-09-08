arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_arr = [el for el in arr if arr.count(el) < 2]
print(new_arr)
