n = int(input('Введите число рядов долек шоколадки по одной оси: '))
m = int(input('Введите число рядов долек шоколадки по другой оси: '))
k = int(input('сколько долек вы хотите отломить?: '))
if k>n*m:
    print('во всей шоколадке нет столько долек')
else:
    if k%n==0 or k%m==0:
        print(f"Да, можно")
    else:
        print('Нет, число доле должно быть кратным одной из сторон шоколадки')