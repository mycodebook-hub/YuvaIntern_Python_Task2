
print("PYTHON DICTIONARY DEMONSTRATION")

# Creating a dictionary
student = {
    "name": "Alex",
    "age": 18,
    "marks": 85
}

print("Original Dictionary:", student)

# Accessing values
print("Student Name:", student["name"])
print("Student Age:", student["age"])

# Adding a new key-value pair
student["course"] = "Python"
print("After Adding:", student)

# Updating a value
student["marks"] = 90
print("After Updating:", student)

# Removing an element
student.pop("age")
print("After Removing:", student)

# Displaying all keys
print("Dictionary Keys:", student.keys())

# Displaying all values
print("Dictionary Values:", student.values())

# Displaying all key-value pairs
print("Dictionary Items:")

for key, value in student.items():
    print(key, ":", value)

# Dictionary length
print("Dictionary Length:", len(student))

print("Dictionary Demonstration Completed")
