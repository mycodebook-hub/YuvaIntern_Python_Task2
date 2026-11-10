word = input("Enter a word: ")

reverse = word[::-1]

if word == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")