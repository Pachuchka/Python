n = int(input('Введите число элементов массива '))
i=0
user_list=[]
for i in range(n):
    user_list.append(int(input('Введите очередной элемент массива ')))
x = float(input('Введите число, для которого будет искаться приближение '))
min = user_list[0]
for j in range(n):
    difference = x - user_list[j]
    if difference < x-min:
        min = user_list[j]
print(min)