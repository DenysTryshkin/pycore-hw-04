from pathlib import Path

def total_salary(path):
    total_sum = 0
    developer_count = 0
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                _, salary = line.strip().split(",")
                total_sum += float(salary)
                developer_count += 1

        if developer_count == 0:
            return 0, 0        

        average_salary = total_sum / developer_count
        return total_sum, average_salary
    
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return 0, 0    


total, average = total_salary("/Users/denys/Desktop/python/pycore-hw-04/task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
