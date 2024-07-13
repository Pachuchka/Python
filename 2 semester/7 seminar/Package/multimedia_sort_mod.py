
__all__ = ['sort_files']
import os
import shutil

def sort_files(root_dir):
    # Создаем директории для видео, музыки и изображений
    video_dir = os.path.join(root_dir, 'Видео')
    music_dir = os.path.join(root_dir, 'Музыка')
    image_dir = os.path.join(root_dir, 'Изображения')
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(music_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    # Словари с расширениями для каждого типа файлов
    video_exts = ['.mp4', '.avi', '.mkv', '.mov']
    music_exts = ['.mp3', '.wav', '.ogg']
    image_exts = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    # Перебираем все файлы в директории
    for filename in os.listdir(root_dir):
        filepath = os.path.join(root_dir, filename)
        if os.path.isfile(filepath):
            # Определяем тип файла по расширению
            ext = os.path.splitext(filename)[1].lower()
            if ext in video_exts:
                shutil.move(filepath, video_dir)
            elif ext in music_exts:
                shutil.move(filepath, music_dir)
            elif ext in image_exts:
                shutil.move(filepath, image_dir)

if __name__ == '__main__':
    sort_files(r'C:\Study\Python\2 semester\7 seminar\multimedia')