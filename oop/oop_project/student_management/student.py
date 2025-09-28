class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.grades = []   # খালি লিস্ট (পরে মার্ক যোগ করা হবে)

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Name: {self.name}, Roll: {self.roll}, Avg Number: {self.average_grade():.2f}"