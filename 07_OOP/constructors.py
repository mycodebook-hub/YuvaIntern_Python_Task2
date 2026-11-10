class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


student1 = Student("Alex", 18)
student2 = Student("Sam", 19)

student1.display()
student2.display()