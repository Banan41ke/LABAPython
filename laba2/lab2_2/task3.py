import datetime


# Декоратор для записи вызовов в файл
def log_calls(filename):

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Получаем текущее время
            now = datetime.datetime.now()
            time_str = now.strftime("%Y-%m-%d %H:%M:%S")

            # Формируем строку с аргументами
            args_str = ""
            for arg in args:
                args_str += str(arg) + ", "

            # Убираем последнюю запятую
            if args_str:
                args_str = args_str[:-2]

            # Создаем строку для записи в файл
            log_line = f"{time_str} - {func.__name__}({args_str})\n"

            # Открываем файл и записываем
            file = open(filename, "a", encoding="utf-8")
            file.write(log_line)
            file.close()

            # Вызываем оригинальную функцию
            return func(*args, **kwargs)

        return wrapper

    return decorator

def main():
    print("=== Декоратор для записи вызовов в файл ===\n")

    @log_calls("log.txt")
    def add(a, b):
        result = a + b
        print(f"  Результат: {a} + {b} = {result}")
        return result

    @log_calls("log.txt")
    def greet(name):
        message = f"  Привет, {name}!"
        print(message)
        return message

    @log_calls("log.txt")
    def multiply(x, y, z):
        result = x * y * z
        print(f"  Результат: {x} * {y} * {z} = {result}")
        return result

    # Очищаем файл перед началом
    open("log.txt", "w").close()
    print("Файл log.txt очищен\n")

    # Вызываем функции - они автоматически записываются в файл
    print("1. Вызов add(5, 3):")
    add(5, 3)

    print("\n2. Вызов greet('Анна'):")
    greet("Анна")

    print("\n3. Вызов multiply(2, 3, 4):")
    multiply(2, 3, 4)

    print("\n4. Вызов add(10, 20):")
    add(10, 20)

    # Показываем содержимое файла
    print("\n" + "=" * 50)
    print("Содержимое файла log.txt:")
    print("=" * 50)

    file = open("log.txt", "r", encoding="utf-8")
    content = file.read()
    file.close()
    print(content)

if __name__ == "__main__":
    main()