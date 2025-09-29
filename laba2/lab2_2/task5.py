def cache(func):

    cache_dict = {}

    def wrapper(*args, **kwargs):

        key = str(args) + str(sorted(kwargs.items()))

        if key in cache_dict:
            print(f"Взято из кэша: {func.__name__}{args}")
            return cache_dict[key]
        else:
            print(f"Вычисляем: {func.__name__}{args}")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper


def main():

    print("Декоратор кэширования\n")

    @cache
    def multiply(a, b):
        return a * b

    @cache
    def factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


    print("Тест умножения:")
    print(f"Результат: {multiply(3, 4)}")
    print(f"Результат: {multiply(3, 4)}")  # Должно быть из кэша
    print(f"Результат: {multiply(5, 6)}")
    print(f"Результат: {multiply(3, 4)}")  # Должно быть из кэша

    print("\nТест факториала:")
    print(f"Результат: {factorial(5)}")
    print(f"Результат: {factorial(5)}")  # Должно быть из кэша
    print(f"Результат: {factorial(4)}")
    print(f"Результат: {factorial(5)}")  # Должно быть из кэша


if __name__ == "__main__":
    main()