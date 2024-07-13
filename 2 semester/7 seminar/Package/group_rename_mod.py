# Функция группового переименования файлов. 
# Аргументы:
# directory - путь к директории в которой нужно переименовать файлы
# desired_final_name - новое имя, присваиваемое файлам + порядковый номер
# num_digits - размерность порядковых номеров переименованных файлов
# original_ext - расширение исходных файлов, подлежащих переименованию
# final_ext -  конечное расширение файлов
# original_name_range - диапазон сохранения исходного имени, с которого начнётся итоговое имя
#3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
__all__ = ['group_rename_files']

import os

START = 1
STEP = 1

def group_rename_files(directory, desired_final_name, num_digits, original_ext, final_ext, original_name_range):
    # создадим список имён файлов в указанной директории, отфильтровав наименования по наличию оригинального расширения файлов
    files = [f for f in os.listdir(directory) if f.endswith(original_ext)]
    files.sort()
    counter = START

    for file in files:
        # формируем полное имя файла
        file_path = os.path.join(directory, file)
        # получаем имя без расширения
        original_name = os.path.splitext(file)[0]
        # формируем новое имя файла
        original_name_range_str = original_name[original_name_range[0]-1:original_name_range[1]]
        new_name = f"{original_name_range_str}{desired_final_name}{str(counter).zfill(num_digits)}.{final_ext}"
        # формируем новое полное имя файла и переименовываем
        new_file_path = os.path.join(directory, new_name)
        os.rename(file_path, new_file_path)
        counter += STEP

if __name__ == '__main__':
    group_rename_files("C:\Study\Python\lesson_7\examples", "-file", 2, "odt", "docx", [1,4])