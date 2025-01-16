# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"

# Print the result
print(f"The number {number} is {result}.")
