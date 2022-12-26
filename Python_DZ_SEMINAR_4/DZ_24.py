# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом
# кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9

# =============================================================================

# Решение:

num = int(input("Количество кустов на грядке: "))


def get_list(len_list: int, min_n: int, max_n: int) -> list:

    import random

    l = []

    # if len_list == 1:
    #     random_number = round(random.randint(min_n, max_n))
    #     l.append(random_number)
    #     return l

    for i in range(len_list):

        random_number = round(random.randint(min_n, max_n))
        l.append(random_number)

    return l


def max_sum_3_elements(start_list: list) -> int:
    left_index = -2
    central_index = -1
    rigth_index = 0
    len_list = len(start_list)
    max_sum = new_sum = 0

    if len_list > 3:
        for g in range(len_list - 1):
            left_index += 1
            central_index += 1
            rigth_index += 1
            new_sum = start_list[left_index] + \
                start_list[central_index] + \
                start_list[rigth_index]

            if max_sum < new_sum:
                max_sum = new_sum

    else:
        if len_list == 3:
            max_sum = start_list[left_index] + \
                start_list[central_index] + \
                start_list[rigth_index]
        elif len_list == 1:
            max_sum = start_list[central_index]
        elif len_list == 2:
            max_sum = start_list[central_index] + start_list[rigth_index]

    return max_sum


list_elemens = get_list(num, 1, 20)
max_sum_3 = max_sum_3_elements(list_elemens)

print(*list_elemens)
print(max_sum_3)


# =============================================================================
