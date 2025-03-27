import math

def calculate_area():
    print("Choose an option to calculate the area:")
    print("1. Rectangle")
    print("2. Circle")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        try:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            print(f"The area of the rectangle is: {area}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
    elif choice == "2":
        try:
            radius = float(input("Enter the radius of the circle: "))
            area = math.pi * radius ** 2
            print(f"The area of the circle is: {area:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    else:
        print("Invalid choice. Please select 1 or 2.")
calculate_area()