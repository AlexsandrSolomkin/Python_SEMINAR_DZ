# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

#========================================================================

#Решение:

maxNum = int(input("Введите число, которое будет являться максимально возможным значением при возведении 2 в степень: "))

startNum = 2

def PrintNumbers(startNum, maxN):
    while startNum <= maxN:
        print(startNum, end=" ")
        startNum *= 2

print(maxNum, "->", end=" ")
PrintNumbers(2, maxNum)
#========================================================================
