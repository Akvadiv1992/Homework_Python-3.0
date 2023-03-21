from random import randint

n = int(input("введите количество элементов массива: "))
array = [0] * n
for i in range(n):
    array[i] = randint(0, 10)
print(array)

x = int(input('Введите число X: '))
min = abs(x - array[0])
index = 0
for i in range(1, n):
    count = abs(x - array[i])
    if count < min:
            min = count
            index = i
print(f'ближайшее число  -- > {array[index]}')