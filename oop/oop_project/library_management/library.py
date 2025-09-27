class Library:
    def __init__(self, name):
        self.name = name
        self.__books = []    # private list
        self.__members = []

    def add_book(self, book):
        self.__books.append(book)

    def add_member(self, member):
        self.__members.append(member)

    def show_books(self):
        print("\n📚 লাইব্রেরির বইয়ের তালিকা:")
        for b in self.__books:
            print(b)

    def show_members(self):
        print("\n👥 মেম্বার তালিকা:")
        for m in self.__members:
            print(m)