import mysql.connector as mysql
import dotenv
import os
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME'),
    use_pure=True
)

csv_path = "C:/Users/mzsve/projects/Svetlana_Nikel/homework/eugene_okulik/Lesson_16/hw_data/data.csv"

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    csv_data = list(csv.DictReader(csvfile))

select_query = '''
SELECT
    s.name AS name,
    s.second_name AS second_name,
    g.title AS group_title,
    b.title AS book_title,
    sb.title AS subject_title,
    l.title AS lesson_title,
    m.value AS mark_value
FROM students s
JOIN books b ON s.id = b.taken_by_student_id
JOIN `groups` g ON s.group_id = g.id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sb ON l.subject_id = sb.id
'''

cursor = db.cursor(dictionary=True)
cursor.execute(select_query)
db_data = cursor.fetchall()

missing_data = [row for row in csv_data if row not in db_data]

if missing_data:
    print(f"\nОтсутствует {len(missing_data)} записей в базе:")
    for i, row in enumerate(missing_data, 1):
        print(f"\n{i}. {row}")
else:
    print("\nВсе данные из файла присутствуют в базе!")

db.close()
