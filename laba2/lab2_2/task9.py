def type_check(expected_type1, expected_type2):

    def decorator(func):
        def wrapper(a, b):
            if type(a) != expected_type1:
                error_msg = f"Ошибка: первый аргумент должен быть {expected_type1.__name__}, а не {type(a).__name__}"
                raise TypeError(error_msg)

            if type(b) != expected_type2:
                error_msg = f"Ошибка: второй аргумент должен быть {expected_type2.__name__}, а не {type(b).__name__}"
                raise TypeError(error_msg)

            print("Типы аргументов правильные!")
            return func(a, b)

        return wrapper

    return decorator

def main():
    print("Проверка типов аргументов\n")

    @type_check(int, int)
    def add_numbers(a, b):
        return a + b

    @type_check(str, int)
    def repeat_text(text, count):
        result = ""
        for i in range(count):
            result += text
        return result

    print("1. Правильные аргументы:")
    try:
        result = add_numbers(10, 20)
        print(f"add_numbers(10, 20) = {result}")
    except TypeError as e:
        print(e)

    print("\n2. Неправильные аргументы:")
    try:
        result = add_numbers(10, "20")
        print(f"add_numbers(10, '20') = {result}")
    except TypeError as e:
        print(e)

    print("\n3. Правильные аргументы для текста:")
    try:
        result = repeat_text("hello", 3)
        print(f"repeat_text('hello', 3) = '{result}'")
    except TypeError as e:
        print(e)

    print("\n4. Неправильные аргументы для текста:")
    try:
        result = repeat_text(123, 3)
        print(f"repeat_text(123, 3) = '{result}'")
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()