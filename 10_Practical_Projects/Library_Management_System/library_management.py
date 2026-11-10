
books = {}


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    if title in books:
        print("Book already exists")
    else:
        books[title] = {
            "author": author,
            "status": "Available"
        }

        print("Book added successfully")


def view_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("\n----- Library Books -----")

        for title, details in books.items():
            print("Title:", title)
            print("Author:", details["author"])
            print("Status:", details["status"])
            print("------------------------")


def search_book():
    title = input("Enter book title to search: ")

    if title in books:
        print("Title:", title)
        print("Author:", books[title]["author"])
        print("Status:", books[title]["status"])
    else:
        print("Book not found")


def issue_book():
    title = input("Enter book title to issue: ")

    if title in books:
        if books[title]["status"] == "Available":
            books[title]["status"] = "Issued"
            print("Book issued successfully")
        else:
            print("Book is already issued")
    else:
        print("Book not found")


def return_book():
    title = input("Enter book title to return: ")

    if title in books:
        if books[title]["status"] == "Issued":
            books[title]["status"] = "Available"
            print("Book returned successfully")
        else:
            print("Book is already available")
    else:
        print("Book not found")


while True:
    print("\n----- Library Management System -----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Thank you for using Library Management System")
        break

    else:
        print("Invalid choice. Please try again")
