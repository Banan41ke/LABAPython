def flatten_list(lst):

    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            flatten_list(lst[i])
            lst[i:i+1] = lst[i]
        else:
            i += 1
    return lst

list_a = [1, 2,[12, 13], 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print("Список после применения flatten_list:")
print(list_a)
