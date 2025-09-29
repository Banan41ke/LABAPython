def merge_sorted_lists(list1, list2):

    result = []
    i = 0  # индекс для list1
    j = 0  # индекс для list2

    while i < len(list1) or j < len(list2):

        if i >= len(list1):
            result.append(list2[j])
            j += 1

        elif j >= len(list2):
            result.append(list1[i])
            i += 1

        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    return result


def main():

    print("Объединение отсортированных списков\n")

    list1_input = input("Введите первый отсортированный список (через запятую): ")
    list1 = [int(x.strip()) for x in list1_input.split(",")]

    list2_input = input("Введите второй отсортированный список (через запятую): ")
    list2 = [int(x.strip()) for x in list2_input.split(",")]

    print(f"\nПервый список: {list1}")
    print(f"Второй список: {list2}")


    merged = merge_sorted_lists(list1, list2)

    print(f"\nОбъединенный отсортированный список: {merged}")


if __name__ == "__main__":
    main()