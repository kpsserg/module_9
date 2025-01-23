from random import choice

# Задание 1
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


# Задание 2
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for item in data_set:
                file.write(str(item) + ' ')
            file.write('\n')

    return write_everything


write = get_advanced_writer('example.txt')
# write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], [1,2,3,(1,2,3)], (3,2,1),{1.2}, {'a':'b'})
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Задание 3
class MysticBall:

    def __init__(self, *data):
        self.sequence = []
        for item in data:
            self.sequence.append(item)

    def __call__(self):
        return choice(self.sequence)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())