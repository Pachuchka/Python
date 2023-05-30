one = [1, 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
two = [2, 'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У' ]
three = [3, 'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
four = [4, 'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
five = [5, 'Ж', 'З', 'Х', 'Ц', 'Ч', 'K']
eight = [8, 'J', 'X', 'Ш', 'Э', 'Ю']
ten = [10, 'Q', 'Z', 'Ф', 'Щ', 'Ъ']
dict = {}
print(dict)
print(one)
def add_to_dict(m,d):
    i =1
    while i<len(m):
        d[m[i].lower()] = m[0]
        i=i+1
    
add_to_dict(one,dict)
add_to_dict(two,dict)
add_to_dict(three,dict)
add_to_dict(four,dict)
add_to_dict(five,dict)
add_to_dict(eight,dict)
add_to_dict(ten,dict)

user_string = str(input('Введите слово,для которого необходимо посчитать стоимость: ')).lower()

char = list(user_string)
sum = 0
for j in char:
    sum = sum + int(dict.get(j))
print(sum)


