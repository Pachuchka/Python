import math
p = int(input('какова сумма чисел? '))
s = int(input('каково произведение? '))
flag = False
for i in range(1,1000):
    for j in range(1,1000):
        if i*j == p and i+j ==s:
            flag = True
            print(f'подходящие натуральные: {i}, {j}')
if flag == False:
    print('подходящих натуральных, в указанном диапазоне не существует')
