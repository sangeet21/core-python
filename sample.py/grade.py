marks = int(input("Enter your marks: "))

if marks >= 90:
    if marks >= 95:
        print("Grade: A+")
    else:
        print("Grade: A")
elif marks >= 75:
    if marks >= 85:
        print("Grade: B+")
    else:
        print("Grade: B")
else:
    if marks >= 50:
        print("Grade: C")
    else:
        print("Grade: F")
