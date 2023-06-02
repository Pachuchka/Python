n = int(input('Введите число элементов первого множества '))
m = int(input('Введите число элементов второго множества '))
i=0
user_set_1 = set()
for i in range(n):
   user_set_1.add(input('Введите очередной элемент первого множества '))
i = 0
user_set_2 = set()
for i in range(m):
   user_set_2.add(input('Введите очередной элемент второго множества '))
new_set = set.intersection(user_set_1, user_set_2)
result = list(new_set)
result.sort()
print(result)