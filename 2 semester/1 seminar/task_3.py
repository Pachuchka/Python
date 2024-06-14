# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки.

from random import randint

START = 1 # стартовое число попыток
ATTEMPTS_LIMIT = 110 # число попыток
UPPER_LIMIT = 1000
LOWER_LIMIT = 0

count = START
random_num = randint(LOWER_LIMIT, UPPER_LIMIT)

while count < ATTEMPTS_LIMIT:
    attempt = int(input("введите натуральное число не более 1000, попробуй угадать загаданное число: "))
    if attempt == random_num:
        print (f'попытка номер: {count} - верно, вы угадали')
        count+=1100
    elif attempt < random_num:
        print(f'попытка номер: {count} - загаданное число больше')
        count +=1
    elif attempt > random_num:
        print(f'попытка номер: {count} - загаданное число меньше')
        count +=1