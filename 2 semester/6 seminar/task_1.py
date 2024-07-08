# Модуль проверки дат.
# Модуль содержит функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать по Григорианскому календарю и ложь, если такая дата не возможна
# Год может изменяться в диапазоне от 1 до 9999
# В отдельной защищённой функции реализовать проверку года на високосность



from sys import argv

def _is_leap(year:int)->bool:
    return year%4 == 0 and year%100 !=0 or year%400 ==0

def date_is_true(data: str) -> bool:
    print (data)
    """
    Returns True if the date string is valid, False otherwise.
    """
    day, month, year = map(int, data.split('.'))
    
    # Define a dictionary to store the maximum days for each month
    max_days = {
        1: 31,
        2: 29 if _is_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    
    # Check if the year is within the valid range
    if not (1 <= year <= 9999):
        print("Year is out of range")
        return False
    
    # Check if the month is valid
    if not (1 <= month <= 12):
        print("Invalid month")
        return False
    
    # Check if the day is within the valid range for the month
    max_day = max_days.get(month)
    if not (1 <= day <= max_day):
        print("Day is out of range for the month")
        return False
    
    # If all checks pass, the date is valid
    print("Дата существует")
    return True

if __name__ == '__main__':
    #print(date_is_true("01.13.2024"))
    #print(date_is_true("32.11.2024"))
    #print(date_is_true("20.11.10000"))
    #print(date_is_true("29.02.2023"))
    date_string = argv[1]
    print (date_string)
    date_is_true(date_string)
