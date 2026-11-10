
print("PYTHON NESTED IF STATEMENT")

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18:
    print("Age condition satisfied")

    if has_ticket == "yes":
        print("You can enter")
    else:
        print("Ticket is required")

else:
    print("Age condition not satisfied")

print("Nested If Statement Completed")
