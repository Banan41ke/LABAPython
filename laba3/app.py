#класс дорожные знаки и наследники  типо запрещающие и тд пользователь может создавать объекты каждого класса то есть вводит что это запрещающий знак его номер название и на выходе выводиться к примеру запрещающие такие и тд
from abc import ABC, abstractmethod

class Road_Sign(ABC):
    a = {}
    def __init__(self,name,number,group_sign):
        self.name = name
        self.number = number
        self.group_sign = group_sign

    def add_sign(self):
        if self.group_sign not in Road_Sign.a:
            Road_Sign.a[self.group_sign] = []
        Road_Sign.a[self.group_sign].append({
            "название": self.name,
            "номер": self.number
        })
    def print_info(self):
        print(self.a.keys())
        return f"Группа знака - {self.group_sign}, номер знака - {self.number}, название - {self.name}"

    @abstractmethod
    def display_info(self):
        pass
class ProhibitingSign(Road_Sign):
    def __init__(self, name, number):
        super().__init__(name,number,"Запрещающие")

    def display_info(self):
        info = f"Запрещающий знак\n"
        info += f"Номер: {self.number}\n"
        info += f"Название: {self.name}\n"
        return info
class InformationalSign(Road_Sign):
    def __init__(self, name, number):
        super().__init__(name,number,"Информационные")

    def display_info(self):
        info = f"Запрещающий знак\n"
        info += f"Номер: {self.number}\n"
        info += f"Название: {self.name}\n"
        return info
class PrescriptiveSign(Road_Sign):
    def __init__(self, name, number):
        super().__init__(name,number,"Предписывающие")

    def display_info(self):
        info = f"Запрещающий знак\n"
        info += f"Номер: {self.number}\n"
        info += f"Название: {self.name}\n"
        return info
class PrioritySigns(Road_Sign):
    def __init__(self, name, number):
        super().__init__(name,number,"Приоритета")

    def display_info(self):
        info = f"Запрещающий знак\n"
        info += f"Номер: {self.number}\n"
        info += f"Название: {self.name}\n"
        return info
class WarningSign(Road_Sign):
    def __init__(self, name, number):
        super().__init__(name,number,"Предупреждающие")

    def display_info(self):
        info = f"Предупреждающий знак\n"
        info += f"Номер: {self.number}\n"
        info += f"Название: {self.name}\n"
        return info

def display_all_signs():
    if not Road_Sign.a:
        print("Список пуст")
    else:
        for group,signs in Road_Sign.a.items():
            print(group.upper())
            if signs:
                for signy in signs:
                    print(signy)
            else:
                print("Нет знаков в группе")

def del_sign(b,c):
    if b in Road_Sign.a:
        for i, sign in enumerate(Road_Sign.a[b]):
            if sign["название"] == c:
                del Road_Sign.a[b][i]
                print(f"Знак '{c}' удален из группы '{b}'")
                if not Road_Sign.a[b]:
                    del Road_Sign.a[b]
                return
        print(f"Знак '{c}' не найден в группе '{b}'")
    else:
        print(f"Группа '{b}' не найдена")

if __name__ == "__main__":

    while True:
        print("Выбери что ты хочешь сделать\n1 - Добавить знак\n2 - Просмотреть список добавленных знаков\n3 - Удалить знак из группы\n4 - Выход")
        choice = input("Выберите действие: ")
        try:
            if choice == "1":
                print("Введите название знака")
                s = input()
                print("Введите номер знака")
                n = input()
                print("Введите группу знака")
                g = input()
                if g == "Запрещающие":
                    sign = ProhibitingSign(s, n)
                elif g == "Информационные":
                    sign = InformationalSign(s, n)
                elif g == "Приоритета":
                    sign = PrioritySigns(s, n)
                elif g == "Предписывающие":
                    sign = PrescriptiveSign(s, n)
                elif g == "Предупреждающие":
                    sign = WarningSign(s, n)
                sign.add_sign()
                print("Знак добавлен")
                print(sign.display_info())
            elif choice == "2":
                display_all_signs()
            elif choice == "3":
                print("Введите группу, в которой хотите удалить знак")
                g = input()
                print("Введите название знака")
                n = input()
                del_sign(g,n)
            elif choice == "4":
                exit()
            else:
                print("Неверный выбор")
        finally:
            print("-------------------------------------------------------")

