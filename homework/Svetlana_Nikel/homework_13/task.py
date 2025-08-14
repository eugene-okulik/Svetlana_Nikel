import os
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
eugene_path = os.path.join(file_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(eugene_path, encoding='utf-8') as file:
    work_file = file.readlines()

for line in work_file:
    line = line.strip()
    parts = line.split(' - ')

    if len(parts) < 2:
        print(f"Строка неподходящего формата: {line}")
        continue

    date_part = parts[0]
    instruction = parts[1]

    try:
        date_str = date_part.split('. ')[1]
    except IndexError:
        print(f"Не удалось извлечь дату из строки: {line}")
        continue

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        print(f"Неверный формат даты: {date_str}")
        continue

    if 'неделю позже' in instruction:
        new_date = date + timedelta(weeks=1)
        print(f"Дата через неделю: {new_date}")
    elif 'день недели' in instruction:
        day_name = date.strftime('%A')  # День недели (на англ.)
        print(f"День недели: {day_name}")

    elif 'дней назад' in instruction:
        now = datetime.now()
        days_ago = (now - date).days
        print(f"Эта дата была {days_ago} дней назад")

    else:
        print(f"Неизвестная инструкция {instruction}")

print("Задачка заставила попыхтеть :)")
