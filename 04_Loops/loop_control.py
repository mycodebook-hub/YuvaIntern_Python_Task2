
print("PYTHON LOOP CONTROL STATEMENTS")

# Break statement
print("Break Statement:")

for number in range(1, 6):
    if number == 4:
        break
    print(number)

# Continue statement
print("Continue Statement:")

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# Pass statement
print("Pass Statement:")

for number in range(1, 4):
    if number == 2:
        pass
    print(number)

print("Loop Control Completed")
