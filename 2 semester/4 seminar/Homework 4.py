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
import typing
def dict_of_args(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not isinstance(value, typing.Hashable):
            value = str(value)
        result[value] = key
    return result
print(dict_of_args(first = 1, second = 2, third = "third`s", fourth = [1,2,3,4,5]))