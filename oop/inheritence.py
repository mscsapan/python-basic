# class Person:
#     def __init__(self,name,age,address:str):
#         self.name = name
#         self.age = age
#         self.address = address


# class Student(Person):
#     pass

# p1 = Student('Ali',27,'Dhaka')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        # Person.__init__(self,name,age)
        super().__init__(name, age)


p1 = Student('Ali', 27)

print(p1.name)

print('hello bangladesh')
