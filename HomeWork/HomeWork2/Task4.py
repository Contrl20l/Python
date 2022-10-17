# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

input_num = int(input('Введите число: '))
list = []

for i in range(input_num):
    list.append(random.randint(input_num*-1, input_num))

print(list)

f = open('file.txt', 'w')
f.write("list")
f.close()

s = input('Укажите позицию для вычисления: ')
result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result = result * list[int(line)]
f.close()
print(result)


# import random

# f = open('file.txt')
# input_num = int(input('Введите число: '))
# list = []

# for i in range(input_num):
#     list.append(random.randint(input_num*-1, input_num))

# print(list)

# for line in f:
#     print (list[int(line)], ' * ' , end='' )
#     result = result * list[int(line)]

# print(' ', result)