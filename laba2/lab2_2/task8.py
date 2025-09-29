import time


def timing(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = (end_time - start_time) * 1000

        print(f"Время выполнения {func.__name__}: {execution_time:.2f} мс")

        return result

    return wrapper


def main():

    print("Декоратор измерения времени\n")

    @timing
    def slow_function():

        time.sleep(0.5)  # Задержка 0.5 секунды
        return "Готово!"

    @timing
    def fast_function():

        return "Быстро!"

    @timing
    def calculate_sum(n):

        total = 0
        for i in range(n):
            total += i
        return total

    print("Тест 1 - Медленная функция:")
    result1 = slow_function()
    print(f"Результат: {result1}")

    print("\nТест 2 - Быстрая функция:")
    result2 = fast_function()
    print(f"Результат: {result2}")

    print("\nТест 3 - Вычисление суммы:")
    result3 = calculate_sum(1000000)
    print(f"Результат: {result3}")


if __name__ == "__main__":
    main()