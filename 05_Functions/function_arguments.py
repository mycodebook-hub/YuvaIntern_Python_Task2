
print("PYTHON FUNCTION ARGUMENTS")

# Function with two arguments
def add_numbers(a, b):
    print("Addition:", a + b)

# Function with a default argument
def greet(name="Student"):
    print("Hello", name)

# Function with keyword arguments
def display_student(name, marks):
    print("Student Name:", name)
    print("Marks:", marks)

# Calling functions
add_numbers(10, 20)

greet()
greet("Alex")

display_student(marks=85, name="Alex")

print("Function Arguments Completed")
