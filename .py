def binary_search(lst, x):
    left = -1
    right = len(lst)
    while right - left > 1:
        mid = (left + right) // 2
        if lst[mid] < x:
            left = mid
        else:
            right = mid
    if right == len(lst):
        return None
    else:
        return left, right

def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]

try:
    lst = list(map(int, input("Введите последовательность чисел: ").split()))
except ValueError:
    print("Ошибка ввода данных. Проверьте правильность введенной последовательности чисел.")
else:
    sort_list(lst)
    print("Отсортированный список:", lst)

    try:
        x = int(input("Введите любое число: "))
    except ValueError:
        print("Ошибка ввода данных. Проверьте правильность введенного числа.")
    else:
        result = binary_search(lst, x)
        if result is None:
            print("В списке нет элемента, меньшего числа", x, "или следующего за ним элемента.")
        else:
            print("Позиция элемента, меньшего", x, ":", result[0])
            print("Позиция элемента, большего или равного", x, ":", result[1])
