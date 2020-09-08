arr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in arr if arr[arr.index(el) - 1] < el and arr.index(el) - 1 > 0]
print(new_list)
