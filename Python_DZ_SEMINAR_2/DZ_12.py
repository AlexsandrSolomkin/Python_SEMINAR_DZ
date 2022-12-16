# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# =====================================================================

# Решение:

import random

num1 = round(random.randint(1, 1000))
num2 = round(random.randint(1, 1000))

sumNum = num1 + num2
multiplyNum = num1 * num2


def AnswerSumMultiply(sum1, multiply):

    num1Kate = 1

    for num1Kate in range(1, multiply):

        if multiply % num1Kate == 0:

            num2Kate = multiply / num1Kate

            if sum1 == num2Kate + num1Kate:
                return int(num2Kate), num1Kate


print("Петя загадал числа: {}, {}".format(num1, num2))
print("Сумма, произведение чисел: {}, {}".format(sumNum, multiplyNum))
print("Катя должна ответить: {}, {}".format(*AnswerSumMultiply(sumNum, multiplyNum)))

# =====================================================================
