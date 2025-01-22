def get_rusian_names():
    return ['Ваня', 'Коля', 'Маша']


def get_british_names():
    return ['Oliver', 'Jack', 'Harry']


print(get_rusian_names())

print(type(get_rusian_names))
print(get_rusian_names.__name__, '\r\r')

my_func = get_rusian_names
print(type(my_func))
print(my_func.__name__)
print(my_func())
print('\r\r')

### Геттеры
name_getters = [get_rusian_names, get_british_names]

for name_getter in name_getters:
    print(name_getter())

print('\r\r')


### Функции высшего порядка - функции принимающие на вход другие функции с аргументами
def adder(args):
    res = 0
    for number in args:
        res += number
    return res


def multiplier(args):
    res = 1
    for number in args:
        res *= number
    return res


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

def process_numbers(numbers, function):
    result = function(numbers)
    print(f'Получилось: {result}')

process_numbers(numbers=my_numbers, function=adder)
process_numbers(numbers=my_numbers, function=multiplier)
print('\r\r')

### ВСТРОЕННЫЕ ФУНКЦИИ ВЫСШЕГО ПОРЯДКА
# MAP применяет функцию к каждому элементу последовательности и пормирует список результатов

def mul_by_2(x):
    return x*2

result = map(mul_by_2, my_numbers)
print(result) # MAP OBJECT AT 0x00...
print(list(result))

#

