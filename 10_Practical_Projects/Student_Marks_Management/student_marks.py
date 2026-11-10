
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return (self.calculate_total() / 300) * 100

    def display_details(self):
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total Marks:", self.calculate_total())
        print("Percentage:", self.calculate_percentage(), "%")

        if all(mark >= 35 for mark in self.marks):
            print("Result: Pass")
        else:
            print("Result: Fail")


name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = float(input("Enter subject " + str(i + 1) + " marks: "))
    marks.append(mark)

student = Student(name, marks)

student.display_details()
