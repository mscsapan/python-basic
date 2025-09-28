from school import School
from teacher import Teacher
from student import Student

# create object
s1 = Student("Rahim", 101)
s2 = Student("Karim", 102)

s1.add_grade(80)
s1.add_grade(90)

s2.add_grade(70)
s2.add_grade(75)

t1 = Teacher("Mr. Ali", "Mathematics")
t2 = Teacher("Mrs. Jahan", "Physics")

school = School("Dhaka Ideal School")

# Add students & teachers
school.add_student(s1)
school.add_student(s2)

school.add_teacher(t1)
school.add_teacher(t2)

# Show data
school.show_students()
school.show_teachers()