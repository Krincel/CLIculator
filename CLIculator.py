# Import math module for sqrt
import math

# Defining the operations
def add(x, y):
    return x + y 
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("UNDEFINED")
def power(x, y):
     return x ** y
def square_root(x):
    if x == -1:
        print("i")
    elif x < -1:
        raise ValueError("Cannot square root any negative number besides -1!")
    else:
     return math.sqrt(x)
def area_square(x):
    return x ** 2
def area_rectangle(x, y):
    return x * y
def area_triangle(x, y):
    return 0.5 * x * y
def area_circle(x):
    return math.pi * x ** 2

# Display main menu
while True:
    print("\nWelcome to CLIculator!")
    print("Please select an operation: ")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Power")
    print("6: Square Root")
    print("7: Area of 2d Shapes")
    print("8: Exit Program")

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")
    # Exit program
    if choice == "8":
        print("Goodbye!\nExiting program...")
        break
    
    # Handle calc and errors
    if choice in ("1", "2", "3", "4", "5"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
    elif choice == "6":
        try:
            num = float(input("Enter a number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue
        
         # Performing the calculation and handling potential errors
    if choice == "1":
        try: 
         print(f"{num1} + {num2} = {add(num1, num2)}")
        except OverflowError:
            print("Answer is effectively infinite. Please try a smaller number.")
    elif choice == "2":
        try:
         print(f"{num1} - {num2} = {subtract(num1, num2)}")
        except OverflowError:
            print("Answer is effectively infinite. Please try a smaller number.")
    elif choice == "3":
        try:
         print(f"{num1} * {num2} = {multiply(num1, num2)}")
        except OverflowError:
            print("Answer is effectively infinite. Please try a smaller number.")
    elif choice == "4":
        try:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except num2 == 0:
            print(num2)
        except ValueError as e:
            print(e)
    elif choice == "5":
        try:
            print(f"{num1} ** {num2} = {power(num1, num2)}") 
        except OverflowError:
            print("Answer is effectively infinite. Please try a smaller number.")
    elif choice == "6":
        try:
            print(f"Square Root of {num} = {square_root(num)}")
        except ValueError as e:
            print(e)
            
            # Handle 2d areas
    elif choice == "7":
        shape = input("Choose a shape:\nSquare/Rectangle/Triangle/Circle: ")
        if shape.lower() == "square":
            try:
                side = float(input("Enter side length: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue
            print(f"Area where l = {side}: {area_square(side)}")
        
        elif shape.lower() == "rectangle":
            try:
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            print(f"Area where w = {width} and h = {height}: {area_rectangle(width, height)}")
        
        elif shape.lower() == "triangle":
            try:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            print(f"Area where b = {base} and h = {height}: {area_triangle(base, height)}")
        
        elif shape.lower() == "circle":
            try:
                radius = float(input("Enter radius: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue
            print(f"Area where r = {radius}: {area_circle(radius)}")
    else:
            print("Invalid choice! Please try again.")
            continue