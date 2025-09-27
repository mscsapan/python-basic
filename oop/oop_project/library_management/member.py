class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"{self.name} বইটি নিতে পারছে না, অন্য কেউ আগে নিয়েছে!")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name}, তুমি তো '{book.title}' বই নিইনি!")

    def __str__(self):
        return f"মেম্বার: {self.name}, ধার করা বই: {[b.title for b in self.borrowed_books]}"