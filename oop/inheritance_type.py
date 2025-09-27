# 1. Single-level: Direct parent-child (basic car example).
# 2. Multi-level: Chain of inheritance (LivingBeing → Dog).
# 3. Multiple: Child inherits from 2+ parents (Smartphone).
# 4. Hierarchical: One parent → Many children (Shapes).
# 5. Hybrid: Combo (Working student).



# 1. Single-level Inheritance
# One parent → One child.
# 👉 Real life analogy: A Vehicle class as parent and Car as child.

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
    
    def info(self):
        print(f"This vehicle has {self.wheels} wheels.")

class Car(Vehicle): 
    def drive(self):
        print("Car is on the road!")


c = Car(4)
c.info()
c.drive()


# 2. Multi-level Inheritance
# Parent → Child → Grandchild.
# 👉 Real life analogy: LivingBeing → Animal → Dog.

class LivingBeing:
    def breathe(self):
        print("Breathing...")

class Animal(LivingBeing):
    def eat(self):
        print("Animal is eating...")

class Dog(Animal):
    def bark(self):
        print("Dog is barking...")

# Example use
dog = Dog()
dog.breathe()  # from LivingBeing
dog.eat()      # from Animal
dog.bark()     # from Dog


# 3. Multiple Inheritance
# A child inherits from two or more unrelated parents.
# 👉 Real life analogy: A Smartphone inherits both from Phone and Camera.

class Phone:
    def call(self):
        print("Making a call...")

class Camera:
    def capture(self):
        print("Taking a photo...")

class Smartphone(Phone, Camera):  # multiple inheritance
    def browse(self):
        print("Browsing the internet...")

# Example use
sp = Smartphone()
sp.call()       # from Phone
sp.capture()    # from Camera
sp.browse()     # from Smartphone


# 4. Hierarchical Inheritance
# One parent → Multiple children.
# 👉 Real life analogy: Shape → Circle, Square, Rectangle.

class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s * self.s

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

shapes = [Circle(5), Square(4), Rectangle(3,6)]
for s in shapes:
    print(s.area())
    
    
# 5. Hybrid Inheritance
# A mix of types (multi-level + multiple).
# 👉 Real life analogy: Person → Employee & Student → WorkingStudent.

class Person:
    def __init__(self, name): self.name = name

class Employee(Person):
    def work(self): print(f"{self.name} is working.")

class Student(Person):
    def study(self): print(f"{self.name} is studying.")

class WorkingStudent(Employee, Student):  # hybrid
    def balance(self):
        print(f"{self.name} balances work and study.")

ws = WorkingStudent("Alex")
ws.work()
ws.study()
ws.balance()


# 🧠 Advanced Discussion: Multiple Inheritance & MRO
# ❓ Problem
# If two parents have a method with the same name, which one does Python choose?

class A:
    def action(self): print("From A")

class B:
    def action(self): print("From B")

class C(A, B):
    pass

c = C()
c.action()

# 👉 Output: From A.

# Why? Because Python uses MRO (Method Resolution Order) left-to-right.
# Check it by:

print(C.mro())


# ⭐ Cooperative Multiple Inheritance
# To properly share across parents, we use super() with *args, **kwargs.

class A:
    def __init__(self, *args, **kwargs):
        print("Init A")
        super().__init__(*args, **kwargs)

class B:
    def __init__(self, *args, **kwargs):
        print("Init B")
        super().__init__(*args, **kwargs)

class C(A, B):
    def __init__(self, *args, **kwargs):
        print("Init C")
        super().__init__(*args, **kwargs)

c = C()

# 👉 Output:
#     Init C
#     Init A
#     Init B


# 🥳 Everyone gets initialized nicely!
# This is considered a best practice for multiple inheritance in Python.



