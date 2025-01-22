# Списковые сборки

# Аналог MAP
my_num = [-1, -3, 11, 4, 6]
res = [x * 3 for x in my_num]
print(res)

# Аналог filter
res = [x * 3 for x in my_num if x % 2]
print(res)

res = [x * 2 if x > 2 else x * 10 for x in my_num]
print(res)

# Условия перед циклом
my_num = ["A", 1, 4, "B", 5, "C", 2, 6]
res = [x if type(x) == str else x * 5 for x in my_num]
print(res)

# Вложенные циклы
my_num_1 = [1, 2, 3, 4]
my_num_2 = [1, 6, 7, 8]

res = [x * y for x in my_num_1 for y in my_num_2]
print(res)

res = [x * y for x in my_num_1 for y in my_num_2 if x % 2]
print(res)

res = [x * y for x in my_num_1 for y in my_num_2 if x % 2 and y // 2]
print(res)

# Логика работы целочисленного деления
my_num_3 = [1, -1, 2, -2,  3, -3,  4, -4]
print(f'Посмотрим на результат целочисленного деления числа на 2. (число, результат)')
print(f'Результат уменьшается до ближайшего целого')
print(f'Это поведение проявляется на отрицательных числах')
res = [(x, x//2) for x in my_num_3]
print(res)


