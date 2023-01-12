# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# ==================================================================================

# Решение:

num_A = int(input("Введите целое неотрицательное число A для суммы A и B: "))
num_B = int(input("Введите целое неотрицательное число B для суммы A и B: "))


def sum_a_b(num_1: int, num_2: int, num_result: int) -> int:
    # if num_result > num_1:
    #     return "Стартовое значение суммы не может быть больше первого элемента!"

    if num_1 == 0:
        if num_2 == 0:
            return num_result
        else:
            num_result += 1
            num_2 -= 1
            num_result = sum_a_b(num_1, num_2, num_result)
    else:
        num_result += 1
        num_1 -= 1
        num_result = sum_a_b(num_1, num_2, num_result)

    return num_result


num_sum = sum_a_b(num_A, num_B, 0)

print(num_sum)

# ==================================================================================