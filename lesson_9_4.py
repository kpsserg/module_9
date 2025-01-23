from pprint import pprint

# LAMBDA
# Иногда нам нужны простые, одноразовые функции, для которых def слишком жирно
# Для этого есть lambda
#
# Пример 1 - lambda-функции

my_func = lambda x: x + 10

print(my_func(x=42))
print(my_func(42))
print(type(my_func))

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(lambda x: x + 10, my_numbers)
print(list(result))

# Пример 2. Лямбда форма может принимать как несколько параметров, так и ни однонго
print('\r\nПример 2. Лямбда форма может принимать как несколько параметров, так и ни однонго')
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
other_numbers = [2, 7, 1, 8, 2, 8, 1]
result = map(lambda x,y: x+y, my_numbers, other_numbers)
print(list(result))

 # Создание функций на лету.

def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        raise Exception('Я умножаю только на 2 и на 3!')
    return multiplier

my_numbers  = [3, 1, 4, 1, 5, 9, 2, 6]

by_2 = get_multiplier_v1(2)
# print(type(by_2))
by_3 = get_multiplier_v1(3)

print('\r\nРабота ф-ции multiplier, которая создана внутри ф-ции get_multiplier')
res = map(by_2, my_numbers)
print(list(res))
res = map(by_3, my_numbers)
print(list(res))

# Пример который показывает, что во внешнюю функцию не стоит передавать изменяемые объекты в качестве
# аргумента, т.к. результат работы внутренней функции становится не предсказуемым
def matrix(some_list):

    def multiply_column(x):
        res =[]
        for element in some_list:
            res.append((element * x))
        return res

    return multiply_column

my_numbers = [3, 1, 4]
other_numbers = [2, 7, 1]

matrix_on_my_numbers = matrix(my_numbers)
print('\r\n Результат работы без изменения аргумента внешней функции')
print('\r\n Внетренняя функция работает как и ожидали')
result = map(matrix_on_my_numbers, other_numbers)
print(list(result))

print('\r\n Изменим аргумент внешней ф-ции, добавив в него 1 эл-т')
my_numbers.extend([10])
result = map(matrix_on_my_numbers, other_numbers)
print('А вот и непредсказуемый результат')
print(list(result))

### Метод __call__ с помощью которого объект класса можно вызвать как функцию

class Multiplier:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        #
        return x * self.n

print('\r\nМетод __call__')

my_numbers = [3, 1, 4]
by_15 = Multiplier(15)
print(type(by_15))
result = by_15(2)
print(result)

result = map(by_15, my_numbers)
print(list(result))