def merge_dicts(dict_a, dict_b):

    for key, value_b in dict_b.items():
        if key in dict_a:
            value_a = dict_a[key]

            if isinstance(value_a, dict) and isinstance(value_b, dict):
                merge_dicts(value_a, value_b)
            elif isinstance(value_a, list) and isinstance(value_b, list):
                dict_a[key] = value_a + value_b
            elif isinstance(value_a, set) and isinstance(value_b, set):
                dict_a[key] = value_a | value_b
            elif isinstance(value_a, tuple) and isinstance(value_b, tuple):
                dict_a[key] = value_a + value_b
            else:
                dict_a[key] = value_b
        else:
            dict_a[key] = value_b


def main():

    print("=== Слияние словарей ===")

    print("\nВведите первый словарь A:")
    dict_a = eval(input("A = "))

    print("\nВведите второй словарь B:")
    dict_b = eval(input("B = "))

    print("\nИсходный словарь A:")
    print(dict_a)

    print("\nИсходный словарь B:")
    print(dict_b)

    merge_dicts(dict_a, dict_b)

    print("\nРезультат слияния (словарь A после слияния):")
    print(dict_a)

if __name__ == "__main__":
    main()


# {'a': 1,'b': 2,'c': 3,'d': {"e":4,'f':5}}
# {'a': 1,'b': 2,'c': 3,'d': {"e":4,'f':5},'p':[123]}