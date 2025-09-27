from library import Library
from librarian import Librarian
from book import Book
from member import Member

# লাইব্রেরি তৈরি
lib = Library("Dhaka City Library")

# বই তৈরি
b1 = Book("Python Basics", "Guido van Rossum")
b2 = Book("Machine Learning", "Andrew Ng")
b3 = Book("Bangla Literature", "Humayun Ahmed")

# মেম্বার তৈরি
m1 = Member("Rahim")
m2 = Member("Karim")

# লাইব্রেরিয়ান
librarian = Librarian("Mr. Ali")

# বই ও মেম্বার অ্যাড করা
librarian.add_book(lib, b1)
librarian.add_book(lib, b2)
librarian.add_book(lib, b3)

lib.add_member(m1)
lib.add_member(m2)

# লাইব্রেরির বর্তমান অবস্থা
lib.show_books()
lib.show_members()

# মেম্বার বই ধার নিচ্ছে
m1.borrow_book(b1)   # Rahim first
m2.borrow_book(b1)   # Karim wants same book (not available)

# বই ফেরত দেওয়া
m1.return_book(b1)

# Karim আবার চাইলে এখন পারবে
m2.borrow_book(b1)

# আপডেট অবস্থা
lib.show_books()
lib.show_members()