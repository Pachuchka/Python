n = int(input('Сколько кустов посажено в круг? '))
i=0
user_list=[]
for i in range(n):
    user_list.append(int(input(f'Введите урожайность {i+1}-ого куста: ')))
#start = int(input('С какого куста начинаем обход? '))
#max = user_list[len(user_list)-1]+user_list[len(user_list)-2]+user_list[0]
max = 0
for j in range(n):
    if  user_list[j%n] + user_list[(j+1)%n] + user_list[(j+2)%n]>max:
        max = user_list[j%n] + user_list[(j+1)%n] + user_list[(j+2)%n]
print(max)
