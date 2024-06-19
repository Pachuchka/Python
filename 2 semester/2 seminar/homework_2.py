# Задача 1
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

#num = int(input("Введите целое число, для которого нужно получить представление: "))
#hex_num_str = "{:x}".format(num)
#print("Шестнадцатеричное строковое представление :", hex_num_str)

#print("Для проверки результата, приводим результат функции hex", hex(num))

#Второй вариант решения, как на семинаре

# DIV_HEX = 16
# ZERO = 0
# NATIVE = 10

# num = int(input("Введите целое число, для которого нужно получить представление: "))
# num_memo = num
# hex_num_str = ""
# if num == ZERO:
#    print(f'Вы ввели число {ZERO}')
# else:
#    while num > ZERO:
#        num, remainder = divmod(num, DIV_HEX) 
#        if remainder < NATIVE:
#            hex_num_str = srt(remainder) + hex_num_str
#        else:
#            hex_num_str = chr(remainder - NATIVE + ord('a')) + hex_num_str
# print("Шестнадцатеричное строковое представление :", hex_num_str)

# print("Для проверки результата, приводим результат функции hex", hex(num_memo))


# Задача 2
# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
from fractions import Fraction
ZERO = 0
STEP = 1

user_str = str(input(f'Введите строковое представление первой дроби, вида a/b: '))
pos_delimer = user_str.index('/')
numerator_1 = int(user_str[:pos_delimer])
delimer_1 = int(user_str[pos_delimer + STEP:])

user_str = str(input(f'Введите строковое представление второй дроби, вида a/b: '))
pos_delimer = user_str.index('/')
numerator_2 = int(user_str[:pos_delimer])
delimer_2 = int(user_str[pos_delimer + STEP:])

fraction_sum = (numerator_1 * delimer_2 + numerator_2 * delimer_1) / (delimer_2 * delimer_1)
fraction_multiply = (numerator_1 * numerator_2)/(delimer_1 * delimer_2)

print(f'Сумма дробей равна: {fraction_sum}')
print(f'Произведение дробей равно: {fraction_multiply}')

print(f'проверка суммы: {Fraction(numerator_1,delimer_1) + Fraction(numerator_2,delimer_2)}')
print(f'проверка произведения: {Fraction(numerator_1,delimer_1) * Fraction(numerator_2,delimer_2)}')