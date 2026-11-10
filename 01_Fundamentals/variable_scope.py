
print("PYTHON VARIABLE SCOPE DEMONSTRATION")

# Global variable
college = "ABC College"

def display_details():
    # Local variable
    student = "Alex"
    print("Student Name:", student)
    print("College Name:", college)

# Calling the function
display_details()

# Modifying a global variable
count = 10

def update_count():
    global count
    count = 20

update_count()

print("Updated Count:", count)

print("Variable Scope Demonstration Completed")
