n = int(input('Введите число элементов массива '))
i=0
user_list=[]
for i in range(n):
    user_list.append(input('Введите очередной элемент массива '))
x = int(input('Введите номер элемента для проверки '))
j,count=0,0
for j in range(len(user_list)):
    if user_list[j]==user_list[x]: count = count+1
print(count)