
__all__ = ['generate_names']
import os
import random
import string

def generate_names(directory, num_names):
    vowels = 'AEIOU'
    names = []

    
    for _ in range(num_names):
        
        name = random.choice(string.ascii_uppercase)
        while True:
            seq = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(2, 10)))
            if any(c in vowels.lower() for c in seq):
                break
        name += seq
        names.append(name)
    file_path = os.path.join(directory, 'pseudo_names.txt')
    with open(file_path, 'w') as f:
        f.write('\n'.join(names))

    print(f"Сгенерировано очередное имя и сохранено {file_path}")

if __name__ == '__main__':
    directory = "C:\Study\Python\lesson_7\examples"
    num_names = 10
    generate_names(directory, num_names)