
print("PYTHON RECURSION")

# Recursive function to calculate factorial
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# Getting input from the user
number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers")
else:
    result = factorial(number)
    print("Factorial:", result)

print("Recursion Completed")
