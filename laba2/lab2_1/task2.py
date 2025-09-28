numbers = input("Введите числа через пробел ")
l_numbers = numbers.split()
num = []
non_unique = []
unique = []
even_numbers = []
non_even_numbers = []
float_numbers = []
c=0

for i in l_numbers:
    if '.' in i:
        num.append(float(i))
        float_numbers.append(i)
        if float(i)%2==0:
            even_numbers.append(i)
        else:
            non_even_numbers.append(i)
    else:
        num.append(int(i))
        if int(i)%2==0:
            even_numbers.append(i)
        else:
            non_even_numbers.append(i)

max_number = max(num)
min_number = min(num)

for i in num:
    if num.count(i)>1:
        non_unique.append(i)
    else:
        unique.append(i)
    if i%5==0:
        c+=i

l_non_unique = list(set(non_unique))

# for i in list(set(l_numbers)):
#     if '.' in i:
#         float_numbers.append(i)
#         if float(i)%2==0:
#             even_numbers.append(i)
#         else:
#             non_even_numbers.append(i)
#     else:
#         if int(i)%2==0:
#             even_numbers.append(i)
#         else:
#             non_even_numbers.append(i)
if not unique:
    print("Нет уникальных чисел.")
else:
    print("Уникальные числа:",*unique)
if not l_non_unique:
    print("Нет повторяющихся чисел.")
else:
    print("Повторяющиеся числа:",*l_non_unique)
if not even_numbers:
    print("Нет четных чисел.")
else:
    print("Четные числа:",*even_numbers)
if not non_even_numbers:
    print("Нетнечетных чисел.")
else:
    print("Нечетные числа:",*non_even_numbers)
if not float_numbers:
    print("Нет чисел с плавающей точкой.")
else:
    print("Числа с плавающей точкой:",*float_numbers)
print("Сумма всех чисел кратных 5:",c)
print("Максимально число:",max_number)
print("Минимальное число:",min_number)
