class Person:
    def __init__(self, name):
        self.name = name

class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book):
        library.add_book(book)
        print(f"👩‍💼 {self.name} '{book.title}' লাইব্রেরিতে যোগ করলেন।")