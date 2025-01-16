def calculate_simple_interest(principal, rate, time):

    interest = (principal * rate * time) / 100
    return interest

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = int(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Output the result
print(f"The Simple Interest is: {simple_interest:.2f}")
