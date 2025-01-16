# Take input in kilometers from the user
kilometers = float(input("Enter the distance in kilometers: "))

# Conversion factor
conversion_factor = 0.621371

# Convert kilometers to miles
miles = kilometers * conversion_factor

# Display the result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")