from random import randint

a = int(input("введите количество элементов массива: "))
array = [0] * a
for i in range(a):
    array[i] = randint(0, 10)
print(array)

t = int(input('Введите число X, которое необходимо найти в массиве: '))
count = 0
for i in range(len(array)):
    if array[i] == t:
        count += 1
print(f'Число {t} встречается в массиве {count} раз')