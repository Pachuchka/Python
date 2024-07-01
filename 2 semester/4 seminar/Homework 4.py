#Задача №1 Напишите функцию транспонирования матрицы

# matrix_A = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(matrix_A)
# def transpose(matrix):
#     transp_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             transp_matrix [j][i] = matrix[i][j]
#     return transp_matrix
# print(transpose(matrix_A))

#Задача #2 
#Напишите функцию принимающую на вход только ключевые параметры 
#и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
#Если ключ не хешируем, используйте его строковое представление.
# import typing
# def dict_of_args(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if not isinstance(value, typing.Hashable):
#             value = str(value)
#         result[value] = key
#     return result
# print(dict_of_args(first = 1, second = 2, third = "third`s", fourth = [1,2,3,4,5]))

#Задача №3 Банкомат:

#реализуйте функци пополнения, снятия, выхода, вычета комиссии

#Суммы пополнения и снятия кратны 50 у.е.

#Комиссия равна 1.5% от суммы снятия но не менее 30 и не более 600 у.е

#После каждой 3 операции снятия или пополнения, начисляются проценты - 3%

#При превышении суммы транзакции в 5 млн., изымать налог на роскошь в размере 10% от суммы каждой операции

import sys
import decimal

MULTIPLICITY = 50
PERCENT = decimal.Decimal(15)/decimal.Decimal(1000)
BONUS = decimal.Decimal(3)/decimal.Decimal(100)
MIN_LIMIT = decimal.Decimal(30)
MAX_LIMIT = decimal.Decimal(600)
PERCENT_RICHNESS = decimal.Decimal(10)/decimal.Decimal(100)
RICHNESS_AMOUNT = 5_000_000
ZERO = 0
OPERATIONS_STEP = 1


clients_pins = {1:'111', 2:'222', 3:'333'}
clients_account = {1:'1110', 2:'2220', 3:'3330'}
accounts_balance = {1:0, 2:0, 3:0}
clients_operation_count = {1:0, 2:0, 3:0}


def hello():

    id = input("Введите свой id: ")

    if id in clients_account.values():

        keys = list(clients_account.keys())

        index = list(clients_account.values()).index(id)

        key = keys[index]

        authentication(key)

    else:

        print("Такого клиента не обнаружено")

def authentication(id):

    pin = str(input("Введите pin-code: "))
    if pin == clients_pins.get(id):
        choice = int(input("Если вы хотите пополнить свой депозит, нажмите - 1, если вы хотите снять наличные, нажмите 2, завершить обслуживание - нажмите 3: "))
        if choice == 1: replenishment(id)
        if choice == 2: withdrawal(id)
        if choice == 3: exit()
        else:
            print("Команда не распознана, введите снова")
            authentication(id)
    else:
        print("pin code отклонён")

def replenishment(id):

    amount = int(input("Введите сумму пополнения"))

    while amount < 0 or amount % MULTIPLICITY != ZERO:

        amount = int(input("Сумма пополнения должна быть положительной и кратной 50 у.е., введите корректную сумму"))

    if amount > RICHNESS_AMOUNT:

        amount += - take_tax(id, amount)

    accounts_balance[id] += amount

    print(f'На ваш счёт зачислено {amount} у.е. * С учётом налогов и сборов')

    bonus(id,amount)

    authentication(id)

def withdrawal(id):

    choice = int(input("Показать текущий баланс вашего счёта: 1 - да, 2 - нет"))

    if choice == 1:

        print(f'Баланс счёта {id} составляет {accounts_balance[id]}')

        draw = int(input("Введите сумму снятия:"))

    elif choice == 2:

        draw = int(input("Введите сумму снятия:"))

    else: withdrawal(id)

    while draw % MULTIPLICITY != ZERO:

        draw = int(input("Сумма снятия должна быть кратна 50 у.е., введите корректную сумму"))

    draw = draw + calculate_comission(id,draw)

    if draw > ZERO and draw < accounts_balance[id]:

        accounts_balance[id] += - draw

    else:

        print("Не корректные данные, указанная сумма не может быть снята")

        withdrawal(id)

    bonus(id,draw)

    authentication(id)

def exit():

    sys.exit("сеанс завершён")

def calculate_tax(id,value):

    tax = value * PERCENT_RICHNESS

    return tax

def calculate_comission(id,value):

    comission = value * PERCENT

    return comission

def bonus(id,value):

    clients_operation_count[id] += OPERATIONS_STEP

    if clients_operation_count.get(id) % 3 == 0:

        bonus = value * BONUS

        print (f'Вам зачислен бонус в размере {bonus}')

        accounts_balance[id] += bonus

hello()