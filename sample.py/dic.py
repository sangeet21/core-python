def create_dictionary():
    my_dict = {}
    
    for i in range(5):
        key = input(f"Enter key {i+1}: ")
        value = input(f"Enter value for key '{key}': ")
        my_dict[key] = value
    
    return my_dict

# Create the dictionary
user_dict = create_dictionary()

# Print the resulting dictionary
print("The created dictionary is:", user_dict)



# Initialize an empty dictionary
user_dict = {}

# Loop to get input for five elements
for i in range(5):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for key '{key}': ")
    user_dict[key] = value

# Print the resulting dictionary
print("The created dictionary is:", user_dict)
