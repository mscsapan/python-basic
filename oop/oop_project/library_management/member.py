class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"{self.name} can not get this book because this is already booked by someone")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name}, You have '{book.title}' not booked this booked")

    def __str__(self):
        return f"Member: {self.name}, borrowed: {[b.title for b in self.borrowed_books]}"