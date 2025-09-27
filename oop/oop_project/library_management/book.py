class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True   # শুরুতে বই পাওয়া যাবে

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"✅ '{self.title}' বইটি ইস্যু করা হলো।")
        else:
            print(f"❌ '{self.title}' এখন পাওয়া যাচ্ছে না!")

    def return_book(self):
        self.is_available = True
        print(f"📖 '{self.title}' ফেরত দেওয়া হলো!")

    def __str__(self):
        status = "মজুদ আছে" if self.is_available else "ইস্যু হয়ে গেছে"
        return f"{self.title} - {self.author} ({status})"