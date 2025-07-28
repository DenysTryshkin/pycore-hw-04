from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                id_, name, age = line.strip().split(",")
                cats_info.append({
                    "id": id_,
                    "name": name,
                    "age": age})
        return cats_info
    
    except Exception as e:
        print(f"Error: {e}")
        return []


cats_info = get_cats_info("/Users/denys/Desktop/python/pycore-hw-04/task_2/cats_file.txt")
print(cats_info)
