from sys import argv
import random

BOARD_SIDE = 8
NUM_SIDE = 2
STEP = 1
START = 1

#Представим шахматную доску как словарь из 64 ключей (клеток), где каждому ключу сопоставлено одно из 3 значений
#0 - клетка пустая и не находится под ударом выставленных на поле фигур
#1 - на клетке размещён ферзь
#-1 - клетка пуста, но находитсчя под ударом хотя бы одного ферзя

_chessboard = {i: 0 for i in range(START, BOARD_SIDE ** NUM_SIDE + STEP )}

# в отдельном списке будем хранить ячейки с уже размещёнными фигурами
_queens = ()

def cells_under_attack(chessboard, x:int, y:int):
    # пускай функция получает на вход координаты клетки, в которой размещается очередная фигура
    # преобразуем координаты к номеру клетки (ключу словаря клеток)
    cell_number = (x - 1) * BOARD_SIDE + y
    queens_cells = [cell for cell, value in chessboard.items() if value == 1]
    # пометим клетки полей, попавших под бой очередной фигуры по горизонтари и вертикали

    for i in range(START, BOARD_SIDE+STEP):
        if i!= y:
            chessboard[(x - STEP) * BOARD_SIDE + i] = -1
    for i in range(1, BOARD_SIDE+STEP):
        if i!= x:
            chessboard[(i - STEP) * BOARD_SIDE + y] = -1
    # а теперь пометим клетки полей, попавших под бой по диагонали
    for i, j in zip(range(x - STEP, 0, - STEP), range(y - STEP, 0, -STEP)):
        chessboard[(i - STEP) * BOARD_SIDE + j] = -1
    for i, j in zip(range(x + STEP, BOARD_SIDE+STEP), range(y +  STEP, BOARD_SIDE+STEP)):
        chessboard[(i - STEP) * BOARD_SIDE + j] = -1
    for i, j in zip(range(x - 1, 0, -1), range(y +  STEP, BOARD_SIDE+STEP)):
        chessboard[(i - STEP) * BOARD_SIDE + j] = -1
    for i, j in zip(range(x + 1, BOARD_SIDE+STEP), range(y -  STEP, 0, -STEP)):
        chessboard[(i - STEP) * BOARD_SIDE + j] = -1

    # Пометим саму ячейку куда встала очередная фигура

    chessboard[cell_number] = 1
    for key in _chessboard:
        if key in queens_cells:
            _chessboard[key] = 1
    print_chessboard(_chessboard)
    print(queens_cells)

def print_chessboard(chessboard):

    #Данная функция рисует текущее состояние шахматной доски, размечая клекти под боем и безопасные клетки

    for i in range(BOARD_SIDE):
        row = []
        for j in range(BOARD_SIDE):
            square_num = i * BOARD_SIDE + j + STEP
            if chessboard[square_num] == 0:
                row.append('.')
            elif chessboard[square_num] == 1:
                row.append('Q')
            elif chessboard[square_num] == -1:
                row.append('*')
        print(' '.join(row))
    queens_cells = [cell for cell, value in chessboard.items() if value == 1]
    print(queens_cells)
    empty_cells = [cell for cell, value in chessboard.items() if value == 0]
    print(empty_cells)
    return None

def _choose_random_empty_square(chessboard):

    #Рандомизатор который случайным образом выбирает куда поставить очередного ферзя

    empty_cells = [cell for cell, value in chessboard.items() if value == 0]
    cell = random.choice(empty_cells)
    print((cell//BOARD_SIDE)+STEP)
    print(cell-(cell//BOARD_SIDE)*BOARD_SIDE)
    cells_under_attack(_chessboard, (cell//BOARD_SIDE)+STEP, (cell-(cell//BOARD_SIDE)*BOARD_SIDE))

def _next_queen():

    choice = int(input("Выберите способ расстановки: 1 - ввести вручную, 2 - поставить случайным образом"))
    if choice == 1:
        x,*y = n = map(int, input("Введите координаты клетки через пробел").split())
        cells_under_attack(_chessboard, x, y[0])
    elif choice == 2:
        _choose_random_empty_square(_chessboard)
    else:
        return False
    _next_queen()

def close_cells(x, y):
        #Возвращает сет клеток под боем
        under_attack = set()
        for i in range(8):
            under_attack.add((x, i))
            under_attack.add((i, y))  
            if x + i < 8 and y + i < 8:
                under_attack.add((x + i, y + i))
            if x - i >= 0 and y + i < 8:
                under_attack.add((x - i, y + i))
            if x + i < 8 and y - i >= 0:
                under_attack.add((x + i, y - i))  
            if x - i >= 0 and y - i >= 0:
                under_attack.add((x - i, y - i))  
        return under_attack    
def queens_attack_each_other(queen_positions):
    #Возвращает истину, если хотя бы 1 ферзь бьёт другого, иначе ложь

    for i in range(len(queen_positions)):
        for j in range(i + 1, len(queen_positions)):
            x1, y1 = queen_positions[i]
            print(queen_positions[i])
            x2, y2 = queen_positions[j]
            print(queen_positions[j])
            #if (x2, y2) in cells_under_attack(x1, y1):
            if (x2, y2) in close_cells(x1, y1):
                print("Ферзи бьют друг друга")
                return True
    print("Ферзи не бьют друг друга")        
    return False


if __name__ == '__main__':
    #_next_queen()
    #  C:\Study\Python\2 semester\6 seminar> python .\task_2.py "1,1 2,3 4,4"
    queen_positions = [tuple(map(int, pos.split(','))) for pos in argv[1].split()]
    print (len(queen_positions))
    queens_attack_each_other(queen_positions)