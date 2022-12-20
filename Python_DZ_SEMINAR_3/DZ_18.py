# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший.

# Ввод: 5
# Ввод: 6
# 1 2 0 4 7
# Вывод: 7

# ========================================================================

# Решение:

num = int(input("Ведите N размер массива, который вы хотите заполнить: "))
хNum = int(input("Нужное число, которое может быть от 1 до N: "))


def GetList(n):

    import random

    l = []

    for i in range(n):

        random_number = round(random.randint(1, n))
        l.append(random_number)

    return l


def ClosestElementToX(x, listElements):

    clEl = listElements[0]
    difference = abs(x - clEl)

    for g in range(1, len(listElements)):

        elDifference = abs(x - listElements[g])

        if difference > elDifference:

            clEl = listElements[g]
            difference = elDifference

    return clEl


newList = GetList(num)
result = ClosestElementToX(хNum, newList)

print(*newList)
print(result)

# ========================================================================
