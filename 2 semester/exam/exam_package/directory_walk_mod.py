
__all__ = ['directory_walk']

import os
import json
import csv
import pickle

def directory_walk(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            result.append({
                'path': file_path,
                'parent': root,
                'type': 'file',
                'size': file_size
            })
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = sum(os.path.getsize(os.path.join(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)))
            result.append({
                'path': dir_path,
                'parent': root,
                'type': 'directory',
                'size': dir_size
            })
    
    with open('result.json', 'w') as f:
        json.dump(result, f, indent=4)
    
    with open('result.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Parent', 'Type', 'Size'])
        for item in result:
            writer.writerow([item['path'], item['parent'], item['type'], item['size']])
    
    with open('result.pickle', 'wb') as f:
        pickle.dump(result, f)

if __name__ == '__main__':
    directory_walk(r'C:\Study\Python')