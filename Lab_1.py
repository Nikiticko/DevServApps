
class Book:
    def __init__(self, id_, title, authors, publisher, year, pages, price, binding_type):
        self.id = id_
        self.title = title
        if isinstance(authors, list):
            self.authors = authors
        else:
            self.authors = [authors]
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.price = price
        self.binding_type = binding_type
    
    def __str__(self):
        authors_str = ", ".join(self.authors)
        if self.binding_type:
            binding_str = "Твёрдый"
        else:
            binding_str = "Мягкий"
        return f"[{self.id}] «{self.title}» — {authors_str}; {self.publisher}, {self.year}. {self.pages} стр. Цена: {self.price:.2f} ₽. Переплёт: {binding_str}."

    # a) Статический метод для поиска книг заданного автора
    @staticmethod
    def find_by_author(books, author_name):
        result = []
        for book in books:
            for author in book.authors:
                if author_name.lower() in author.lower():
                    result.append(book)
                    break
        return result

    # b) Статический метод для поиска книг заданного издательства
    @staticmethod
    def find_by_publisher(books, publisher_name):
        result = []
        for book in books:
            if publisher_name.lower() in book.publisher.lower():
                result.append(book)
        return result

    @staticmethod
    def find_after_year(books, year):
        result = []
        for book in books:
            if book.year > year:
                result.append(book)
        return result
    
    @staticmethod
    def print_books(book_list, title):
        print(f"\n=== {title} ===")
        if book_list:
            for book in book_list:
                print(book)
        else:
            print("— список пуст —")
    



if __name__ == "__main__":
    import os
    os.system("cls")
    books = [
        Book(1, "книга1", ["автор1"], "издательство1", 2020, 100, 1000.00, True),
        Book(2, "книга2", ["автор2"], "издательство2", 2019, 200, 1500.00, False),
        Book(3, "книга3", ["автор1"], "издательство1", 2022, 150, 1200.00, True),
        Book(4, "книга4", ["автор3", "автор4"], "издательство3", 2018, 300, 2000.00, True),
        Book(5, "книга5", ["автор5"], "издательство2", 2015, 250, 1800.00, True),
        Book(6, "книга6", ["автор1"], "издательство1", 2016, 180, 1300.00, False),
        Book(7, "книга7", ["автор6"], "издательство3", 2021, 220, 1600.00, True),
    ]
    
    print("Массив объектов Book создан.")
    print("Демонстрация работы методов класса Book:")
    print()

    for book in Book.find_by_author(books, "автор1"):
        print(book)
    print()

    for book in Book.find_by_publisher(books, "издательство1"):
        print(book)
    
    # c) Список книг, выпущенных после заданного года
    print()
    for book in Book.find_after_year(books, 2019):
        print(book)
