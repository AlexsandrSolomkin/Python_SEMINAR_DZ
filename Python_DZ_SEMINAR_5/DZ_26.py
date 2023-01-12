# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# ==================================================================================

# Решение:

num_A = int(input("Введите число A для возведения в степень B: "))
num_B = int(input("Введите степень B для возведения в степень числа A: "))


def exponentiation_num(num_start: int, num_result: int, num_end: int) -> int:
    if num_end == 0:
        return num_result
    else:
        num_result *= num_start
        num_end -= 1
        num_result = exponentiation_num(num_start, num_result, num_end)

    return num_result


num_res = exponentiation_num(num_A, 1, num_B)

print(num_res)

# ==================================================================================