# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.

import random

UPPER_LIMIT = 100000
LOWER_LIMIT = 1
ZERO = 0
ITERATION = 12 #Число итераций теста Ферма
STEP = 1 #Шаг для уменьшения или увеличения числа
REMAINDER = 1

result = "Число простое"
num = int(input(f'Введите целое положительное число меньше {UPPER_LIMIT}: '))
while num > UPPER_LIMIT or num < LOWER_LIMIT:
    num = int(input(f'Не корректный ввод, введите число от {LOWER_LIMIT} до {UPPER_LIMIT}'))
else:
    for _ in range(min(num,ITERATION)):
        a = random.randint(STEP, num - STEP)
        if pow(a, num-STEP, num) != REMAINDER:
            result = "число составное"
print (result)