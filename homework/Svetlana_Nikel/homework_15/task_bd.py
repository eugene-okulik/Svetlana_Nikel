import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl',
    use_pure=True
)

cursor = db.cursor(dictionary=True)
# Добавляем студента
cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", ("Svetlana", "Ivanova"))
student_id = cursor.lastrowid
cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
print("Студент создан:", cursor.fetchone())

# Добавляем книги
books = ["Algebra", "Biology"]
for title in books:
    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", (title, student_id))
    book_id = cursor.lastrowid
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    print("Книга добавлена:", cursor.fetchone())

# Добавляем группу
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ("Faculty of Economics", "2025-09-01", "2029-05-31")
)
group_id = cursor.lastrowid
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (group_id,))
print("Группа создана:", cursor.fetchone())

# Привязываем студента к группе
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))
cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
print("Студент добавлен в группу:", cursor.fetchone())

# Добавляем предметы
subjects = ["Алгебра", "Биология"]
subject_ids = {}
for title in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (title,))
    subject_id = cursor.lastrowid
    subject_ids[title] = subject_id
    cursor.execute("SELECT * FROM subjects WHERE id = %s", (subject_id,))
    print("Предмет добавлен:", cursor.fetchone())

# Добавляем уроки
lessons = [
    ("lesson_alg_1", subject_ids["Алгебра"]),
    ("lesson_alg_2", subject_ids["Алгебра"]),
    ("lesson_bio_1", subject_ids["Биология"]),
    ("lesson_bio_2", subject_ids["Биология"]),
]
lesson_ids = []
for title, subj_id in lessons:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (title, subj_id))
    lesson_id = cursor.lastrowid
    lesson_ids.append(lesson_id)
    cursor.execute("SELECT * FROM lessons WHERE id = %s", (lesson_id,))
    print("Урок добавлен:", cursor.fetchone())

# Добавляем оценки
marks = [5, 5, 4, 4]
for i in range(len(marks)):
    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   (marks[i], lesson_ids[i], student_id))
    mark_id = cursor.lastrowid
    cursor.execute("SELECT * FROM marks WHERE id = %s", (mark_id,))
    print("Оценка добавлена:", cursor.fetchone())

# Всё про студента
cursor.execute("""
SELECT s.id, s.name, s.second_name, g.title AS group_title,
       b.title AS book_title, sb.title AS subject_title,
       l.title AS lesson_title, m.value AS mark_value
FROM students s
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sb ON l.subject_id = sb.id
WHERE s.id = %s
""", (student_id,))

fulls = cursor.fetchall()
print("\n Вся информация про студента")
for full in fulls:
    print(full)

db.commit()
db.close()
