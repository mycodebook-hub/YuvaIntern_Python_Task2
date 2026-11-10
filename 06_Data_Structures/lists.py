
print("PYTHON LIST DEMONSTRATION")

# Creating a list
subjects = ["Python", "Java", "DBMS", "HTML"]

print("Original List:", subjects)

# Accessing elements
print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

# Adding an element
subjects.append("C++")
print("After Append:", subjects)

# Inserting an element
subjects.insert(1, "Computer Networks")
print("After Insert:", subjects)

# Removing an element
subjects.remove("HTML")
print("After Remove:", subjects)

# Updating an element
subjects[0] = "Python Programming"
print("After Update:", subjects)

# Displaying list length
print("List Length:", len(subjects))

# Sorting a list
numbers = [40, 10, 30, 20]
numbers.sort()
print("Sorted Numbers:", numbers)

# Iterating through a list
print("List Elements:")

for subject in subjects:
    print(subject)

print("List Demonstration Completed")
