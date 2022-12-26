# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

# =============================================================================

# Решение:

num_n = int(input("n - кол-во элементов первого набора: "))
num_m = int(input("m - кол-во элементов второго набора: "))


def get_list(n: int, min_n: int, max_n: int) -> list:

    import random

    l = []

    for i in range(n):

        random_number = round(random.randint(min_n, max_n))
        l.append(random_number)

    return l


list_random_n = get_list(num_n, 0, 20)
list_random_m = get_list(num_m, 0, 20)

print(*list_random_n)
print(*list_random_m)

# =============================================================================
