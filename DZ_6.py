# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

#========================================================================================

#Решение:

num = int(input("Введите 6-ый номер билета для проверки, является ли он счастливым: "))
minNum = 100000
maxNum = 999999
if minNum <= num <= maxNum:
    num1 = num // 100000
    num2 = num % 100000 // 10000
    num3 = num % 10000 // 1000
    num4 = num % 1000 // 100
    num5 = num % 100 // 10
    num6 = num % 10
    sumNum123 = num1 + num2 + num3
    sumNum456 = num4 + num5 + num6
    if sumNum123 == sumNum456:
        print("yes")
    else:
        print("no")
else:
    print("Дынные некорректны")

#========================================================================================
