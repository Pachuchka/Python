__all__ =['write_random_pairs_to_file']

import os
import random
MIN = -1000
MAX = 1000

def write_random_pairs_to_file(file_path, num_pairs):
    with open(file_path, 'w') as f:
        for _ in range(num_pairs):
            int_num = random.randint(MIN, MAX)
            float_num = random.uniform(MIN, MAX)
            f.write(f"{int_num}|{float_num:.2f}\n")

if __name__ == '__main__':
    file_path = "C:\Study\Python\lesson_7\examples\файл-file01.docx"
    num_pairs = 5
    write_random_pairs_to_file(file_path, num_pairs)




