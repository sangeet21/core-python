age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()

if age >= 18:
    if citizen == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote because you are not a citizen.")
else:
    if citizen == "yes":
        print("You are not eligible to vote because you are under 18.")
    else:
        print("You are not eligible to vote due to age and citizenship.")
