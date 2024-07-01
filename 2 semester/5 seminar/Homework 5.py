#4. Создайте функцию генератор чисел Фибоначчи

#def fibonachi(x,y,z):
    #f=[x,y]
    #[f.append(f[-2]+f[-1]) for i in range(z)]
    #print(f)
    #f

#fibonachi(5,10,18)

#3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

# import decimal

# names = ['Иван','Оксана','Константин','Арсений']
# price = [25000, 17000,22000,30000]
# percents = ['12.5%', '9.0%', '11.0%', '15.0%']

# PERCENT = decimal.Decimal(1)/decimal.Decimal(100)

# bonus = dict(zip(names, [x * (1 + float(decimal.Decimal(y[:-1])*PERCENT)) for x,y in zip(price,percents)]))
# print(bonus)



#2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
path = "C:\Study\Python\2 semester\5 seminar\Homework 5.py"
print(list([path.rsplit('\\', 1)[0], path.rsplit('\\', 1)[-1].rsplit('.', 1)[0] if '.' in path.rsplit('\\', 1)[-1] else path.rsplit('\\', 1)[-1], *(['.' + path.rsplit('\\', 1)[-1].rsplit('.', 1)[1]] if '.' in path.rsplit('\\', 1)[-1] else [''])]))