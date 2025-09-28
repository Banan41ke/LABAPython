numbers1 = input("Введите числа через пробел: ")
numbers2 = input("Введите числа через пробел: ")

l_numbers1 = numbers1.split()
l_numbers2 = numbers2.split()

num1 = []
num2 = []

for i in l_numbers1:
    if '.' in i:
        num1.append(float(i))
    else:
        num1.append(int(i))

for i in l_numbers2:
    if '.' in i:
        num2.append(float(i))
    else:
        num2.append(int(i))

num1 = list(set(num1))
num2 = list(set(num2))

into = []
non_into1 = []
non_into2 = []

for i in num1:
    if i in num2:
        into.append(i)
    else:
        non_into1.append(i)

print("Пересечение двух списков",*into)

for i in num2:
    if i not in num1:
        non_into2.append(i)

print("Числа, которых нет в пересечении из 1 списка",*non_into1)
print("Числа, которых нет в пересечении из 2 списка",*non_into2)
print("Числа, которых нет в пересечении из обоих списков",*(non_into2+non_into1))