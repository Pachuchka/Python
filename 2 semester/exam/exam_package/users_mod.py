__all__ = ['input_user']

import json
from pathlib import Path

def input_user(path: Path) -> None:
    unique_id = set()
    if not path.is_file():
        data = {level:{} for level in range(1,8)}
    else:
        with open(path, 'r', encoding = 'UTF-8') as f_read:
            data = json.load(f_read)
            for id_name in data.values():
                unique_id.update(id_name.keys())
    while name := input("Input user name: "):
        user_id = int(input("Input user id: "))
        level = int(input("Input security level from 1 to 7: "))
        if user_id not in unique_id:
            unique_id.add(user_id)
            data[level].update({user_id: name})
            with open(path,'w',encoding="UTF-8") as f_write:
                json.dump(data,f_write, indent = 4, ensure_ascii=False)
                
        else:
            print("Такой id пользователя сущестует")
            
if __name__ == '__main__':
    input_user(Path("users.json"))