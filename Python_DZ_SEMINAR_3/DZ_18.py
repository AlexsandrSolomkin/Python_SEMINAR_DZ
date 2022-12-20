# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший.

# Ввод: 5
# Ввод: 6
# 1 2 0 4 7
# Вывод: 7

# ========================================================================

# Решение:

num = int(input("Ведите N размер массива, который вы хотите заполнить: "))
хNum = int(input("Нужное число, которое может быть от 1 до N/2: "))

numMax = int(num / 2)


def GetList(n, nMax):

    import random

    l = []

    for i in range(n):

        random_number = round(random.randint(1, nMax))
        l.append(random_number)

    return l


def ClosestElementToX(x, listElements):

    clEl = listElements[0]
    difference = x - clEl

    for g in range(1, len(listElements)):

        elDifference = x - listElements[g]

        if difference > elDifference:

            clEl = listElements[g]

    return clEl

# ========================================================================