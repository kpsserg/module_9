first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = []
for i, j in zip(first, second):
    if len(i) != len(j):
        first_result.append(len(i) - len(j))

print((first_result))

second_result = []
for i in range(len(first)):
    if len(first[i]) != len(second[i]):
        second_result.append(False)
    else:
        second_result.append(True)
print((second_result))