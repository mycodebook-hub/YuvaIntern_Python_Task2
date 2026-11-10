
print("PYTHON TUPLE DEMONSTRATION")

# Creating a tuple
colors = ("Red", "Blue", "Green", "Yellow")

print("Original Tuple:", colors)

# Accessing elements
print("First Color:", colors[0])
print("Last Color:", colors[-1])

# Slicing a tuple
print("Selected Colors:", colors[1:3])

# Finding tuple length
print("Tuple Length:", len(colors))

# Counting an element
print("Blue Count:", colors.count("Blue"))

# Finding an element position
print("Green Position:", colors.index("Green"))

# Iterating through a tuple
print("Tuple Elements:")

for color in colors:
    print(color)

print("Tuple Demonstration Completed")
