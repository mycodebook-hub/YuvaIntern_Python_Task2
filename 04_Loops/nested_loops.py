
print("PYTHON NESTED LOOPS")

# Printing a number pattern
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")
    print()

# Multiplication table
print("Multiplication Table:")

for number in range(1, 4):
    for multiplier in range(1, 4):
        print(number * multiplier, end=" ")
    print()

print("Nested Loops Completed")
