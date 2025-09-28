class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.__students = []   # private list
        self.__teachers = []

    def add_student(self, student):
        self.__students.append(student)

    def add_teacher(self, teacher):
        self.__teachers.append(teacher)

    def show_students(self):
        print("\n👩‍🎓 Student list:")
        for s in self.__students:
            print(s)

    def show_teachers(self):
        print("\n👨‍🏫 Teacher list:")
        for t in self.__teachers:
            print(t)