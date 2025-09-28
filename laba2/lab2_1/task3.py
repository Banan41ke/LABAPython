numbers = input("Введите числа через пробел: ")
l_numbers = numbers.split()
num = []

for i in l_numbers:
    if '.' in i:
        num.append(float(i))
    else:
        num.append(int(i))
num = list(set(num))
m = max(num)
num.remove(m)
m = max(num)
print("Наибольшее второе число:",m)