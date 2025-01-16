# Input angles
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# Check if the angles form a triangle
if angle1 > 0 and angle2 > 0 and angle3 > 0:
    if angle1 + angle2 + angle3 == 180:
        print("The given angles form a triangle.")
    else:
        print("The given angles do not form a triangle because their sum is not 180.")
