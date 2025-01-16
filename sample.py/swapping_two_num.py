# Take two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display original numbers
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swap the numbers
num1, num2 = num2, num1

# Display swapped numbers
print(f"After swapping: num1 = {num1}, num2 = {num2}")
