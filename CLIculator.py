# Importing the necessary math module
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
    return math.sqrt(x)

# Displaying the main menu
while True:
    print("\nSimple Calculator")
    print("Please select an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Power")
    print("6: Square Root")
    print("7: Exit Program")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    # Exit the program
    if choice == "7":
        print("Goodbye!\nExiting program...")
        break
    
    # Handling the calculation and input errors
    if choice in ("1", "2", "3", "4", "5", "6"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
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
            num = float(input("Enter a number:"))
            print(f"math.sqrt({num}) = {square_root(num)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice! Please try again.")
        continue