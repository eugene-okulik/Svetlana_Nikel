class Book:
    page_material = 'бумага'
    text = True
    reserved = False

    def __init__(self, name, author, number_of_pages, isbn):
        self.name = name
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = isbn

    def reserved_info(self):
        reserved_info = ', зарезервирована' if self.reserved else ""
        return (f"Название: {self.name}, Автор: {self.author}, страниц: {self.number_of_pages}, "
                f"материал: {self.page_material}{reserved_info}")


book_1 = Book('Мастер и Маргарита', 'Булгаков', 600, '978-5-699-12014')
book_2 = Book('Идиот', 'Достоевский', 500, '978-5-699-35614')
book_3 = Book('Преступление и наказание', 'Достоевский', 550, '978-5-909-35614')
book_4 = Book('Война и мир', 'Толстой', 1300, '978-5-888-35614')
book_5 = Book('Гарри Поттер - 1 часть', 'Джоанн Роллинг', 500, '978-5-699-35674')

book_2.reserved = True

for book in [book_1, book_2, book_3, book_4, book_5]:
    print(book.reserved_info())


class SchoolBook(Book):
    def __init__(self, name, author, number_of_pages, isbn, subject, number_class, task):
        super().__init__(name, author, number_of_pages, isbn)
        self.subject = subject
        self.number_class = number_class
        self.task = task

    def reserved_info(self):
        reserved_info = ', зарезервирована' if self.reserved else ""
        return (f"Название: {self.name}, Автор: {self.author}, страниц: {self.number_of_pages}, "
                f"предмет: {self.subject}, класс: {self.number_class}{reserved_info}")


schoolbook_1 = SchoolBook('Алгебра', 'Иванов', 200, '978-5-09-482950-1', 'Математика', 9, True)
schoolbook_2 = SchoolBook('Русский язык', 'Грибнев', 300, '978-5-45-078980-1', 'Русский язык', 6, True)

schoolbook_2.reserved = True

for book in [schoolbook_1, schoolbook_2]:
    print(book.reserved_info())
