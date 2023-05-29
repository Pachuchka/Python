n = int(input('Сколько монеток лежит на столе? '))
f_side = 0
s_side = 0
for i in range(n):
    coin = int(input(f'{i}-ая монетка лежит орешкой вверх? 1 - да; 0 - нет '))
    flag = False
    while flag == False:
        if coin==1 or coin==0:
            flag = True
        else:
          coin = int(input(f'введите корреткное значение,{i}-ая монетка лежит орешкой вверх? 1 - да; 0 - нет '))  
    if coin == 1:
        f_side = f_side+1
    else:
        s_side = s_side+1
if f_side>s_side:
    print(s_side)
else: print(f_side)

