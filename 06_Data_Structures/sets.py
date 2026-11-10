
print("PYTHON SET DEMONSTRATION")

# Creating a set
numbers = {10, 20, 30, 20, 40}

print("Original Set:", numbers)

# Adding an element
numbers.add(50)
print("After Adding:", numbers)

# Removing an element
numbers.remove(30)
print("After Removing:", numbers)

# Updating a set
numbers.update([60, 70])
print("After Update:", numbers)

# Checking membership
print("20 in Set:", 20 in numbers)

# Set union
first_set = {10, 20, 30}
second_set = {30, 40, 50}

print("Union:", first_set.union(second_set))

# Set intersection
print("Intersection:", first_set.intersection(second_set))

# Set difference
print("Difference:", first_set.difference(second_set))

print("Set Length:", len(numbers))

print("Set Demonstration Completed")
