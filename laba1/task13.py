import random

number = random.randint(1, 100)
number_user = 0
print(number)

while number_user != number:
    number_user = int(input("Введите ваше целое число:"))
    if number_user<number:
        print("Больше")
    elif number_user>number:
        print("Меньше")
    else:
        print("Бинго!!!")