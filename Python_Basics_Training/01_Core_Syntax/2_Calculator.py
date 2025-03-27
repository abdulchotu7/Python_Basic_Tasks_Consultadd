def calculate_arithmetic():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid choice. Please select 1-4.")
            return
        
        print(f"The result is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculate_arithmetic()