verse = input("Введите строку:")

yes = "Парам пам-пам"
no = "Пам парам"

def check(message):
    vowels = set("аеёиоуяэю")
    count = 0
    for symbol in message:
        if symbol in vowels:
            count += 1
    return count

versus = map(check,verse.split())
if len(set(map(check,verse.split())))==1:
    print(yes)
else:
    print(no)


