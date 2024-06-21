#Задача №1
#  Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
# LIMIT = 1

# user_text = input("Введите свой список, перечислив элементы через запятую:")
# user_list = user_text.split(",")
# user_dict = {}
# for element in user_list:
#     count = sum(1 for x in user_list if x == element)
#     if count > LIMIT:
#         user_dict[element] = count
# print(list(user_dict))

#Задача №2
# В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.
# import re

# user_text = input("Введите текст для подчсёта: ")
# user_text = re.sub(r'[^\w\s]', '', user_text).lower()
# list_of_words = user_text.split()
# words_count = len(list_of_words)
# dict_of_words = {}
# for element in list_of_words:
#     count = sum(1 for x in list_of_words if x == element)
#     dict_of_words[element] = count
# sort_data = sorted(dict_of_words.items(), key=lambda x: x[1], reverse=True)
# print(f'в представленном тексте {words_count} слов')
# print("Самые распространённые:")
# sort_data_dict = dict(sort_data)
# for key in list(sort_data_dict.keys())[:10]:
#     print(key)

#Задача №3
#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
#Достаточно вернуть один допустимый вариант
#*Верните все возможные варианты комплектации рюкзака.

STEP = 1
MIN_VOLUME = 0.9

import itertools
items = {'палатка': '4.5', 'спальник': '2.5','коврик': '0.5', 'термос':'1', 'топор':'1.5', 'пакет с одеждой':'4', \
'консарвная банка':'0.5', 'бутылка воды':'1', 'котелок':'0.2', 'пакет с едой':'4', 'медикаменты':'2'}
backpack_volume = int(input("Введите объём рюкзака: "))
combinations = []
for i in range(STEP, len(list(items.values())) + STEP):
    for combination in itertools.combinations(list(items.values()), i):
        if sum([float(x) for x in combination]) <= backpack_volume and sum([float(x) for x in combination]) > MIN_VOLUME * backpack_volume:
            combinations.append(items.keys())
print(combinations)