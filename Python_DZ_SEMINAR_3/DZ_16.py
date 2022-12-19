# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 3

# 1 2 3 4 5
# Вывод: 1

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


def ElemntsXList(x, listElements):

    count = 0

    for g in range(len(listElements)):

        if listElements[g] == x:

            count += 1

    return count


newList = result = 0

if numMax >= хNum >= 1:

    newList = GetList(num, numMax)
    result = ElemntsXList(хNum, newList)

    print(newList, result, sep="\n")

else:

    print("Число некорректно")

# ========================================================================
