def unique_elements(nested_list):

    result = []

    def extract_elements(lst):
        for item in lst:
            if isinstance(item, list):
                extract_elements(item)
            else:
                found = False
                for elem in result:
                    if elem == item:
                        found = True
                        break
                if not found:
                    result.append(item)

    extract_elements(nested_list)
    return result


def main():

    print("Уникальные элементы из вложенного списка\n")


    list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]

    print("Исходный список:")
    print(list_a)

    unique = unique_elements(list_a)

    print("\nУникальные элементы:")
    print(unique)


if __name__ == "__main__":
    main()