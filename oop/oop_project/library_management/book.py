class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True   # initially all books will be available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"✅ '{self.title}' The book is booked")
        else:
            print(f"❌ '{self.title}' Not available now")

    def return_book(self):
        self.is_available = True
        print(f"📖 '{self.title}' return to the library")

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"{self.title} - {self.author} ({status})"